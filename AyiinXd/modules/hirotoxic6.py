# import by Hiroshi
# Credits @Bisubiarenak
# dont't remove Credits
# From https://github.com/UserbotMaps/Hiroshi-Userbot
# MEMEK YANG APUS CREDIT NYA

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.dsn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DAERAH SITU NAJIS BAT SIH HIDUP LU MANA HIDUP NUMPANG DIEMPERAN RUKO MAKAN MINTA MINTA KALO GA KOREK KOREK TONG SAMPAH KALO GADAPET MAKAN DAUN UDAH KEK KAMBING AJA TOLOL UDAH BULU TEBEL DEKIL BAU LAGI KONTOL DIDIK DULU NOH ADEKLU BIAR GA JADI LACUR KEK MAK LU MANA MASIH KECIL SUKA BAT NYEPONGIN KONTOL TETANGGA CUMA PEN DAPET DUIT JAJAN KARENA HIDUP KELUARGALU TERLALU MISKIN KASIAN BAT SIH MENDING LU JADI ANAK BERGUNA DIKIT TOLOL MANA JADI BEBAN HOBI BAT SIH MABOK MABOKAN MANA MABOK KOMIK UDAH HASIL NYOLONG DARI RUKO ORANG DIH KERJAAN NGAMEN DILAMPU MERAH HABIS ITU BEGAYA PASANG TOGEL CUMA GOCENG BERHARAP BAT DAPET HASIL BUAT NYAMBUNG HIDUPLU YANG GA BERGUNA ITU DIH MAKANYA YA JADI ANAK HARAM JAN KEBANYAKAN TINGKAH KONTOL.**")


@register(outgoing=True, pattern=r"^\.bty(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BOCA TOLOL YANG KELUAR DARI RAHIM ANJING, YANG DI MANA BOKAP LU AJA KERJAAAN NYA CUMA JADI GIGOLO YANG BANYAK BACOT AJE, BOCAH BOCAH WIBU YANG SANGE KALAU LIAT ANIME ANJING LIAT ANIME BISA SANGE TOLOL BOCAH HINA LEBIH BAIK LU NYEMBAH BABI AJA KAN TUHAN LU BABI ANJING BOCAH TOLOL YANG UDAH KENA KANKER  STADIUM 4 YANG UDAH MAU MATI MALAH NGELUARIN SUARA YANG BAU TAI BABI MAKANYA CEWEK GAK ADA YANG MAU SAMA LU KERENA MULUT LU ITU BAU TAI YANG UDAH 7 ABAD GAK PERNAH DI GOSOK.**")


@register(outgoing=True, pattern='^.ebo(?: |$)(.*)')
async def typewriter(kontol):
    kontol.pattern_match.group(1)
    await kontol.edit("**EH BOCAH TOLOL YANG KERJAAN NYA JADI GIGOLO LEBIH BAIK LU APUS TELE DARI PADA DI TELEGRAM JADI RAJA JAMET MENDING GUE YE KAN RAJA PARA ORANG GANTENG TOLOL.**")


@register(outgoing=True, pattern='^\\.niye(?: |$)(.*)')
async def typewriter(memek):
    memek.pattern_match.group(1)
    await memek.edit("**NI YE EMAK LU KEMARIN TUH DATANG KERUMAH GUE MINTA MEMEK NYA DI INJAK YA UDAH GUE INJAK KERENA MAMA LU SANGE LIAT GUE**")


@register(outgoing=True, pattern='^\\.cla(?: |$)(.*)')
async def typewriter(pukii):
    pukii.pattern_match.group(1)
    await pukii.edit("**CEWEK LU AJA PAS KETEMU GUE LANGSUNG TELANJANG KERENA GUE TERLALU GANTENG YANG GANTENG NYA KELWATAN**")

CMD_HELP.update({
    "toxic9":
    "𝘾𝙈𝘿: `.dsn`\
    \n↳ : cobain Kntl"
    "𝘾𝙈𝘿: `.bty`\
    \n↳ : cobain Kntl"
})

CMD_HELP.update({
    "toxic10":
    "𝘾𝙈𝘿: `.ebo`\
    \n↳ : cobain Kntl"
    "𝘾𝙈𝘿: `.niye`\
    \n↳ : cobain Kntl"
    "𝘾𝙈𝘿: `.cla`\
    \n↳ : cobain Kntl"

})
