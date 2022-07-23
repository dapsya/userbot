# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, hiro_cmd
from userbot.events import register

# KALO FORK/CLONE ID GC DI BAWAH G USH DI HAPUSS YAA KONTOLL

GCAST_BLACKLIST = [
    -1001512737035,  # HIROSHI SUPPORT
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001380293847,  # Kyy
    -1001456135097,  # SpamBot
    -1001462425381,  # JANGAN DI APUS
    -1001649802697,  # JANGAN DI APUS
    -1001551881481,  # GROUP JUAL JASA
    -1001386557465,  # KITARO SUPPORT
    -1001578091827,  # PRIME SUPPORT
    -1001692751821,  # RAM SUPPORT
    -1001554560763,  # VEGETA SUPPORT
    -1001273141346,  # ALLIANCE SPY SUPORT
    -1001683749664,  # XA SUPPORT
    -1001637312147,  # VIENA SUPPORT
    -1001788983303,  # KAYU SUPPORT
    -1001572486389,  # PLUVIA SUPPORT
    -1001687155877,  # CILIK SUPPORT
    -1001688172956,  # KEKINIAN SUPPORT
    -1001400037668,  # RIO SUPPORT
    -1001538752127,  # ABING SUPPORT
    -1001675396283,  # AYIN SUPPORT
    -1001740774911,  # ZEZANZEZAN SUPPORT
    -1001795125065,  # BASKARA SUPPORT
]


@hiro_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=5098393204,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**PESAN NYA MANA NGENTOT?**")
    kk = await edit_or_reply(event, "**LAGI GUA KIRIM KONTOL, LIMIT JANGAN SALAHIN GUA YA BANGSAT...**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@hiro_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**PESAN NYA MANA NGENTOT?**")
    kk = await edit_or_reply(event, "**LAGI GUA KIRIM KONTOL, LIMIT JANGAN SALAHIN GUA YA BANGSAT...**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
