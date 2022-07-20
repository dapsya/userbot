# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from Daps import BOT_TOKEN
from Daps import BOT_VER as version
from Daps import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    DAPS2,
    DAPS3,
    DAPS4,
    DAPS5,
    DAPS6,
    DAPS7,
    DAPS8,
    DAPS9,
    DAPS10,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    STRING_SESSION,
    blacklistdap,
    bot,
    call_py,
    tgbot,
)
from Daps.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nMan-UserBot v{}, Copyright © 2021-2022 Dap• <https://github.com/dapsya>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\ndaps_userBot v{}, Copyright © 2021-2022 Daps• <https://github.com/dapsya>"


async def daps_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multidaps():
    if 1230443490 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001531612874 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1230443490 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(daps_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            DAPS2.start()
            LOOP.run_until_complete(daps_client(DAPS2))
            user = DAPS2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            DAPS3.start()
            LOOP.run_until_complete(daps_client(DAPS3))
            user = DAPS3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            DAPS4.start()
            LOOP.run_until_complete(daps_client(DAPS4))
            user = DAPS4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            DAPS5.start()
            LOOP.run_until_complete(daps_client(DAPS5))
            user = DAPS5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_6:
        try:
            DAPS6.start()
            LOOP.run_until_complete(daps_client(DAPS6))
            user = DAPS6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            DAPS7.start()
            LOOP.run_until_complete(daps_client(DAPS7))
            user = DAPS7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            DAPS8.start()
            LOOP.run_until_complete(daps_client(DAPS8))
            user = DAPS8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            DAPS9.start()
            LOOP.run_until_complete(daps_client(DAPS9))
            user = DAPS9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_10:
        try:
            DAPS10.start()
            LOOP.run_until_complete(daps_client(DAPS10))
            user = DAPS10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1
    if not STRING_10:
        failed += 1
    return failed# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from Daps import BOT_TOKEN
from Daps import BOT_VER as version
from Daps import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    DAPS2,
    DAPS3,
    DAPS4,
    DAPS5,
    DAPS6,
    DAPS7,
    DAPS8,
    DAPS9,
    DAPS10,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    STRING_SESSION,
    blacklistdap,
    bot,
    call_py,
    tgbot,
)
from Daps.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nDaps-UserBot v{}, Copyright © 2021-2022 Dap• <https://github.com/dapsya>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\ndaps_userBot v{}, Copyright © 2021-2022 Daps• <https://github.com/dapsya>"


async def daps_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multidaps():
    if 1230443490 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001531612874 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1230443490 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(daps_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            DAPS2.start()
            LOOP.run_until_complete(daps_client(DAPS2))
            user = DAPS2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            DAPS3.start()
            LOOP.run_until_complete(daps_client(DAPS3))
            user = DAPS3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            DAPS4.start()
            LOOP.run_until_complete(daps_client(DAPS4))
            user = DAPS4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            DAPS5.start()
            LOOP.run_until_complete(daps_client(DAPS5))
            user = DAPS5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_6:
        try:
            DAPS6.start()
            LOOP.run_until_complete(daps_client(DAPS6))
            user = DAPS6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            DAPS7.start()
            LOOP.run_until_complete(daps_client(DAPS7))
            user = DAPS7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            DAPS8.start()
            LOOP.run_until_complete(daps_client(DAPS8))
            user = DAPS8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            DAPS9.start()
            LOOP.run_until_complete(daps_client(DAPS9))
            user = DAPS9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_10:
        try:
            DAPS10.start()
            LOOP.run_until_complete(daps_client(DAPS10))
            user = DAPS10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistdaps:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1
    if not STRING_10:
        failed += 1
    return failed
