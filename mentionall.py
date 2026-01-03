import random
import os
import logging
import asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    InputStickerSetShortName
)
from telethon.tl.functions.stickers import CreateStickerSetRequest, AddStickerToSetRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetItem
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
owner = 1449935113
SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []
tekli_calisan = []
ozel_list = [1449935113]
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

# Sticker pack adı (benzersiz olsun diye bot username'i ekledik)
STICKER_PACK_NAME = f"sera_sticker_by_{bot_username.replace('@', '').lower()}"

# Diğer tüm komutlar (start, help, tag, etag, stag, gtag, otag, tektag, burc, admins, duyuru vs.) 
# tamamen aynı kalıyor, sadece /sticker güncellendi

@client.on(events.NewMessage(pattern="^/sticker$"))
async def sticker_command(event):
    if event.is_private:
        return await event.reply("**Bu komut sadece gruplarda ve kanallarda kullanılabilir.**")

    if not event.is_reply:
        return await event.reply("**Lütfen bir görsele alıntı yaparak /sticker yazın.**")

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.media:
        return await event.reply("**Alıntılanan mesajda görsel bulunamadı.**")

    processing = await event.reply("**Çıkartma oluşturuluyor, lütfen bekleyin...** ✨")

    try:
        # Görseli indir ve upload et
        file_bytes = await client.download_media(reply_msg.media, bytes)
        uploaded_file = await client.upload_file(file_bytes)

        me = await client.get_me()

        added = False
        try:
            # Önce pack'e eklemeyi dene
            await client(AddStickerToSetRequest(
                stickerset=InputStickerSetShortName(short_name=STICKER_PACK_NAME),
                sticker=InputStickerSetItem(
                    document=uploaded_file,
                    emoji="✨"
                )
            ))
            added = True
        except Exception as e:
            if "STICKERSET_INVALID" in str(e):
                # Pack yoksa oluştur
                await client(CreateStickerSetRequest(
                    user_id=me.id,
                    title="Sera Bot Çıkartmaları",
                    short_name=STICKER_PACK_NAME,
                    stickers=[
                        InputStickerSetItem(
                            document=uploaded_file,
                            emoji="✨"
                        )
                    ]
                ))
                added = True
            else:
                raise e

        if added:
            # Pack'ten son sticker'ı al ve gönder
            sticker_set = await client(GetStickerSetRequest(
                stickerset=InputStickerSetShortName(short_name=STICKER_PACK_NAME),
                hash=0
            ))
            last_sticker = sticker_set.documents[-1]
            await client.send_file(event.chat_id, last_sticker)

        await processing.delete()
        await event.delete()

    except Exception as e:
        error_msg = str(e)
        if "STICKERSET_INVALID" in error_msg:
            await processing.edit("**Sticker pack geçici bir sorun nedeniyle eklenemedi. Birkaç saniye sonra tekrar deneyin.**")
        elif "SHORT_NAME_OCCUPIED" in error_msg:
            await processing.edit("**Bu pack adı zaten alınmış. Bot sahibine bildirin.**")
        else:
            await processing.edit(f"**Çıkartma oluşturulurken hata:**\n`{error_msg}`")
        LOGGER.error(f"Sticker hatası: {e}")

# Kalan tüm kod (tag komutları, burç, admin vs.) tamamen aynı...

print(">> Bot çalışıyor 🚀 <<")
client.run_until_disconnected()
