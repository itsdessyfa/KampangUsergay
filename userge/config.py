# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Config', 'get_version']

import os
from typing import Set
from . import versions
import heroku3
from git import Repo
from pyrogram import filters

from userge import logging, logbot

_REPO = Repo()
_LOG = logging.getLogger(__name__)
logbot.reply_last_msg("Setting Configs ...")


class Config:
    """ Configs to setup Userge """
    API_ID = int(os.environ.get("2299408"))
    API_HASH = os.environ.get("fa5c4c5642806b98a08fc1f95f66ef72")
    WORKERS = int(os.environ.get("WORKERS")) or os.cpu_count() + 4
    BOT_TOKEN = os.environ.get("1635754150:AAEBdH1gD2REAbp_2x9AMSZmYTVP5O796NA", None)
    HU_STRING_SESSION = os.environ.get("BQCJv1OfFx3Ggjif8X2LlgpTb1GU4lkfwf21g6WNFfCfonkhIyBxT4knT6OrpWciOqRWH6Af3l0j4JZAAZBcJzld0LsgJV3UWLQ6iGI43B9mT2DbI>, None)
    OWNER_ID = tuple(filter(lambda x: x, map(int, os.environ.get("1679205837", "0").split())))
    LOG_CHANNEL_ID = int(os.environ.get("-1001413215750"))
    AUTH_CHATS = (OWNER_ID[0], LOG_CHANNEL_ID) if OWNER_ID else (LOG_CHANNEL_ID,)
    DB_URI = os.environ.get("mongodb+srv://Daisyfa:searev12@cluster0.7241a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    LANG = os.environ.get("PREFERRED_LANGUAGE")
    DOWN_PATH = os.environ.get("DOWN_PATH")
    CMD_TRIGGER = os.environ.get(".")
    SUDO_TRIGGER = os.environ.get("SUDO_TRIGGER")
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR")
    ALIVE_MEDIA = os.environ.get("ALIVE_MEDIA", None)
    CUSTOM_PACK_NAME = os.environ.get("honeybee's")
    INSTA_ID = os.environ.get("INSTA_ID")
    INSTA_PASS = os.environ.get("INSTA_PASS")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO")
    UPSTREAM_REMOTE = os.environ.get("UPSTREAM_REMOTE")
    SPAM_WATCH_API = os.environ.get("SPAM_WATCH_API", None)
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    OCR_SPACE_API_KEY = os.environ.get("0c2078b99188957", None)
    OPEN_WEATHER_MAP = os.environ.get("OPEN_WEATHER_MAP", None)
    REMOVE_BG_API_KEY = os.environ.get("GPLyodhzj3uY2fnJbSsnKek8", None)
    WEATHER_DEFCITY = os.environ.get("BALIKPAPAN", None)
    TZ_NUMBER = os.environ.get("TZ_NUMBER", 1)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_PARENT_ID = os.environ.get("G_DRIVE_PARENT_ID", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    GOOGLE_CHROME_DRIVER = os.environ.get("GOOGLE_CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    HEROKU_API_KEY = os.environ.get("b0226bb4-3b2d-41a8-8c6c-5acaeb3745a7", None)
    HEROKU_APP_NAME = os.environ.get("honeybee12", None)
    G_DRIVE_IS_TD = os.environ.get("G_DRIVE_IS_TD") == "true"
    LOAD_UNOFFICIAL_PLUGINS = os.environ.get(
        "LOAD_UNOFFICIAL_PLUGINS") == "true"
    THUMB_PATH = DOWN_PATH + "thumb_image.jpg"
    TMP_PATH = "userge/plugins/temp/"
    MAX_MESSAGE_LENGTH = 4096
    MSG_DELETE_TIMEOUT = 120
    WELCOME_DELETE_TIMEOUT = 120
    EDIT_SLEEP_TIMEOUT = 10
    AUTOPIC_TIMEOUT = 300
    ALLOWED_CHATS = filters.chat([])
    ALLOW_ALL_PMS = True
    USE_USER_FOR_CLIENT_CHECKS = False
    SUDO_ENABLED = False
    SUDO_USERS: Set[int] = set()
    DISABLED_ALL = False
    DISABLED_CHATS: Set[int] = set()
    ALLOWED_COMMANDS: Set[str] = set()
    ANTISPAM_SENTRY = False
    RUN_DYNO_SAVER = False
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] \
        if HEROKU_API_KEY and HEROKU_APP_NAME else None
    STATUS = None
    BOT_FORWARDS = False
    BOT_MEDIA = os.environ.get("BOT_MEDIA", None)
    ### Spotify
    SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID', None)
    SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET', None)
    SPOTIFY_MODE = False
    ### MEME Generator 
    IMGFLIP_ID = os.environ.get('IMGFLIP_ID', None)
    IMGFLIP_PASS = os.environ.get('IMGFLIP_PASS', None)
    ALLOW_NSFW = os.environ.get("ALLOW_NSFW", "False")
    PM_LOG_GROUP_ID = int(os.environ.get("PM_LOG_GROUP_ID", 0))
    PM_LOGGING = False
    DEEP_AI = os.environ.get("DEEP_AI", None)
    ### Last FM
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY", None)
    TG_IDS = [777000, 1087968824, 454000]
    INLINE_NOTES = False


def get_version() -> str:
    """ get KampangUsergay version """
    ver = f"{versions.__major__}.{versions.__minor__}.{versions.__micro__}"
    try:
        if "/camel07/kampangusergay" in Config.UPSTREAM_REPO.lower():
            diff = list(_REPO.iter_commits(f'v{ver}..HEAD'))
            if diff:
                return f"{ver}-Chpt.{len(diff)}"
        else:
            diff = list(_REPO.iter_commits(f'{Config.UPSTREAM_REMOTE}/alpha..HEAD'))
            if diff:
                return f"{ver}-GAY.{len(diff)}"
    except Exception as e:
        _LOG.error(e)
        return "For Fix See -> https://github.com/Camel07/KampangUsergay/issues/17"
    return ver
