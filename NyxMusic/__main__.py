#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/NyxMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/NyxMusic/blob/master/LICENSE >
#
# All rights reserved.
import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from NyxMusic import HELPABLE, LOGGER, app, userbot
from NyxMusic.core.call import Nyx
from NyxMusic.plugins import ALL_MODULES
from NyxMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if len(config.STRING_SESSIONS) == 0:
        LOGGER("NyxMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("NyxMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("NyxMusic.plugins").info("Successfully Imported All Modules ")
    await userbot.start()
    await Nyx.start()
    LOGGER("NyxMusic").info("Assistant Started Sucessfully")
    try:
        await Nyx.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("NyxMusic").error(
            "Please ensure the voice call in your log group is active."
        )
        sys.exit()

    await Nyx.decorators()
    LOGGER("NyxMusic").info("NyxMusic Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("NyxMusic").info("Stopping NyxMusic! GoodBye")
