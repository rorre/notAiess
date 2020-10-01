from unittest import mock

EVENTS_JSON = [
    {
        "id": 2389105,
        "type": "rank",
        "comment": None,
        "created_at": "2020-09-29T07:43:31+00:00",
        "user_id": None,
        "beatmapset": {
            "artist": "Doja Cat",
            "artist_unicode": "Doja Cat",
            "covers": {
                "cover": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/cover.jpg?1600644042",
                "cover@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/cover@2x.jpg?1600644042",
                "card": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/card.jpg?1600644042",
                "card@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/card@2x.jpg?1600644042",
                "list": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/list.jpg?1600644042",
                "list@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/list@2x.jpg?1600644042",
                "slimcover": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/slimcover.jpg?1600644042",
                "slimcover@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/slimcover@2x.jpg?1600644042",
            },
            "creator": "Plaudible",
            "favourite_count": 178,
            "id": 1107500,
            "play_count": 78,
            "preview_url": "\/\/b.ppy.sh\/preview\/1107500.mp3",
            "source": "Birds of Prey",
            "status": "ranked",
            "title": "Boss Bitch",
            "title_unicode": "Boss Bitch",
            "user_id": 7149815,
            "video": False,
            "user": {
                "avatar_url": "https:\/\/a.ppy.sh\/7149815?1592166734.jpeg",
                "country_code": "US",
                "default_group": "default",
                "id": 7149815,
                "is_active": True,
                "is_bot": False,
                "is_online": False,
                "is_supporter": True,
                "last_visit": "2020-09-29T07:08:00+00:00",
                "pm_friends_only": False,
                "profile_colour": None,
                "username": "Plaudible",
            },
        },
    }
]

BANCHO_EVENT_JSON = [
    {
        "id": 2389105,
        "type": "nominate",
        "comment": None,
        "created_at": "2020-09-29T07:43:31+00:00",
        "user_id": 3,
        "beatmapset": {
            "artist": "Doja Cat",
            "artist_unicode": "Doja Cat",
            "covers": {
                "cover": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/cover.jpg?1600644042",
                "cover@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/cover@2x.jpg?1600644042",
                "card": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/card.jpg?1600644042",
                "card@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/card@2x.jpg?1600644042",
                "list": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/list.jpg?1600644042",
                "list@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/list@2x.jpg?1600644042",
                "slimcover": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/slimcover.jpg?1600644042",
                "slimcover@2x": "https:\/\/assets.ppy.sh\/beatmaps\/1107500\/covers\/slimcover@2x.jpg?1600644042",
            },
            "creator": "Plaudible",
            "favourite_count": 178,
            "id": 1107500,
            "play_count": 78,
            "preview_url": "\/\/b.ppy.sh\/preview\/1107500.mp3",
            "source": "Birds of Prey",
            "status": "ranked",
            "title": "Boss Bitch",
            "title_unicode": "Boss Bitch",
            "user_id": 7149815,
            "video": False,
            "user": {
                "avatar_url": "https:\/\/a.ppy.sh\/7149815?1592166734.jpeg",
                "country_code": "US",
                "default_group": "default",
                "id": 7149815,
                "is_active": True,
                "is_bot": False,
                "is_online": False,
                "is_supporter": True,
                "last_visit": "2020-09-29T07:08:00+00:00",
                "pm_friends_only": False,
                "profile_colour": None,
                "username": "Plaudible",
            },
        },
    }
]

API_JSON = [
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2314613",
        "approved": "1",
        "total_length": "130",
        "hit_length": "109",
        "version": "Insane",
        "file_md5": "c3ae782165001911a0b14a690b5cf374",
        "diff_size": "3.5",
        "diff_overall": "7",
        "diff_approach": "9",
        "diff_drain": "6",
        "mode": "0",
        "count_normal": "231",
        "count_slider": "223",
        "count_spinner": "1",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "49",
        "passcount": "10",
        "packs": None,
        "max_combo": "690",
        "diff_aim": "1.96786",
        "diff_speed": "1.82435",
        "difficultyrating": "3.86396",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2314614",
        "approved": "1",
        "total_length": "130",
        "hit_length": "108",
        "version": "Shine Like Gloss",
        "file_md5": "a43625f02fb61e9a59cc6f02ce612492",
        "diff_size": "4.2",
        "diff_overall": "9.5",
        "diff_approach": "9.8",
        "diff_drain": "6",
        "mode": "0",
        "count_normal": "279",
        "count_slider": "254",
        "count_spinner": "1",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "120",
        "passcount": "7",
        "packs": None,
        "max_combo": "790",
        "diff_aim": "3.79201",
        "diff_speed": "2.69422",
        "difficultyrating": "7.03513",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2321526",
        "approved": "1",
        "total_length": "129",
        "hit_length": "108",
        "version": "Hard",
        "file_md5": "8dfd171c7a9c17d2791a729e929b4227",
        "diff_size": "3.3",
        "diff_overall": "6",
        "diff_approach": "8",
        "diff_drain": "5",
        "mode": "0",
        "count_normal": "96",
        "count_slider": "206",
        "count_spinner": "1",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "44",
        "passcount": "8",
        "packs": None,
        "max_combo": "575",
        "diff_aim": "1.76146",
        "diff_speed": "1.44297",
        "difficultyrating": "3.36367",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2323128",
        "approved": "1",
        "total_length": "129",
        "hit_length": "109",
        "version": "Normal",
        "file_md5": "a0c20eafa1a94c511ef179a7602f9859",
        "diff_size": "3",
        "diff_overall": "4",
        "diff_approach": "5",
        "diff_drain": "4",
        "mode": "0",
        "count_normal": "63",
        "count_slider": "100",
        "count_spinner": "2",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "99",
        "passcount": "20",
        "packs": None,
        "max_combo": "304",
        "diff_aim": "0.867372",
        "diff_speed": "0.815259",
        "difficultyrating": "1.70869",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2323773",
        "approved": "1",
        "total_length": "130",
        "hit_length": "117",
        "version": "Cool's Extreme",
        "file_md5": "e6f32bfebba5a6e5d439b635535a02f5",
        "diff_size": "4",
        "diff_overall": "8.8",
        "diff_approach": "9.4",
        "diff_drain": "5.5",
        "mode": "0",
        "count_normal": "276",
        "count_slider": "266",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "17",
        "passcount": "3",
        "packs": None,
        "max_combo": "818",
        "diff_aim": "3.20118",
        "diff_speed": "2.39071",
        "difficultyrating": "5.99713",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2387726",
        "approved": "1",
        "total_length": "130",
        "hit_length": "109",
        "version": "Shmiklak's Advanced",
        "file_md5": "ce3789f5a6d8b8e9acc81a7a28ec7bab",
        "diff_size": "3.3",
        "diff_overall": "5",
        "diff_approach": "6.5",
        "diff_drain": "4",
        "mode": "0",
        "count_normal": "55",
        "count_slider": "175",
        "count_spinner": "2",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "57",
        "passcount": "22",
        "packs": None,
        "max_combo": "433",
        "diff_aim": "1.27041",
        "diff_speed": "1.18301",
        "difficultyrating": "2.49712",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2395787",
        "approved": "1",
        "total_length": "129",
        "hit_length": "115",
        "version": "schoolboy's Ultra",
        "file_md5": "570dcad7a506481c03d0c239b1a14ba5",
        "diff_size": "4.5",
        "diff_overall": "8.9",
        "diff_approach": "9.6",
        "diff_drain": "6",
        "mode": "0",
        "count_normal": "239",
        "count_slider": "302",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "48",
        "passcount": "1",
        "packs": None,
        "max_combo": "848",
        "diff_aim": "3.43066",
        "diff_speed": "2.5369",
        "difficultyrating": "6.41445",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2402711",
        "approved": "1",
        "total_length": "130",
        "hit_length": "108",
        "version": "Another",
        "file_md5": "54915271cd5347dc6a9b50e446bb590d",
        "diff_size": "3.7",
        "diff_overall": "8",
        "diff_approach": "9",
        "diff_drain": "5",
        "mode": "0",
        "count_normal": "211",
        "count_slider": "254",
        "count_spinner": "1",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "75",
        "passcount": "10",
        "packs": None,
        "max_combo": "725",
        "diff_aim": "2.37107",
        "diff_speed": "2.32348",
        "difficultyrating": "4.71835",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2402712",
        "approved": "1",
        "total_length": "130",
        "hit_length": "109",
        "version": "jas' Extra",
        "file_md5": "b4403602883191688f32894e091c27cb",
        "diff_size": "4.3",
        "diff_overall": "8.5",
        "diff_approach": "9.2",
        "diff_drain": "5",
        "mode": "0",
        "count_normal": "192",
        "count_slider": "212",
        "count_spinner": "2",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "7",
        "passcount": "1",
        "packs": None,
        "max_combo": "688",
        "diff_aim": "3.03368",
        "diff_speed": "2.37671",
        "difficultyrating": "5.73887",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2422429",
        "approved": "1",
        "total_length": "130",
        "hit_length": "116",
        "version": "Digi's Skinny Extra",
        "file_md5": "aa661ce698a9bcd69c2d1f8632b211d7",
        "diff_size": "4.1",
        "diff_overall": "8.5",
        "diff_approach": "9.3",
        "diff_drain": "5",
        "mode": "0",
        "count_normal": "241",
        "count_slider": "300",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "11",
        "passcount": "1",
        "packs": None,
        "max_combo": "848",
        "diff_aim": "3.06137",
        "diff_speed": "2.39833",
        "difficultyrating": "5.79122",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2425079",
        "approved": "1",
        "total_length": "130",
        "hit_length": "115",
        "version": "Asphyxia's Extra",
        "file_md5": "72b06d99f01520df8337498dfe6ca30a",
        "diff_size": "4.3",
        "diff_overall": "8",
        "diff_approach": "9.4",
        "diff_drain": "5",
        "mode": "0",
        "count_normal": "183",
        "count_slider": "334",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "47",
        "passcount": "6",
        "packs": None,
        "max_combo": "861",
        "diff_aim": "2.85625",
        "diff_speed": "2.37557",
        "difficultyrating": "5.47216",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2425080",
        "approved": "1",
        "total_length": "130",
        "hit_length": "122",
        "version": "Cub's Extra",
        "file_md5": "f328c094be900725e343fa590f5367c6",
        "diff_size": "4",
        "diff_overall": "8.3",
        "diff_approach": "9.4",
        "diff_drain": "5.5",
        "mode": "0",
        "count_normal": "271",
        "count_slider": "298",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "53",
        "passcount": "3",
        "packs": None,
        "max_combo": "882",
        "diff_aim": "2.86857",
        "diff_speed": "2.49151",
        "difficultyrating": "5.54861",
    },
    {
        "beatmapset_id": "1107500",
        "beatmap_id": "2487993",
        "approved": "1",
        "total_length": "130",
        "hit_length": "109",
        "version": "Gero's Insane",
        "file_md5": "15d056373a263aac2ec7b193bc787638",
        "diff_size": "4",
        "diff_overall": "7",
        "diff_approach": "9",
        "diff_drain": "6",
        "mode": "0",
        "count_normal": "215",
        "count_slider": "238",
        "count_spinner": "0",
        "submit_date": "2020-02-10 05:29:22",
        "approved_date": "2020-09-29 07:43:31",
        "last_update": "2020-09-20 23:20:18",
        "artist": "Doja Cat",
        "artist_unicode": "Doja Cat",
        "title": "Boss Bitch",
        "title_unicode": "Boss Bitch",
        "creator": "Plaudible",
        "creator_id": "7149815",
        "bpm": "126",
        "source": "Birds of Prey",
        "tags": "riot games valorant jett jas craezy asphyxia cubby cubbby komore schoolboy marvollo m_a_r_v_o_l_l_o shmiklak c00l cool gero digidrake pop english fantabulous emancipation of one harley quinn ost original soundtrack",
        "genre_id": "5",
        "language_id": "2",
        "favourite_count": "178",
        "rating": "8.69697",
        "storyboard": "1",
        "video": "0",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "83",
        "passcount": "13",
        "packs": None,
        "max_combo": "701",
        "diff_aim": "2.14529",
        "diff_speed": "2.0722",
        "difficultyrating": "4.25404",
    },
]

USERS_JSON = [
    {
        "avatar_url": "https:\/\/a.ppy.sh\/3378391?1585838216.jpeg",
        "country_code": "ID",
        "default_group": "bng",
        "id": 3378391,
        "is_active": True,
        "is_bot": False,
        "is_online": True,
        "is_supporter": True,
        "last_visit": "2020-10-01T04:07:00+00:00",
        "pm_friends_only": False,
        "profile_colour": "#6B3FA0",
        "username": "-Keitaro",
        "country": {"code": "ID", "name": "Indonesia"},
        "cover": {
            "custom_url": "https:\/\/assets.ppy.sh\/user-profile-covers\/3378391\/e67a3e74eb2f30f4d84c7b6219f97c80b74f8ca2aa344dc938dc3c479cda6775.jpeg",
            "url": "https:\/\/assets.ppy.sh\/user-profile-covers\/3378391\/e67a3e74eb2f30f4d84c7b6219f97c80b74f8ca2aa344dc938dc3c479cda6775.jpeg",
            "id": None,
        },
        "current_mode_rank": 36433,
        "groups": [
            {
                "id": 28,
                "identifier": "bng",
                "name": "Beatmap Nominators",
                "short_name": "BN",
                "description": "",
                "colour": "#A347EB",
            }
        ],
        "support_level": 1,
    }
]

bancho_event_mock = mock.AsyncMock(return_value=BANCHO_EVENT_JSON)
events_mock = mock.AsyncMock(return_value=EVENTS_JSON)
api_mock = mock.AsyncMock(return_value=API_JSON)
users_mock = mock.AsyncMock(return_value=USERS_JSON)
