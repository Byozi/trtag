import random
import os
import logging
import asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    DocumentAttributeSticker,
    InputStickerSetEmpty,
    InputStickerSetShortName
)
from telethon.tl.functions.stickers import CreateStickerSetRequest, AddStickerToSetRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetItem, InputDocument
from asyncio import sleep
from Config import Config
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import date
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
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

# Botun kendi sticker pack'i için benzersiz isim
STICKER_PACK_NAME = f"sera_sticker_by_{bot_username.replace('@', '')}"

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    await event.reply("**Sera Tag Bot** çalışıyor!\n Ben gruplarınızdaki tüm kullanıcılara etiket atmaya yarayan son derece basit kullanıma sahip bir botum. Komutlarımı görmek için /help yazabilirsiniz.\n\n Tamamen ücretsiz olarak hizmet vermekteyim. Gruplarınıza eklemekten çekinmeyiniz. ",
                      buttons=(
                          [Button.url('Beni Gruba Ekle ', f"https://t.me/{bot_username}?startgroup=a")],
                          [Button.url('Müzik Botu', f"https://t.me/seramusicbot")],
                          [Button.url('Teknik Destek', 'https://t.me/scrable')],
                          [Button.url('Tüm Diğer Botlar', 'https://t.me/serabotu')],
                      ),
                      link_preview=False
                     )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    helptext = "**Sera Tag Bot Komutları**\n\n" \
               "**/start** - Botu başlatır\n" \
               "**/tag** <metin> - Tüm üyeleri 7’şerli etiketler\n" \
               "**/etag** <metin> - Emoji ile etiketler\n" \
               "**/stag** - Rastgele günaydın mesajı ile etiketler\n" \
               "**/gtag** - Rastgele iyi geceler mesajı ile etiketler\n" \
               "**/otag** - Rastgele iltifat mesajı ile etiketler\n" \
               "**/tektag** <metin> - Üyeleri tek tek etiketler\n" \
               "**/admins** <metin> - Yöneticileri etiketler\n" \
               "**/btag** <metin> - Bayrak emojisi ile etiketler\n" \
               "**/sticker** - Alıntılanan görseli gerçek çıkartma (sticker) yapar ve gönderir\n" \
               "**/burc** <burç> - Günlük burç yorumu\n" \
               "**/iptal** - Etiketleme işlemini durdurur"
    
    await event.reply(helptext,
                      buttons=(
                          [Button.url('Beni Gruba Ekle', f"https://t.me/{bot_username}?startgroup=a")],
                          [Button.url('Müzik Botu', f"https://t.me/seramusicbot")],
                          [Button.url('Teknik Destek', 'https://t.me/scrable')],
                          [Button.url('Tüm Diğer Botlar', 'https://t.me/serabotu')],
                      ),
                      link_preview=False
                      )

@client.on(events.NewMessage(pattern="^/yardim$"))
async def yardim(event):
    user_id = event.sender_id
    await client.send_message(user_id, "/yardim")

@client.on(events.NewMessage(pattern='^(?i)/iptal'))
async def cancel(event):
    if event.chat_id in anlik_calisan:
        anlik_calisan.remove(event.chat_id)
    if event.chat_id in tekli_calisan:
        tekli_calisan.remove(event.chat_id)
    
    if event.chat_id in rxyzdev_tagTot:
        await event.respond(f"**Etiket işlemi durduruldu.\n\nEtiketlenen kişi sayısı:** `{rxyzdev_tagTot[event.chat_id]}`")
    else:
        await event.respond("**Durdurulacak aktif işlem yok.**")

emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩 🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")

# GERÇEK STICKER (ÇIKARTMA) KOMUTU - Pack oluşturur ve sticker ekler
@client.on(events.NewMessage(pattern="^/sticker$"))
async def sticker_command(event):
    if event.is_private:
        return await event.reply("**Bu komut sadece gruplarda ve kanallarda kullanılabilir.**")

    if not event.is_reply:
        return await event.reply("**Lütfen bir görsele (fotoğraf, GIF vb.) alıntı yaparak /sticker yazın.**")

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.media:
        return await event.reply("**Alıntılanan mesajda görsel bulunamadı.**")

    processing = await event.reply("**Çıkartma oluşturuluyor, lütfen bekleyin...** ✨")

    try:
        # Görseli indir ve upload et
        file_bytes = await client.download_media(reply_msg.media, bytes)
        uploaded_file = await client.upload_file(file_bytes)

        # Sticker pack var mı kontrol et, yoksa oluştur
        try:
            # Pack varsa sticker ekle
            await client(AddStickerToSetRequest(
                stickerset=InputStickerSetShortName(short_name=STICKER_PACK_NAME),
                sticker=InputStickerSetItem(
                    document=uploaded_file,
                    emojis="✨"
                )
            ))
        except Exception as pack_error:
            if "STICKERSET_INVALID" in str(pack_error):
                # Pack yoksa oluştur
                await client(CreateStickerSetRequest(
                    user_id=await client.get_me(),
                    title="Sera Bot Stickers",
                    short_name=STICKER_PACK_NAME,
                    stickers=[InputStickerSetItem(
                        document=uploaded_file,
                        emojis="✨"
                    )]
                ))
            else:
                raise pack_error

        # Yeni eklenen sticker'ı al ve gönder
        sticker_set = await client(GetStickerSetRequest(
            stickerset=InputStickerSetShortName(short_name=STICKER_PACK_NAME),
            hash=0
        ))

        # Pack'teki son sticker'ı gönder
        last_sticker = sticker_set.documents[-1]

        await client.send_file(event.chat_id, last_sticker)

        await processing.delete()
        await event.delete()

    except Exception as e:
        await processing.edit(f"**Çıkartma oluşturulurken hata:**\n`{str(e)}`")
        LOGGER.error(f"Sticker hatası: {str(e)}")

# Diğer tüm komutlar orijinal haliyle aynı kalıyor...
@client.on(events.NewMessage(pattern="^/btag([\s\S]*)"))
async def mentionall(event):
    if event.is_private:
        return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
 
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("**Üzgünüm, Bu komutu sadece yöneticiler kullanabilir.**")
 
    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = event.reply_to_msg_id
    else:
        return await event.respond("**Etikete Başlamak için <Açıklama> yazın...!**")
 
    if mode == "text_on_cmd":
        anlik_calisan.append(event.chat_id)
        usrnum = 0
        usrtxt = ""
        async for usr in client.iter_participants(event.chat_id):
          usrnum += 1
          usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
          if event.chat_id not in anlik_calisan:
            await event.respond("**Etiket işlemi durduruldu**")
            return
          if usrnum == 7:
            await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

# (Diğer tüm komutlar: /etag, /stag, /gtag, /otag, /tag, /tektag, /burc, /admins, /duyuru, /test, /stats, /durum tamamen aynı kalıyor)

print(">> Bot çalışıyor <<")
client.run_until_disconnected()
