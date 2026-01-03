import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import random
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import date
from urllib.parse import quote
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(**name**)
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
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**💭 Sera Tag Bot** çalışıyor!\n Ben gruplarınızdaki tüm kullanıcılara etiket atmaya yarayan son derece basit kullanıma sahip bir botum. Komutlarımı görmek için /help yazabilirsiniz.\n\n Tamamen ücretsiz olarak hizmet vermekteyim. Gruplarınıza eklemekten çekinmeyiniz. ",
                    buttons=(
                     
                          [Button.url('➕ Beni Gruba Ekle ', f"https://t.me/{bot_username}?startgroup=a")],
                          [Button.url('Müzik Botu', f"https://t.me/seramusicbot")],
                  [Button.url('Teknik Destek', 'https://t.me/scrable')],
                  [Button.url('Tüm Diğer Botlar', 'https://t.me/serabotu')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    helptext = "**💭 Sera Tag Bot Komutlarına aşağıdan ulaşabilirsiniz.**\n\n**/start** - Botun göreve başlatılmasını sağlar\n**/tag** <Açıklama> - Tek mesajda yedi kişi olacak şekilde etiketler.\n**/etag** <Açıklama> - Emoji ile etiketler\n**/stag** - Kullanıcıları rastgele günaydın mesajı ile etiketler.\n**/gtag** - Kullanıcıları rastgele iyi geceler mesajı ile etiketler.\n**/otag** - Kullanıcılara güzel iltifatlar yaparak etiketler\n**/tektag** <Açıklama> - Üyeleri Tek Tek Etiketler\n**/admins** <Açıklama> - Gruptaki yöneticileri etiketler\n**/btag** - Bayrak Şeklinde Etiket Atar\n**/burc** Günlük Burç yorumu atar, tüm üyeler kullanabilir\n**/iptal** - Başlatılan etiketleme işlemini durdurur.\n\nAçıklama yazan kısımlara kullanıcılara söylemek istediğiniz metni yazabilirsiniz."
   
    await event.reply(helptext,
                      buttons=(
                          [Button.url('➕ Beni Gruba Ekle', f"https://t.me/{bot_username}?startgroup=a")],
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
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
 
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"❌**Etiket işlemi durduruldu.\n\n Etiketlerin Sayısı👤: {rxyzdev_tagTot[event.chat_id]}**")
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")
bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩 🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")
@client.on(events.NewMessage(pattern="^/btag([\s\S]*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli❗**")
 
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**❌ Üzgünüm, Bu komutu sadace yoneticiler kullanabilir.**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki mesajları etiket işlemi için kullanamıyorum.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiket Yapmak için <Açıklama> yok❗️")
  else:
    return await event.respond("**Etikete Başlamak için <Açıklama> yazın...!**")
 
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{random.choice(bayrak)} "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Etiket işlemi başarıyla durduruldu❌**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
@client.on(events.NewMessage(pattern='^(?i)/iptal'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
@client.on(events.NewMessage(pattern="^/etag([\s\S]*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗**")
 
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**❌ Üzgünüm, Bu komutu sadace yoneticiler kullanabilir.**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki mesajları etiket işlemi için kullanamıyorum.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Etiket yapmam için herhangi bir açıklama veya yazı yazmadınız❗️")
  else:
    return await event.respond("**Etikete başlamak için mesaj yazmalısın!**")
 
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{random.choice(emoji)} "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Etiket işlemi başarıyla durduruldu❌**")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
       
 
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{random.choice(emoji)} "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
@client.on(events.NewMessage(pattern="^/stag$"))
async def send_greetings(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**❌ Üzgünüm, Bu komutu sadece yöneticiler kullanabilir.**")
  greetings = [
    "Günaydın ya, hadi kalk güzel bir gün bizi bekliyor! ☕😊",
    "Günaydın canım benim, bugün de gülümseyerek başla güne 💕",
    "Günaydın dostlar, kahveler hazır mı? Harika bir gün olsun!",
    "Günaydın güzel insan, yüzünden gülücük eksik olmasın bugün 🌞",
    "Günaydın ya, uyanınca ilk seni düşündüm, hadi kalk ☀️",
    "Günaydın herkese, bugün de enerjimiz tavan yapsın! 🚀",
    "Günaydın arkadaşım, güzel şeyler olacak hissediyorum 😄",
    "Yeni güne merhaba! Kahveni içtin mi yoksa? ☕🌈",
    "Günaydın sevgili dostum, bugün sana bol şans getirsin!",
    "Günaydın canlarım, hepinize sımsıcak bir gün diliyorum 💖",
    "Günaydın ya, hadi kalk dünyayı güzelleştirelim bugün!",
    "Günaydın keyifli insan, sabahın en güzel hali sensin 😊",
    "Mutlu sabahlar! Bugün de harika olacağına eminim 🌟",
    "Günaydın, kahve kokusuyla uyananlar burda mı? ☕✨",
    "Günaydın ya, umarım güzel bir rüyadan uyanmışsındır!",
    "Günaydın herkese, bugün gülmek serbest, bol bol gülün 😄",
    "Günaydın dostum, hadi yeni maceralara yelken açalım!",
    "Günaydın, bugün sana güzel sürprizler hazırladım (hayat hazırladı aslında) 😉",
    "Günaydın ya, enerjin zaten yüksek, biraz daha yükseltelim mi?",
    "Günaydın arkadaşlar, yeni gün yeni umutlar getirsin 🌞",
    "Günaydın güzel kalpli insan, günün senin kadar güzel olsun!",
    "Günaydın ya, kalk kahvaltını yap, gün seni bekliyor ☕🍳",
    "Günaydın herkese, bugün de en güzel siz olun tamam mı? 😊",
    "Günaydın canım, hadi gülümse dünya seninle aydınlansın!",
    "Günaydın dostlar, kahve içip güne güçlü başlayalım mı?",
    "Günaydın ya, bugün harika şeyler yapacağız, hazır mısın?",
    "Günaydın sevgili arkadaşım, seni düşünerek uyandım 🌅",
    "Günaydın, güzel bir kahveyle güne enerji katalım hadi ☕",
    "Günaydın ya, uyanınca mesaj at diye bekliyordum 😄",
    "Günaydın herkese, bugün bol kahkaha borcu var hayatın!",
    "Günaydın güzel insan, sabahın en tatlı hali sensin 💕",
    "Günaydın dostum, hadi kalk dünyayı fethedelim bugün!",
    "Günaydın ya, güne gülerek başlamak en güzeli, hadi gülümse!",
    "Günaydın arkadaşlar, yeni gün size bol güzellik getirsin 🌈",
    "Günaydın canım benim, bugün de parlamaya devam et 🌟",
    "Günaydın ya, kahveni aldın mı? Gün başlasın o zaman ☕",
    "Günaydın herkese, bugün de mutlu olmaya kararlıyız değil mi?",
    "Günaydın sevgili dostlar, hepinize sıcacık bir gün diliyorum ☀️",
    "Günaydın ya, hadi kalk güzel haberler bizi bekliyor!",
    "Günaydın güzel insan, günün senin enerjinle dolsun 😊",
    "Günaydın dostlar, sabah sporu yapan var mı aramızda? 💪",
    "Günaydın ya, uyan ve dünyayı biraz daha güzelleştir bugün!",
    "Günaydın canlarım, hepinize mis gibi bir gün diliyorum 🌸",
    "Günaydın arkadaşım, bugün de harika olacağına eminim!",
    "Günaydın ya, kahvaltı ne bugün? Anlat da özendireyim 😄",
    "Günaydın herkese, güne pozitif başlayalım hadi!",
    "Günaydın sevgili insan, seni görmek güne değer katıyor 🌞",
    "Günaydın ya, hadi kalk yeni hikayeler yazalım bugün!",
    "Günaydın dostum, sabah mesajı benden, gülücük senden 😊",
    "Günaydın güzel kalpli arkadaşım, günün aydın olsun!",
    "Günaydın ya, bugün sana bol bol güzel şeyler olsun inşallah!",
    "Günaydın herkese, kahve molası verenler el kaldırsın ☕",
    "Günaydın canım, hadi güne enerjik bir giriş yapalım!",
    "Günaydın ya, uyanınca ilk işim sana günaydın demek oldu 🌅",
    "Günaydın arkadaşlar, bugün de en güzel anılar bizde olsun!",
    "Günaydın sevgili dostlar, sabahın en tatlı hali burda 😄",
    "Günaydın ya, kalk ve güne sahip çık bugün!",
    "Günaydın güzel insan, gülüşünle aydınlat etrafı hadi!",
    "Günaydın dostlar, yeni gün yeni şanslar getirsin 🌟",
    "Günaydın ya, kahveni iç de güne başlayalım birlikte ☕",
    "Günaydın herkese, bugün de mutlu olmaya niyetliyiz!",
    "Günaydın canım benim, günün en güzel yerinde ol 😊",
    "Günaydın ya, hadi kalk dünyayı biraz daha sevelim bugün!",
    "Günaydın arkadaşım, sabah mesajı benden sevgiler senden 💕",
    "Günaydın sevgili insan, günün harika geçsin inşallah!",
    "Günaydın ya, uyan ve mucizelere hazır ol bugün 🌈",
    "Günaydın dostum, kahvaltıda ne var söyle de iştahım açılsın 😄",
    "Günaydın herkese, güne gülerek başlayalım hadi!",
    "Günaydın güzel kalpli dostlar, hepinize bol neşe!",
    "Günaydın ya, bugün de senin günün olsun tamam mı?",
    "Günaydın canlarım, sabahın en enerjik hali sensin 🚀",
    "Günaydın arkadaşlar, hadi kalk güzel şeyler bizi bekliyor!",
    "Günaydın ya, güne senin enerjinle başlayalım ☀️",
    "Günaydın sevgili dostum, günün senin kadar güzel olsun!",
    "Günaydın herkese, kahve kokusu alan var mı? ☕✨",
    "Günaydın ya, hadi kalk ve günü güzelleştirelim birlikte!",
    "Günaydın güzel insan, sabahın en tatlı mesajı benden 😊",
    "Günaydın dostlar, yeni güne hoş geldiniz, harika olun!",
    "Günaydın ya, uyanınca gülümsedin mi? Gülümsemediysen şimdi gülümse!",
    "Günaydın canım, bugün de parlamaya devam et 🌟",
    "Günaydın arkadaşım, günün aydın, kalbin huzurlu olsun 💖",
    "Günaydın ya, kahveni aldın mı? Gün başlasın o zaman!",
    "Günaydın herkese, bugün bol kahkaha, bol mutluluk olsun!",
    "Günaydın sevgili insan, seni düşünerek güne başladım 🌅",
    "Günaydın ya, hadi kalk yeni başlangıçlar yapalım!",
    "Günaydın dostum, sabahın en güzel hediyesi sensin 😄",
    "Günaydın güzel kalpli arkadaşlar, gününüz mübarek olsun!",
    "Günaydın ya, bugün sana güzel şeyler getireceğine eminim gün!",
    "Günaydın canlarım, hepinize sımsıcak bir sabah diliyorum ☕",
    "Günaydın herkese, güne enerjik bir selam benden!",
    "Günaydın ya, kalk ve dünyayı biraz daha güzelleştir!",
    "Günaydın sevgili dostlar, bugün de harika şeyler yaşayalım!",
    "Günaydın güzel insan, gülüşünle başla güne hadi 😊",
    "Günaydın ya, kahvaltı masası hazır mı? Özendim şimdi ☕🍳",
    "Günaydın arkadaşlar, yeni gün size bol güzellik getirsin 🌸",
    "Günaydın dostum, sabah mesajı atmak en sevdiğim şey oldu!",
    "Günaydın ya, hadi kalk ve günü senin rengine boyayalım!",
    "Günaydın herkese, bugün de mutlu olmaya karar verdik mi?",
    "Günaydın canım benim, günün en güzel yerinde ol hep 💕",
    "Günaydın ya, uyan ve güne teşekkür et, harika olacak!",
    "Günaydın sevgili insan, sabahın en tatlı hali sensin 🌞",
    "Günaydın dostlar, kahve içip güne güçlü başlayalım mı? ☕",
    "Günaydın ya, bugün de en güzel sen ol, zaten hep öylesin!",
    "Günaydın arkadaşım, günün senin enerjinle dolsun 🚀",
    "Günaydın herkese, hadi gülümseyelim dünya güzelleşsin 😄",
    "Günaydın ya, kalk ve yeni hikayeler yazalım bugün!",
    "Günaydın güzel kalpli dostum, günün aydın olsun!",
    "Günaydın canlarım, sabahın en enerjik selamı benden!",
    "Günaydın ya, kahveni iç de güne merhaba diyelim birlikte ☕",
    "Günaydın sevgili arkadaşlar, bugün de harika olun!",
    "Günaydın dostum, uyanınca ilk seni düşündüm 😊",
    "Günaydın ya, hadi kalk güzel şeyler olacak bugün!",
    "Günaydın herkese, güne pozitif enerjiyle başlayalım 🌟",
    "Günaydın güzel insan, günün senin kadar aydınlık olsun!",
    "Günaydın ya, sabah mesajı benden, gülücük senden 💖",
    "Günaydın arkadaşlar, yeni güne hoş geldiniz, keyfini çıkarın!",
    "Günaydın canım, bugün de parlamaya devam et hadi 🌈",
    "Günaydın ya, kalk ve günü güzelleştirmeye başla!",
    "Günaydın sevgili dostlar, hepinize bol neşeli bir gün!",
    "Günaydın herkese, kahve kokusuyla uyananlar burada mı? ☕",
    "Günaydın ya, uyan ve mucizelere inanmaya devam et!",
    "Günaydın güzel kalpli insan, günün harika geçsin inşallah 😊",
    "Günaydın dostum, sabahın en tatlı mesajı sana!",
    "Günaydın ya, hadi kalk dünyayı biraz daha sevelim!",
    "Günaydın arkadaşlar, bugün de en güzel anılar bizim olsun!",
    "Günaydın canlarım, güne gülerek başlayalım hadi 🌞",
    "Günaydın ya, kahvaltıda ne var söyle de iştahım açılsın 😄",
    "Günaydın herkese, yeni gün yeni umutlar getirsin!",
    "Günaydın sevgili insan, seni düşünerek güne başladım yine 💕",
    "Günaydın ya, kalk ve günü senin rengine boya!",
    "Günaydın dostlar, sabahın en enerjik hali burada!",
    "Günaydın güzel insan, gülüşünle başla güne lütfen 😊",
    "Günaydın ya, bugün sana bol bol güzellik dilerim!",
    "Günaydın arkadaşım, günün aydın, kalbin mutlu olsun ☀️"
]
    anlik_calisan.append(event.chat_id)
    users = []
    async for user in client.iter_participants(event.chat_id):
        users.append(user)
   
    random.shuffle(users)
   
    usrnum = 0
    usrtxt = ""
    for user in users:
        usrnum += 1
        usrtxt += f"{user.first_name}, "
        if usrnum == 7:
            if event.chat_id not in anlik_calisan:
                await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
                return
            random_greeting = random.choice(greetings)
            await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    if usrnum > 0:
        if event.chat_id not in anlik_calisan:
            await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
            return
        random_greeting = random.choice(greetings)
        await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
def convert_to_ascii(text):
    conversions = {
        'ğ': 'g',
        'ü': 'u',
        'ş': 's',
        'ı': 'i',
        'ö': 'o',
        'ç': 'c',
        'Ğ': 'G',
        'Ü': 'U',
        'Ş': 'S',
        'İ': 'I',
        'Ö': 'O',
        'Ç': 'C'
    }
    for char, repl in conversions.items():
        text = text.replace(char, repl)
    return text
@client.on(events.NewMessage(pattern="^/burc$"))
async def ask_horoscope(event):
    burc_listesi = [
        "koç", "boğa", "ikizler", "yengeç", "aslan", "başak", "terazi", "akrep", "yay", "oğlak", "kova", "balık"
    ]
    burc_listesi_str = "\n".join(burc_listesi)
    await event.respond(
        "🏹 ** Burç yorumu nasıl kullanılır** : /burc kova şeklinde burcunuzu yazarak günlük burç yorumunuzu alabilirsiniz. Hergün 23.00'dan sonra günlük yorumunuz değişir.",
        reply_to=event
    )
@client.on(events.NewMessage(pattern="^/burc$"))
async def ask_horoscope(event):
    burc_listesi = [
        "koç", "boğa", "ikizler", "yengeç", "aslan", "başak", "terazi", "akrep", "yay", "oğlak", "kova", "balık"
    ]
    burc_listesi_str = "\n".join(burc_listesi)
    await event.respond(
        "🏹 **Burç yorumu nasıl kullanılır**: /burc kova şeklinde burcunuzu yazarak günlük burç yorumunuzu alabilirsiniz. Hergün 23.00'dan sonra günlük yorumunuz değişir.",
        reply_to=event
    )
@client.on(events.NewMessage(pattern="^/burc (.+)$"))
async def send_horoscope(event):
    burc = event.pattern_match.group(1).lower()
    burc_listesi = [
        "koç", "boğa", "ikizler", "yengeç", "aslan", "başak", "terazi", "akrep", "yay", "oğlak", "kova", "balık"
    ]
    if burc not in burc_listesi:
        burc_listesi_str = "\n".join(burc_listesi)
        await event.respond(
            f"**Üzgünüm, böyle bir burç bulunmamaktadır. Lütfen aşağıdaki burçlardan birini seçin:**\n{burc_listesi_str}",
            reply_to=event
        )
        return
    ascii_burc = convert_to_ascii(burc)
    burc_url = f"https://www.hurriyet.com.tr/mahmure/astroloji/{quote(ascii_burc)}-burcu/"
    response = requests.get(burc_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_element = soup.find("div", class_="horoscope-detail-tab-content")
        if horoscope_element:
            horoscope = horoscope_element.find_all("p")[1].text.strip() # İkinci <p> etiketinin içeriğini alıyoruz
            today = date.today()
            formatted_date = today.strftime("%d.%m.%Y")
            await event.respond(
                f"Sevgili {event.sender.first_name}, işte {burc.capitalize()} burcu yorumunuz:\n\n{horoscope}",
                reply_to=event.reply_to_msg_id
            )
        else:
            await event.respond(
                f"**Üzgünüm, {burc.capitalize()} burcu yorumunu bulurken bir hata oluştu.**",
                reply_to=event.reply_to_msg_id
            )
    else:
        await event.respond(
            f"**Üzgünüm, {burc.capitalize()} burcu yorumunu alırken bir hata oluştu.**",
            reply_to=event.reply_to_msg_id
        )
@client.on(events.NewMessage(pattern="^/otag$"))
async def send_greetings(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**❌ Üzgünüm, Bu komutu sadece yöneticiler kullanabilir.**")
  greetings = [
    "Her günün böyle güzel geçsin ya, yüzünden gülücük eksik olmasın!",
    "Gülüşün hiç solmasın, sen gülünce dünya güzelleşiyor resmen 😊",
    "İçindeki o güzel sevgiyi herkese saç, etrafın ışıl ışıl olsun!",
    "Başarıların daim olsun, hep zirvede kal inşallah!",
    "Bugünün harika insanlarla dolsun, güzel anılar biriktir bugün de!",
    "Sevdiklerinle bol bol vakit geçir, unutulmaz günler olsun!",
    "Hayallerinin peşinden koş, hepsi gerçek olacak eminim!",
    "Her gün biraz daha mutlu uyan, sen bunu hak ediyorsun ya 💖",
    "Kendini geliştir, sen zaten harikasın ama daha da parlayacaksın!",
    "Güzel insanlarla karşılaş, güzel anılar biriktir bugün!",
    "İyi niyetinle herkesi mutlu et, senin kalbin altın gibi çünkü 🌟",
    "Her sabah umutla uyan, yeni gün yeni heyecanlar getirsin!",
    "Huzurun, mutluluğun hiç eksik olmasın hayatından!",
    "Pozitif ol, enerjin zaten bulaşıcı, herkes kapıyor senden 😄",
    "Küçük şeylerden mutlu olmayı unutma, en güzeli onlar zaten!",
    "Kendini sev, olduğun gibi muhteşemsin sen!",
    "Başarıların katlanarak artsın, hep gurur duyacağız seninle!",
    "Sevdiklerinle sağlıklı, mutlu, bol kahkahalı günler geçirin!",
    "Günün sevgiyle dolsun, kalbin hep sıcacık kalsın 💕",
    "Hayatın hep güzelliklerle dolsun, senin gibi insanlara yakışır bu!",
    "Yeni şeyler dene, kendini keşfet, çok güzel yerlere geleceksin!",
    "Seni görmek beni çok mutlu ediyor biliyor musun? 😊",
    "Daha nice başarılar senin olsun, hep yanındayız!",
    "Her anın kıymetli olsun, güzelliklerle çevrilisin!",
    "Hayatını coşkuyla yaşa, neşeni hiç kaybetme!",
    "Etrafın hep iyi insanlarla dolsun, sen de onları hak ediyorsun!",
    "Her yeni güne minnetle başla, güzel şeyler gelecek emin ol 🌈",
    "O güzel kalbinle herkesi aydınlat, sen zaten ışığınsın!",
    "Bugün sana bol bol güzellik getirsin, senin günün harika olsun!",
    "Seni mutlu eden şeyleri yap, hayat kısa, keyfini çıkar!",
    "Gözlerin hep mutlulukla parlasın, gülüşün hiç eksilmesin!",
    "Senin gibi güzel insanlara hep güzel şeyler olsun ya!",
    "Bugün de gülümse bol bol, dünya senin enerjine ihtiyaç duyuyor 😄",
    "İçindeki gücü hisset, her şeyin üstesinden geleceksin!",
    "Hayat sana hep en güzel sürprizleri yapsın!",
    "Kendine iyi bak, sen çok değerlisin biliyor musun?",
    "Bugün birine güzel bir şey söyle, senin kalbin zaten dolu iyilikle 💖",
    "Her şey yoluna girecek, sen sadece gülümse yeter!",
    "Sevdiklerin hep yanında olsun, mutluluğun katlansın!",
    "Yeni bir şeyler öğren bugün, senin zekana bayılıyorum zaten 😊",
    "Kahkahan bol olsun, en güzel ses seninki!",
    "Hayallerine bir adım daha yaklaş, ben inanıyorum sana!",
    "Bugün kendin için bir şey yap, küçük de olsa mutlu etsin seni 🌟",
    "Etrafına pozitiflik saç, zaten doğalında var bu sende!",
    "Güzel bir gün geçirmen dileğiyle, hadi keyfini çıkar!",
    "Sen mutlu olunca ben de mutlu oluyorum, gülümse lütfen 😄",
    "Her şey daha güzel olacak, biraz sabır, hepsi senin olacak!",
    "Kalbin hep sevgiyle dolsun, sen sevgiyi hak ediyorsun!",
    "Bugün harika şeyler olacak, hissediyorum!",
    "Kendine güven, sen zaten muhteşemsin ya!",
    "Bol bol gül, hayat seninle güzel çünkü!",
    "Sevdiklerinle güzel vakitler geçir, anılar biriktir bugün de 💕",
    "İçindeki çocuğu mutlu et, biraz şımar bugün!",
    "Güzel haberler al diye dua ediyorum, olacak biliyorum!",
    "Senin enerjin yeter herkese, dağıt biraz etrafa 😊",
    "Hayat sana hep iyilikle dönsün, sen hep iyilik yapıyorsun çünkü!",
    "Bugün de parlamaya devam et, yıldız gibisin sen!",
    "Küçük mutlulukları fark et, en büyük zenginlik onlar!",
    "Her yeni gün sana yeni fırsatlar getirsin 🌈",
    "Gülüşünü eksik etme, en güzel aksesuarın o!",
    "Kendini sev, başkaları da seni daha çok sevecek!",
    "Bugün sana güzel şeyler layık, kabul et hepsini!",
    "İyi ki varsın, dünyam daha güzel seninle!",
    "Her şey gönlünce olsun, hep güzel şeyler yaşa!",
    "Senin gibi insanlara hep mutluluk yakışır ya 💖",
    "Bugün de harika ol, zaten hep öylesin!",
    "Kalbinin sesini dinle, en doğru yol o!",
    "Hayat sana bol bol kahkaha borçlu, bugün ödesin!",
    "Güzel kalbin hep kazansın, sen kazanıyorsun zaten!",
    "Yeni maceralara açık ol, çok güzel şeyler bekliyor seni!",
    "Bugün biraz kendine zaman ayır, sen de hak ediyorsun!",
    "Mutlu olman için dua ediyorum, hep mutlu ol inşallah 🌟",
    "Sen gülünce her şey güzelleşiyor, hadi gülümse!",
    "Hayatın hep sürprizlerle dolsun, güzel sürprizlerle tabii 😄",
    "Kendine iyi davran, en değerli sensin!",
    "Bugün de en güzel sen ol, zaten öylesin!",
    "Sevdiklerinle bol bol sarıl, en güzel ilaç o!",
    "İçindeki ışığı hiç söndürme, herkese lazım o ışık!",
    "Her şey daha iyi olacak, sen sadece inanmaya devam et!",
    "Bugün harika bir gün olacak, çünkü sen varsın!",
    "Güzel şeyler peşini bırakmasın hiç!",
    "Senin mutluluğun benim için çok önemli, gülümse lütfen 💕",
    "Hayat sana hep en iyisini versin, sen en iyisini hak ediyorsun!",
    "Bugün de kendine gurur duy, harikasın çünkü!",
    "Kahveni iç, gülümse, gün güzel olacak!",
    "Her zaman yanındayım, unutma bunu tamam mı? 😊",
    "Senin gibi güzel kalpli insanlara hep güzellikler olsun!",
    "Bugün biraz şımar, biraz eğlen, hayat kısa!",
    "İçin rahat olsun, her şey yoluna girecek!",
    "Güzel bir gün seni bekliyor, hadi çık karşıla!",
    "Sen mutlu ol, gerisi kendiliğinden gelir 🌈",
    "En güzel günler senin olsun, hep sen gül!",
    "Kendini takdir et, çok şey başarıyorsun farkında mısın?",
    "Bugün de dünyayı güzelleştirmeye devam et 😄",
    "Hayat sana bol bol sevgi versin, sen zaten sevgi dolusun!",
    "Gülüşünle aydınlat etrafını, en güzel ışık sensin!",
    "Her yeni gün sana yeni mutluluklar getirsin!",
    "Senin yerin hep en güzel yerde olsun ya 💖",
    "Bugün de harika şeyler yaşa, sen buna layıksın!",
    "İyi ki varsın, iyi ki seni tanıyorum!",
    "Mutlu ol, çünkü sen mutluluğu hak ediyorsun!",
    "Her şey senin istediğin gibi olsun, hep güzel olsun!",
    "Bugün gülümse, yarın daha çok gülersin 😊",
    "Kalbin hep huzurla dolsun, sen huzuru hak ediyorsun!",
    "Hayat sana hep en güzel renkleri göstersin 🌈",
    "Senin gibi insanlar çoğalsa dünya cennet olurdu!",
    "Bugün de kendine sarıl, seni çok seviyoruz!",
    "Güzel şeyler olacak, hissediyorum, hazır ol!",
    "Her zaman başarın daim olsun, sen zaten yıldızsın 🌟",
    "Bugün de en güzel sen ol, zaten hep öylesin!",
    "Hayatın hep sevgiyle, neşeyle dolsun!",
    "Gülümse, çünkü sen gülünce her şey güzel oluyor!"
]
    anlik_calisan.append(event.chat_id)
    users = []
    async for user in client.iter_participants(event.chat_id):
        users.append(user)
    random.shuffle(users)
    usrnum = 0
    usrtxt = ""
    for user in users:
        usrnum += 1
        usrtxt += f"{user.first_name}, "
        if usrnum == 7:
            if event.chat_id not in anlik_calisan:
                await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
                return
            random_greeting = random.choice(greetings)
            await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    if usrnum > 0:
        if event.chat_id not in anlik_calisan:
            await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
            return
        random_greeting = random.choice(greetings)
        await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
@client.on(events.NewMessage(pattern="^/tag([\s\S]*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
 
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**❌ Üzgünüm, Bu komutu sadace yoneticiler kullanabilir.**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki mesajları etiket işlemi için kullanamıyorum.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlatmak için <Açıklama> yok❗️")
  else:
    return await event.respond("Işleme başlamak için sebep yok")
 
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{usr.first_name}, "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
       
 
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{usr.first_name}, "
      if event.chat_id not in anlik_calisan:
        await event.respond("işlem başarıyla durduruldu❌")
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
@client.on(events.NewMessage(pattern='^(?i)/iptal'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
@client.on(events.NewMessage(pattern="^/gtag$"))
async def send_greetings(event):
    global anlik_calisan
    if event.is_private:
        return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("**❌ Üzgünüm, Bu komutu sadece yöneticiler kullanabilir.**")
  greetings = [
    "Zorlukları unut, derin nefes al uyu. İyi geceler! 🌟 🌙",
    "Yarın yeni bir gün, güzelce uyuyalım. İyi geceler! 💤💤",
    "Yıldızlar dans etsin sana, tatlı rüyalar 🌟🛌 🌌🌌",
    "Rüyalar alemine hoş geldin, iyi yolculuklar 😊 🛌🛌",
    "Sabaha tatlı uyu dostum! İyi geceler 🛌💤 🌌🌌",
    "Tatlı rüyalar, yarın görüşürüz inşallah! 🛌🛌",
    "Sabah daha güzel olacak, huzurla uyu ya 🌌✨ 🌠",
    "Seni seviyorum, iyi geceler canım benim. (arkadaşça tabii) 💤💤",
    "Uyu artık, gözlerin kapanıyor baksana 😊 İyi geceler. ✨✨",
    "Tatlı rüyalar gör, sabah gülerek uyan. 🌙🌙",
    "En güzel yerlere git rüyanda, tatlı uykular 🌙✨ 💫💫",
    "Gözlerini kapat, hayal kur. Huzurlu uykular. ✨",
    "Hadi kapanış yapalım günü, iyi uykular. ✨",
    "Rüyanda beni görürsen selam söyle 😜 Tatlı rüyalar. 🌟",
    "Sabaha kadar mutluluk sarsın seni, iyi uykular 🌙💖 🌠",
    "Güzel bir gece geçirmen dileğiyle, iyi uykular. 🌟🌟",
    "Kötü geçtiyse bile gece düzeltir, tatlı uykular 🌌💤 💫💫",
    "Gece huzurla dolsun, sabah neşeyle uyan dostum 🌙💫 🛌🛌",
    "Geceyi kucakla, mutlu uyu. İyi geceler! 💫💖 🌌🌌",
    "Sabah kahvaltıda görüşürüz belki, iyi geceler! 🌌",
    "Tatlı rüyalar, yarın anlatırsın ne gördün. 🌙🌙",
    "Stres bitti, dinlen artık! İyi geceler 💤✨ ✨",
    "Gece sarmalasın seni huzurla, tatlı rüyalar 🌟✨ 💫💫",
    "Rüyanda en sevdiğin şeyi yaşa, tatlı rüyalar. 💫💫",
    "Sabah mesaj atarsın uyanınca, iyi geceler ya. 🌟",
    "Rüyalarımda seni görürsem haber veririm 😄 İyi geceler. 🌌",
    "Yarın yeni macera, iyi geceler güzel rüyalar 💫 💤",
    "Huzurlu bir gece olsun, bugün bayağı çalıştın dinlen artık 🌌 💖💖",
    "Rüyanda başrol sensin, güzel uyu 🌠💤 💖💖",
    "Gece masal gibi olsun sana, tatlı rüyalar 🌟🛌",
    "Uyu artık, çok konuştuk bugün 😄 İyi geceler. 💖",
    "İyi geceler ya, tüm yorgunluğu at üstünden, güzel uyu 🌙 🌠🌠",
    "Sen kahraman ol rüyanda, huzurlu geceler 🌟💤 🛌🛌",
    "Yoruldun, yastığa sarıl uyu ya 🛌💫 💫",
    "En sevdiğin rüyayı gör bu gece, iyi geceler dostum. 💫",
    "Bugün de bitti şükür, şimdi uyku zamanı. İyi geceler! 🌟",
    "Rahat uyku seni bekliyor, kapat gözleri 🛌💤 ✨",
    "Yıldızlara bak hayal kur, huzurlu uykular 🌌🌟",
    "Huzurla dol, umutla uyan. Tatlı rüyalar 🌟💖 🛌🛌",
    "Yarın için hazır ol, güzel dinlen. İyi geceler. 💤💤",
    "Gözlerim kapanıyor, sen de uyu artık. İyi uykular. 🌙",
    "Sevdiklerin rüyanda olsun, iyi geceler 🌙💖",
    "Bu gece yıldızlar sana baksın, huzurla uyu ya 🌟🌙 💖💖",
    "Gece güzel rüyalarla dolsun, tatlı uykular. 🛌🛌",
    "Seni düşünerek uyuyorum ben de, tatlı rüyalar sana. 🌟🌟",
    "Huzur dolu bir gece olsun sana, sevgiler. 💤",
    "İyi geceler ya, bugün bayağı yoruldun değil mi? Hadi güzelce dinlen. 💖💖",
    "Sevdiğin anıya dal, huzurlu uykular 🌠✨ 🛌",
    "Yepyeni umutla uyan diye tatlı rüyalar 🌙💤 🌌🌌",
    "Geceyi kucakla, huzurla dol. İyi geceler dostum. 🛌",
    "Gecenin huzuru sarsın seni ya, dinlen 🌌💖 ✨",
    "Geceyi armağan gibi al, huzurla dinlen 🌟💫 🌠",
    "Gece boyunca mutlu ol, rüyaların tatlı olsun. 🌌🌌",
    "Bugünü bitirdin helal, şimdi uyku zamanı. İyi geceler! 💤",
    "Her şey yoluna girer, uyu rahatça. İyi geceler. 💤💤",
    "Hadi uyu, geç oldu. Tatlı rüyalar sevgili arkadaşım. 💫",
    "Taptaze uyan diye tatlı rüyalar 🌠✨ 💤",
    "Kapat ışığı, uyu artık şımarık 😄 İyi geceler. ✨",
    "Yıldızlar seni izliyor, güzel uyu. 💫💫",
    "Yıldızlarla dans et rüyanda, iyi geceler 🌟💖 🌌",
    "Dinlenmeye ihtiyacın var, hadi iyi uykular. 🌠🌠",
    "Gece güzel olsun, sabah enerjik uyanalım. İyi geceler. 🌙🌙",
    "Sabaha kadar huzurlu uyu dostum 🌠💫 🌟🌟",
    "Hayal kur bol bol, iyi geceler! 🌠💤 🌙🌙",
    "Huzur seninle olsun bu gece, iyi uykular. 🌌",
    "Yarın daha güzel olacak, inan. Huzurlu geceler. 💤💤",
    "Gece sessiz olsun, güzel dinlen. Tatlı rüyalar sana. 💤",
    "Bugün konuşmak güzeldi, yarın devam ederiz. İyi uykular. 🛌🛌",
    "Harikaydın bugün, dinlen yarına hazır ol 🌌💫 🌟🌟",
    "Rüyanda güzel anılarla takıl, huzurlu uykular 🌠 🛌🛌",
    "Her şey yoluna girer diye güzel uyu. İyi geceler! 🌌💤 💫💫",
    "Gözlerini kapat, hayallere dal! İyi geceler sana 🌠 🌙🌙",
    "Huzurla dolup taşsın gecen, tatlı rüyalar. 💖💖",
    "Yastığa başını koyar koymaz uyursun umarım, iyi uykular canım. 🌠🌠",
    "Kapat gözlerini, her şey güzel olacak yarın. Huzurlu uykular. 💖",
    "Rüyanda mutluluklar gör dostum, tatlı rüyalar 🌙🌠 💖",
    "Sakin gece olsun ya, iyi uykular 🌙✨ 🌙🌙",
    "Rahatça uyu, sabah her şey daha iyi olacak dostum 🛌 🛌🛌",
    "Tatlı rüyalar, hadi rüyalarda görüşelim 😊 💤 🛌🛌",
    "Enerjini topla yarına, iyi uyku geçir 🌌🛌 💫",
    "Rüyanda uçmayı falan dene, eğlenceli olur 😊 İyi geceler. 💖",
    "Tüm güzel düşünceler seninle, tatlı rüyalar 🛌 🌠",
    "Sevdiklerinle ilgili güzel rüyalar gör, iyi uykular. 🛌🛌",
    "Uyu derin derin, yarına enerji lazım. 🛌",
    "Rüyanda güzel şeyler gör, stres falan olmasın hiç. 💫",
    "Bugün de geçti, şükür. İyi geceler ya. 💖💖",
    "Karanlık dinginlik versin, rahat uyu. İyi geceler! 🌌✨ 💫💫",
    "Mutlu yerlere git rüyanda, iyi geceler 🌠🛌 🌌🌌",
    "Bugünün tüm kötülüğünü geride bırak, güzel uyu. 💫",
    "Huzur içinde uyu, her şey güzel olsun. 🌟🌟",
    "Yıldızlar rehber olsun, güzel rüyalar gör. İyi geceler! 🌟✨ 🌌",
    "Bu gece sadece senin huzurun için, iyi uykular ya 🌌💖",
    "Yastık yumuşacık olsun, uyku derin. İyi geceler. 🌌🌌",
    "Bugün yoruldum ben de, birlikte uyuyalım uzaklardan. İyi geceler. 💖💖",
    "Mutluluğunu kur bu gece, tatlı rüyalar 🌙💤 🌌🌌",
    "Yoruldun bugün, hadi dinlen artık. Tatlı rüyalar. 💤💤",
    "Çok çalıştın, huzur içinde dinlen ya 🌌💖 🛌",
    "Gece seni sarsın huzurla, iyi uykular ya. 💫",
    "Sabaha enerji patlaması yapasın diye güzel uyu 🌙✨"
]
    anlik_calisan.append(event.chat_id)
    users = []
    async for user in client.iter_participants(event.chat_id):
        users.append(user)
    random.shuffle(users)
    usrnum = 0
    usrtxt = ""
    for user in users:
        usrnum += 1
        usrtxt += f"{user.first_name}, "
        if usrnum == 7:
            if event.chat_id not in anlik_calisan:
                await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
                return
            random_greeting = random.choice(greetings)
            await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    if usrnum > 0:
        if event.chat_id not in anlik_calisan:
            await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
            return
        random_greeting = random.choice(greetings)
        await client.send_message(event.chat_id, f"{random_greeting}\n\n{usrtxt}")
@client.on(events.NewMessage(pattern="^/tektag([\s\S]*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar ve kanallar için geçerlidir❗️**")
 
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**❌ Üzgünüm, Bu komutu sadace yoneticiler kullanabilir.**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki mesajları etiket işlemi için kullanamıyorum.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamak için mesaj yazmalısın❗️")
  else:
    return await event.respond("**İşleme başlamam için mesaj yazmalısın**")
 
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**{usr.first_name}, **"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
       
 
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"{usr.first_name}, "
      if event.chat_id not in tekli_calisan:
        await event.respond("**Etiketleme İşlemi Başarıyla Durduruldu**❌")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
@client.on(events.NewMessage(pattern='^(?i)/iptal'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
@client.on(events.NewMessage(pattern="^/duyuru([\s\S]*)"))
async def duyuru(event):
    if event.is_private:
        user_id = event.sender_id
        if str(user_id) != owner and str(user_id) != "1449935113":
            return await event.reply("**❌ Bu komut sadece bot sahibi tarafından kullanılabilir.**")
       
        message = event.pattern_match.group(1)
        if not message:
            return await event.reply("**Duyuru mesajını belirtmelisiniz.**")
       
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                chat_id = dialog.id
                try:
                    await client.send_message(chat_id, message)
                except Exception as e:
                    LOGGER.warning(f"Hata: {str(e)}")
       
        await event.reply("**✅ Duyuru gönderildi!**")
    else:
        await event.reply("**❌ Bu komut sadece özel mesajlarda kullanılabilir.**")
@client.on(events.NewMessage(pattern="^/admins([\s\S]*)"))
async def mentionall(tagadmin):
if tagadmin.pattern_match.group(1):
seasons = tagadmin.pattern_match.group(1)
else:
seasons = ""
chat = await tagadmin.get_input_chat()
a_=0
await tagadmin.delete()
async for i in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
if a_ == 500:
break
a_+=5
await tagadmin.client.send_message(tagadmin.chat_id, "**{} {}**".format(i.first_name, i.id, seasons))
sleep(0.5)
@client.on(events.NewMessage(pattern='/test'))
async def handler(event):
    # Alive Bot Durumunu Kontrol Etme Yalnızca Adminler İçin !
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("**Sen sahibim değilsin !**")
    await event.reply('**Hey Bot Çalışıyor!** \n Teknik destek @Scrable')
grup_sayi = []
grup_isimleri = [] # Grup isimlerini saklamak için bir liste tanımlanır
@client.on(events.NewMessage(pattern='^/stats'))
async def son_durum(event):
    # Bot Stats
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("**Hey!** \n **Sen botun sahibi değilsin. Botun İstatiklerini Öğrenemezsin.!**")
    global anlik_calisan, grup_sayi, grup_isimleri, ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
        return
    grup_isimleri_str = "\n".join(grup_isimleri) # Grup isimlerini birleştirerek bir metin oluşturulur
    await event.respond(f"**{bot_username} İstatistikleri 🤖**\n\nToplam Grup: {len(grup_sayi)}\nAnlık Çalışan Grup: {len(anlik_calisan)}\n\nGrup İsimleri:\n{grup_isimleri_str}")
# Grup sayısı ve isimlerini güncelleme örneği:
async def bir_grup_eklendi():
    global grup_sayi, grup_isimleri
    # Grup eklenirken grup_sayi listesine eklenmeli
    # ve grup_isimleri listesine grup ismi eklenmeli
    grup_sayi.append(grup) # 'grup' değişkeni, eklenen grubun bilgisini içermelidir
    grup_isimleri.append(grup_ismi) # 'grup_ismi' değişkeni, eklenen grubun ismini içermelidir
    # Diğer işlemler...
@client.on(events.NewMessage(pattern='/durum'))
async def handler(event):
    await event.reply('**Tagger Bot un Durum Menüsü** \n\n **Durum:** Çalışıyor✅ \n\n **Telethon Sürümü:** **v1.24.0** \n\n**Python Sürümü:** **v3.10** \n\n **Bot Sürümü:** **v1.2** \n\n **** Daha fazla bilgi için @scrable **dir**')
print(">> Bot çalıyor 🚀 <<")
client.run_until_disconnected()
