from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import edit_or_reply, edit_delete, hiro_cmd
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd


@hiro_cmd(pattern="getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "`Mohon Reply Dulu Pesannya Kontol`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_delete(event, "```Mohon Di Balas Ke Replynya```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_delete(event, "`Mohon Reply Dulu Pesannya Kontol`")
        return
    xx = await edit_or_reply(event, "` Sabar Sedang Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1821140802))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Lu Sedang Error Mampus`")
            return
        if response.text.startswith("Forward"):
            await xx.edit("`Mohon Maaf, Orang Kontol Ini Tidak Mempunyai ID Karena Dia Yatim`")
        else:
            await xx.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}getid`"
    "\n↳ : Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
