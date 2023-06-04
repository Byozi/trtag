import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import random

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
    helptext = "**💭 Sera Tag Bot Komutlarına aşağıdan ulaşabilirsiniz.**\n\n**/start** - Botun göreve başlatılmasını sağlar\n**/tag** <Açıklama> - Tek mesajda yedi kişi olacak şekilde etiketler.\n**/etag** <Açıklama> - Emoji ile etiketler\n**/tektag** <Açıklama> - Üyeleri Tek Tek Etiketler\n**/admins** <Açıklama> - Gruptaki yöneticileri etiketler\n**/btag** - Bayrak Şeklinde Etiket Atar\n**/iptal** - Başlatılan etiketleme işlemini durdurur.\n\nAçıklama yazan kısımlara kullanıcılara söylemek istediğiniz metni yazabilirsiniz."
    
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

bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩  🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")

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
    return await event.respond("Etiket Yapmak için  <Açıklama>  yok❗️")
  else:
    return await event.respond("**Etikete Başlamak için  <Açıklama>  yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
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
        "Günaydın!",
        "İyi sabahlar!",
        "Herkese merhaba!",
        "Günaydın dostlar!",
        "Harika bir gün olsun!",
        "Günaydın herkese!",
        "Günaydın arkadaşlar!",
        "Yeni bir güne merhaba!",
        "Günaydın sevgili dostlar!",
        "Günaydın canlarım!",
        "Günaydın herkese enerjik bir gün diliyorum!",
        "Günaydın keyifli insanlar!",
        "Mutlu sabahlar!",
        "Günaydın, bugün harika şeyler yapacağız!",
        "Günaydın, umarım harika bir gün geçirirsiniz!",
        "Günaydın, bugün sizi gülümsetecek bir şeyler yapın!",
        "Yeni bir güne başlarken herkese mutluluklar dilerim!",
        "Günaydın, hayatınıza güzellikler dolsun!",
        "Günaydın, enerjik bir gün geçirmenizi dilerim!",
        "Yeni bir güne uyanırken enerjik hissediyorum!",
        "Günaydın, gününüz huzurlu ve neşeli geçsin!",
        "Yepyeni bir güne merhaba! Bugün harika şeyler yapacağız!",
        "Günaydın, güzel bir gün geçirmeniz dileğiyle!",
        "Günaydın, bugün size bolca şans getirsin!",
        "Umarım gününüz harika başlar!",
        "Günaydın dostlar, harika bir gün sizi bekliyor!",
        "Yeni bir güne enerjik başlamak için harika bir gün!",
        "Günaydın, bugün güzelliklerle dolu olsun!",
        "Günaydın, güzel bir kahveyle gününüze enerji katın!",
        "Yeni bir güne uyanırken sizi düşünerek günaydın demek istedim!"
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
        usrtxt += f"[{user.first_name}](tg://user?id={user.id}), "
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
    return await event.respond("Başlatmak için  <Açıklama>  yok❗️")
  else:
    return await event.respond("Işleme başlamak için sebep yok")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
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
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
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
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}), **"
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
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),  "
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
        
        for chat_id in grup_sayi:
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
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)
	
@client.on(events.NewMessage(pattern='/test'))
async def handler(event):
    # Alive Bot Durumunu Kontrol Etme Yalnızca Adminler İçin !
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sen sahibim değilsin !__")
    await event.reply('**Hey Bot Çalışıyor!** \n Teknik destek @Scrable')
	
@client.on(events.NewMessage(pattern='^/stats'))
async def son_durum(event):
    # Bot Stats 
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("**Hey!** \n __Sen botun sahibi değilsin. Botun İstatiklerini Öğrenemezsin.!__")
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**{bot_username} İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern='/durum'))
async def handler(event):
	
    await event.reply('**Tagger Bot un Durum Menüsü** \n\n __Durum:__ `Çalışıyor✅` \n\n **Telethon Sürümü:** __v1.24.0__ \n\n**Python Sürümü:** __v3.10__ \n\n **Bot Sürümü:** __v1.2__ \n\n **** Daha fazla bilgi için @scrable **dir**')




print(">> Bot çalıyor 🚀 <<")
client.run_until_disconnected()
