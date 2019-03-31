#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qqmusicbox/api.py was created on 2019/03/31.
file in :relativeFile
Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""
import requests

from QQMusicAPI import QQMusic
from qqmusicbox import logger
log = logger.getLogger(__name__)

class Parse(object):
    @classmethod
    def _song_url_by_id(cls,song_mid='002BbUoO2fU5cV', vkey='', guid='4831279384', fromtag=30):
        music_type = {
            'C400': 'm4a',
            'M500': 'mp3',
            # 'M800': 'mpe',
            # 'A000': 'ape',
            # 'F000': 'flac'
        }  # m4a, mp3普通, mp3高, ape, flac

        url = "http://dl.stream.qqmusic.qq.com/M500{0}.mp3?vkey={1}&guid={2}&fromtag={3}".format(song_mid, vkey, guid, fromtag)
        quality = "mp3 128k"
        return url, quality

    @classmethod
    def song_url(cls, song):
        return Parse._song_url_by_id(song_mid=song.song_mid,
        vkey=song._get_vkey(),
        guid=song.guid)


    @classmethod
    def song_artist(cls, song):
        """[summary]
        singer in song, is a [Singer, Singer]
         [<Singer: name=茅野愛衣, title=茅野愛衣 (かやの あい)>]
         elements:
         singer_mid 004BsEon35Mmxz
        name 茅野愛衣
        title 茅野愛衣 (かやの あい)
        url https://y.qq.com/n/yqq/singer/004BsEon35Mmxz.html
        hot_music []
        music_total_num 0
        Arguments:
            song {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        singer_list = song.singer
        sn_list = list()
        for singer in singer_list:
            sn_list.append(singer.name)

        if len(sn_list) == 0:
            return "未知艺术家"
        elif len(sn_list) == 1:
            return sn_list[0]
        else:
            return "&".join(sn_list)

    @classmethod
    def songs(cls, songs):
        song_info_list = []
        for song in songs:
            url, quality = Parse.song_url(song)
            if not url:
                continue

            # album_name, album_id = Parse.song_album(song)
            song_info = {
                "song_mid": song.song_mid,
                "artist": Parse.song_artist(song),
                "song_name": song.name,
                "mp3_url": url,
                "quality": quality,
                # "expires": song["expires"],
                # "get_time": song["get_time"],
            }
            song_info_list.append(song_info)
        return song_info_list

    @classmethod
    def artists(cls, singer_list):
        return [
            {
                "artists_id": singer.singer_id,
                "artists_name": singer.name,
                "alias": singer.title,
            }
            for singer in singer_list
        ]

    @classmethod
    def albums(cls, albums):
        return [
            {
                "album_id": album["id"],
                "albums_name": album["name"],
                "artists_name": album["artist"]["name"],
            }
            for album in albums
        ]

    @classmethod
    def playlists(cls, playlists):
        return [
            {
                "playlist_id": pl["id"],
                "playlist_name": pl["name"],
                "creator_name": pl["creator"]["nickname"],
            }
            for pl in playlists
        ]



class QQMUSIC(object):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_version(self):
        action = "https://pypi.org/pypi/QQMUSIC-MusicBox/json"
        try:
            return requests.get(action).json()
        except requests.exceptions.RequestException as e:
            log.error(e)
            return {}
    
    def search(self, keywords, stype='songs', offset=0, total="true", limit=50):
        songs = QQMusic.search(keywords)
        result = {stype:songs}
        return result
    
    def dig_info(self, data, dig_type):
        if not data:
            return []
        if dig_type == "songs" or dig_type == "fmsongs":
            songs_list = data.data
            songs = Parse.songs(songs_list)

            return songs

        elif dig_type == "refresh_urls":
            songs_list = data.data
            songs = Parse.songs(songs_list)
            return songs

        elif dig_type == "artists":
            return Parse.artists(data)

        elif dig_type == "albums":
            return Parse.albums(data)

        elif dig_type == "playlists" or dig_type == "top_playlists":
            return Parse.playlists(data)

        elif dig_type == "playlist_classes":
            return list(PLAYLIST_CLASSES.keys())

        elif dig_type == "playlist_class_detail":
            return PLAYLIST_CLASSES[data]
        else:
            raise ValueError("Invalid dig type")
def songs_url(self, song_mid):
    pass

