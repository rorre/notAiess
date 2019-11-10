from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from bs4 import BeautifulSoup

from .helper import get_api, get_beatmap_api, get_discussion_json


class EventBase(ABC):
    """An Abstract Class (ABC) representing base osu! beatmapset event.

    Attributes
    ----------
    creator: str
        Mapper of beatmap.
    artist: str
        Beatmap's artist.
    title: str
        Beatmap's title.
    map_cover: str
        URL to map's cover image.
    user_action: str
        User in charge of the event.
    user_id_action: int
        ``user_action``'s user id.
    time: datetime
        A ``datetime`` object representing the time where the event happened.
    event_type: str
        Event that happened on the beatmap (bubbled, qualified, etc.)
    event_source_url: str
        URL to event cause.
    gamemodes: list of str
        Game modes inside the beatmapset.
    beatmap: osuClasses.Beatmap
        The difficulty of the beatmap, usually the first entry from osu! API.
    beatmapset: list of osuClasses.Beatmap
        Array of difficulties inside the beatmap.
    source: Source
        Representation of the beatmapset event source.
    """

    def __init__(self, soup: BeautifulSoup, nextevent: BeautifulSoup = None):
        self.soup = soup
        self.next_map = nextevent
        self.beatmapset = None
        self.beatmap = None

    async def _get_map(self):
        """Receive map from osu! API"""
        map_id = self.soup.a.get("href").split("/")[4]
        self.beatmapset = await get_beatmap_api(s=map_id)
        self.beatmap = self.beatmapset[0]

    @property
    def creator(self) -> str:
        return self.beatmap.creator

    @property
    def artist(self) -> str:
        return self.beatmap.artist

    @property
    def title(self) -> str:
        return self.beatmap.title

    @property
    def map_cover(self) -> str:
        return self.soup.a.img.get("src")

    @property
    def user_html(self):
        return self.soup.find(class_="beatmapset-event__content").a

    def user_action(self) -> str:
        return self.user_html.text.strip()

    def user_id_action(self) -> int:
        return int(self.user_html.get('data-user-id'))

    @property
    def time(self) -> datetime:
        dt = self.soup.find(class_="timeago").get("datetime")
        return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S+00:00')

    @abstractmethod
    def event_type(self):
        pass

    @property
    def event_source_url(self) -> str:
        return f"https://osu.ppy.sh/s/{self.beatmap.beatmapset_id}"

    @property
    def gamemodes(self) -> List[str]:
        mode_num = {
            "0": "osu",
            "1": "taiko",
            "2": "catch",
            "3": "mania"
        }
        modes = []
        for diff in self.beatmapset:
            if mode_num[diff.mode] not in modes:
                modes.append(mode_num[diff.mode])
        return modes

    @property
    def source(self):
        return Source(
            self.event_source_url,
            self.user_action(),
            self.user_id_action()
        )


class Source:
    """Representation of the beatmapset event source

    Attributes
    ----------
    post: dict
        The post/thread causing the event. (raises ``Exception`` if its a Nomination post)
    user: dict
        osu! API user object of the user that causes the event.
    """

    def __init__(self, src_url: str, username: str = None, user_id: int = None,
                 post: dict = None, user: dict = None):
        self.src_url = src_url
        self._username = username
        self._user_id = user_id
        self._user = user
        self._post = post

    async def post(self):
        if "discussion" not in self.src_url:
            raise Exception("Nominations doesn't have posts.")
        if self._post:
            return self._post
        post_url = self.src_url
        post_id = int(post_url.split('/')[-1])
        discussion_parents = await get_discussion_json(post_url)
        sourcePost = None
        for discussion in discussion_parents:
            if not discussion:
                continue
            discussion_id = discussion.get("id")
            if discussion_id == post_id:
                sourcePost = discussion['posts'][0]
                break
        return sourcePost

    async def user(self):
        if self._user:
            return self._user
        api_response = list()
        if self._username:
            api_response = await get_api("get_user", u=self._username)
        elif self._user_id:
            api_response = await get_api("get_user", u=self._user_id)
        elif self.src_url:
            post = await self.post()
            api_response = await get_api("get_user", u=post['user_id'])
        return api_response[0]


class Handler:
    """Handler base for ``notAiess``

    Parameters
    ----------
    webhook_url: str
        Discord webhook url to send
    """

    def __init__(self, webhook_url):
        self.hook_url = webhook_url

    def register_emitter(self, emitter):
        self.emitter = emitter
        self._register_events()

    def _register_events(self):
        for func in dir(self):
            if not func.startswith("on_"):
                continue
            if func == "on_map_event":
                self.emitter.on("map_event", getattr(self, func))
            elif func == "on_group_added":
                self.emitter.on("group_added", getattr(self, func))
            elif func == "on_group_removed":
                self.emitter.on("group_removed", getattr(self, func))
            elif func == "on_group_probation":
                self.emitter.on("bng_limited", getattr(self, func))
            else:
                self.emitter.on(func.split("_")[-1], getattr(self, func))

    async def on_map_event(self, event):
        pass

    async def on_map_bubbled(self, event):
        pass

    async def on_map_qualified(self, event):
        pass

    async def on_map_disqualified(self, event):
        pass

    async def on_map_popped(self, event):
        pass

    async def on_map_ranked(self, event):
        pass

    async def on_map_loved(self, event):
        pass

    async def on_group_added(self, user):
        pass

    async def on_group_removed(self, user):
        pass

    async def on_group_probation(self, user):
        pass

    async def on_group_gmt(self, user):
        pass

    async def on_group_bng(self, user):
        pass

    async def on_group_nat(self, user):
        pass

    async def on_group_alumni(self, user):
        pass
