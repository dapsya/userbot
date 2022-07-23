# Created by @punya_alby
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# ⚠️ Do not remove credits ⚠️

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HANDLER as cmd, CMD_HELP
from userbot.utils import edit_or_reply, hiro_cmd
from userbot.events import register


@hiro_cmd(pattern="nulis(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_or_reply(event, "`Tambahin Tulisan yang mau dibuat`")
    else:
        await edit_or_reply(event, "`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@hiro_cmd(pattern="nulis1(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_or_reply(event, "`Tambahin Tulisan yang mau dibuat`")
    else:
        await edit_or_reply(event, "`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis2(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis3(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis4(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis5(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis6(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis7(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis8(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis9(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis10(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


@register(outgoing=True, pattern=r"^\.nulis11(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"Tulisan by [🔥 ʜɪʀᴏsʜɪ ᴜꜱᴇʀʙᴏᴛ 🔥](https://t.me/bombleebas/197)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


CMD_HELP.update(
    {
        "nulis": f"❖ **Plugin : **`nulis`\
        \n\n ┌❖ **Perintah :** `{cmd}nulis <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 1.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis1 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas kedua dengan font 1.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis2 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas ketiga dengan font 1.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis3 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas keempat dengan font 1.\
    "
    }
)

CMD_HELP.update(
    {
        "nulis2": f"❖ **Plugin : **`nulis kedua`\
        \n\n ┌❖ **Perintah :** `{cmd}nulis4 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 2.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis5 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas kedua dengan font 2.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis6 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas ketiga dengan font 2.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis7 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas keempat dengan font 2.\
    "
    }
)

CMD_HELP.update(
    {
        "nulis3": f"❖ **Plugin : **`nulis ketiga`\
        \n\n ┌❖ **Perintah :** `{cmd}nulis8 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 3.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis9 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas kedua dengan font 3.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis10 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas ketiga dengan font 3.\
        \n\n ┌❖ **Perintah :** `{cmd}nulis11 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas keempat dengan font 3.\
    "
    }
)
