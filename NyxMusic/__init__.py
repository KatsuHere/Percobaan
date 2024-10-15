#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/NyxMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/NyxMusic/blob/master/LICENSE >
#
# All rights reserved.

from NyxMusic.core.bot import NyxBot
from NyxMusic.core.dir import dirr
from NyxMusic.core.git import git
from NyxMusic.core.userbot import Userbot
from NyxMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()
# Bot Client
app = NyxBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Saavn = SaavnAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
