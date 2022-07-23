# SEPESIAL THANKS @JustRex
# Hiroshi-Userbot
# Special Ramadhan

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, hiro_cmd


@hiro_cmd(pattern="sholat2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**LU NGAPAIN PUASA KALO GA SHOLAT TOLOL?BATALAIN AJA GOBLOK!**")


@hiro_cmd(pattern="bukber5(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**kemarin ada yang ngajak gua bukber, tapi Cuma wacana, Kalo tau gitu ga usah ajak ajak gua bukber ye anj!**")


@hiro_cmd(pattern="setan4(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**TAU GA LU?**")
    sleep(1.5)
    await edit_or_reply(event, "**Lo itu SETAN yang Lolos waktu pintu NERAKA ditutup!**")


@hiro_cmd(pattern="taraw3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**TARAWEH BEGO BUKAN MAIN TELE! KIBLAT LU TELEGRAM EMANG?**")


@hiro_cmd(pattern="taraw4(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Malu napa bego, yang lain pada taraweh lo kagak! gua sih malu**")


@hiro_cmd(pattern="mp(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Setidaknya KALO GA PUASA MALU NAPA GOBLOK JANGAN DIUMBAR UMBAR, KESANNYA NORAK!**")


@hiro_cmd(pattern="pk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BUAT COWO YANG GAK PUASA, POTONG AJA KONTOLNYA!!**")


@hiro_cmd(pattern="aus1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**LAGI WUDHU GA SENGAJA KEMINUM, YAUDAH GUA LANJUTIN MINUM AIR KULKAS**")


@hiro_cmd(pattern="aus2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BELI ES CEKEK ENAK BGT INI ASLI DAH **")


@hiro_cmd(pattern="tox1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Lagi ga pengen toxic soalnya puasa**")


@hiro_cmd(pattern="setan5(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GUA GA GAMPANG KEHASUT SETAN KEK LU YA !**")


@hiro_cmd(pattern="kolek1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BAGI KOLEK LAH!!!!**")


@hiro_cmd(pattern="sebat1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BENTAR....**")
    sleep(1.5)
    await edit_or_reply(event, "**GUA SEBAT DULU ABIS ITU LANJUT PUASA**")


@hiro_cmd(pattern="sah(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SAHUR DOANG PUASA KAGAK!!!!**")


@hiro_cmd(pattern="mamadede(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**NOBAR MAMA DEDE SKUY!!!**")


@hiro_cmd(pattern="warp(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**WAR WER WOR! PUASA TOLOL!**")


CMD_HELP.update(
    {
        "hiropuasa2": f"**Plugin : **`ramadhan2`\
        \n\n    **Perintah :** `{cmd}sholat2`\
        \n✙    **Fungsi : **ngatain orang yang puasa tapi ga sholat.\
        \n\n    **Perintah :** `{cmd}bukber5`\
        \n✙    **Fungsi : **Cobain aja lah anjg.\
        \n\n    **Perintah :** `{cmd}setan4`\
        \n✙    **Fungsi : **ngatain orang setan.\
        \n\n    **Perintah :** `{cmd}setan5`\
        \n✙    **Fungsi : **Ini buat lu hehe.\
        \n\n    **Perintah :** `{cmd}taraw4`\
        \n✙    **Fungsi : **taraweh, intinya cobain aja.\
        \n\n    **Perintah :** `{cmd}mp`\
        \n✙    **Fungsi : **malu gblk klo ga puasa?.\
        \n\n    **Perintah :** `{cmd}pk`\
        \n✙    **Fungsi : **Potong aja kontolnya.\
        \n\n    **Perintah :** `{cmd}aus1`\
        \n✙    **Fungsi : **cobain aja.\
        \n\n    **Perintah :** `{cmd}aus2`\
        \n✙    **Fungsi : **ini kalo misalnya lu aus.\
        \n\n    **Perintah :** `{cmd}tox1`\
        \n✙    **Fungsi : **toxic dikit hehe.\
        \n\n    **Perintah :** `{cmd}kolek`\
        \n✙     **Fungsi: **minta kolek.\
        \n\n    **Perintah :** `{cmd}sebat1`\
        \n✙    **Fungsi : **sebat dikit.\
        \n\n    **Perintah :** `{cmd}sah`\
        \n✙    **Fungsi : **cobain aja.\
        \n\n    **Perintah:** `{cmd}mamadede`\
        \n✙    **Fungsi: **nobar mama dede.\
        \n\n    **Perintah:** `{cmd}warp`\
        \n✙    **Fungsi: **ngatain war."
    })
