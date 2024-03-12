from pyrogram import Client,filters
from datetime import datetime

app = Client("@ZeusThon • Welcome",
api_id=29203867,
api_hash="cb13705fc054d5075a4f58027d7400f9",
bot_token="7074066484:AAG6fYQCv96hXmUo623xwm1Tprj4Ym5kaco")

@app.on_message(filters.new_chat_members)
async def welcome(_,message):
    id = message.from_user.id
    name= message.from_user.mention
    user = message.from_user.username
    now = datetime.now()
    now = (now.strftime('%I:%M'))
    await message.reply_text(f'''- يامرحباَ ، نورتنا يا كِيكَ 🔥♥· .    
   𖡋 𝐍𝐀𝐌𝐄 :- {name}
   𖡋 𝐔𝐒𝐄 :-  @{user}
   𖡋 𝐈𝐃 :- {id}
   𖡋 𝐄𝐍𝐓𝐑𝐘 :- {now}''')
print('تم تشغيل البوت ✅😂😂😂😜')
print(('==============================='))
app.run()