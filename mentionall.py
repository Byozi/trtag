import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import requests
from bs4 import BeautifulSoup
from datetime import date
from PIL import Image
import io
from urllib.parse import quote

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = 1449935113
bot_name = Config.BOT_NAME

SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []
tekli_calisan = []
ozel_list = [1449935113]

emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧".split(" ")

bayrak = "🇹🇷 🇩🇪 🇫🇷 🇮🇹 🇪🇸 🇬🇧 🇺🇸 🇨🇦 🇯🇵 🇨🇳 🇰🇷 🇷🇺 🇧🇷 🇦🇺 🇳🇱 🇧🇪 🇸🇪 🇳🇴 🇫🇮 🇩🇰".split(" ")

# ================= STICKER KOMUTU =================
@client.on(events.NewMessage(pattern="^/sticker$"))
async def sticker_command(event):
    if not event.is_reply:
        return await event.reply("**Bir görsele yanıt vererek /sticker yaz**")

    reply = await event.get_reply_message()
    if not reply.media:
        return await event.reply("**Yanıtlanan mesajda görsel yok**")

    msg = await event.reply("🎨 **Sticker hazırlanıyor...**")

    try:
        raw = await client.download_media(reply.media, bytes)

        img = Image.open(io.BytesIO(raw)).convert("RGBA")
        img.thumbnail((512, 512))

        output = io.BytesIO()
        img.save(output, format="PNG")
        output.seek(0)

        await client.send_file(
            event.chat_id,
            file=output,
            file_name="sticker.png",
            attributes=[
                DocumentAttributeSticker(
                    alt="✨",
                    stickerset=InputStickerSetEmpty()
                )
            ]
        )

        await msg.delete()
        await event.delete()

    except Exception as e:
        await msg.edit(f"❌ **Sticker hatası:** `{e}`")


# ================= START =================

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    await event.reply(
        "**💭 Sera Tag Bot** çalışıyor!\n\n"
        "Komutları görmek için /help yazabilirsiniz.",
        buttons=[
            [Button.url("➕ Beni Gruba Ekle", f"https://t.me/{bot_username}?startgroup=a")],
            [Button.url("Müzik Botu", "https://t.me/seramusicbot")],
            [Button.url("Teknik Destek", "https://t.me/scrable")]
        ],
        link_preview=False
    )

# ================= HELP =================

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    helptext = (
        "**💭 Sera Tag Bot Komutları**\n\n"
        "**/start** - Botu başlatır\n"
        "**/tag** <Açıklama> - 7'li etiket\n"
        "**/etag** <Açıklama> - Emoji ile etiket\n"
        "**/stag** - Günaydın etiket\n"
        "**/gtag** - İyi geceler etiket\n"
        "**/otag** - İltifatlı etiket\n"
        "**/tektag** <Açıklama> - Tek tek etiket\n"
        "**/admins** <Açıklama> - Yöneticileri etiketler\n"
        "**/btag** - Bayraklı etiket\n"
        "**/burc** - Günlük burç yorumu\n"
        "**/sticker** - Bir görsele yanıt ver, sticker yapar\n"
        "**/iptal** - Etiket işlemini durdurur\n\n"
        "Açıklama yazan yerlere mesaj ekleyebilirsiniz."
    )

    await event.reply(helptext, link_preview=False)

# ================= IPTAL =================

@client.on(events.NewMessage(pattern="^/iptal$"))
async def cancel(event):
    if event.chat_id in anlik_calisan:
        anlik_calisan.remove(event.chat_id)
    if event.chat_id in tekli_calisan:
        tekli_calisan.remove(event.chat_id)

    await event.reply("❌ **İşlem durduruldu.**")

# ================= TAG =================

@client.on(events.NewMessage(pattern="^/tag (.+)$"))
async def tag(event):
    if event.is_private:
        return await event.reply("Bu komut gruplar içindir.")

    admins = [admin.id async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins)]
    if event.sender_id not in admins:
        return await event.reply("❌ **Sadece yöneticiler kullanabilir.**")

    msg = event.pattern_match.group(1)
    anlik_calisan.append(event.chat_id)

    users = []
    async for user in client.iter_participants(event.chat_id):
        users.append(user)

    usrnum, usrtxt = 0, ""
    for user in users:
        usrnum += 1
        usrtxt += f"[{user.first_name}](tg://user?id={user.id}), "
        if usrnum == 7:
            if event.chat_id not in anlik_calisan:
                return
            await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum, usrtxt = 0, ""

# ================= TEST =================

@client.on(events.NewMessage(pattern="/test"))
async def test(event):
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("Yetkin yok.")
    await event.reply("✅ **Bot çalışıyor.**")

print(">> Bot çalışıyor 🚀 <<")
client.run_until_disconnected()
