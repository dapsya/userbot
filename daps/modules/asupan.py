# © @tofik_dn
# ⚠️ Do not remove credits
# recode by @greyyvbss
# video lucu & sad by @JustRex
# video bkp @Bisubiarenak

import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import hiro_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@hiro_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@testimonihiroshi", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Nih Sayang asupannya** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan.**")


@hiro_cmd(pattern="desah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@deshanhiroshi", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"**Jangan Sange ya kak, nih desah buat** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**sange nya ditahan dulu ya kak.**")


@hiro_cmd(pattern="bokep$")
async def _(event):
    try:
        bokepnya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@fakyudurov", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(bokepnya),
            caption=f"**Jangan coli terus kak, nih bokep buat** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**bokep nya ditahan dulu ya kak.**")


@hiro_cmd(pattern="vidlucu$")
async def _(event):
    try:
        vidlucunya = [
            vidlucu
            async for vidlucu in event.client.iter_messages(
                "@videolucuxauserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(vidlucunya),
            caption=f"**Nih kak video lucunya** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video lucu.**")


@hiro_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Ayang nya** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA CAKEP!.**")


@hiro_cmd(pattern="sadvid$")
async def _(event):
    try:
        sadvidnya = [
            sadvid
            async for sadvid in event.client.iter_messages(
                "@sadvideorexa", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sadvidnya),
            caption=f"**Jangan Terlalu Sedih ya kak** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, kayaknya kamu ga pantes untuk sedih :) .")

CMD_HELP.update(
    {
        "asupan": f"**Plugin : **asupan\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}asupan\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}desah\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim voice desah secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}bokep\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video bokep secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vidlucu\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video lucu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ayang\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan Ayang mu, hehe.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}sadvid\
        \n  ☆  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video sad random.\
"
    }
)
