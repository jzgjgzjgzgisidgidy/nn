import os
import json
import asyncio
import time
from os import system, path
from time import sleep
from random import choice
from base64 import b64decode
import aiohttp
from bs4 import BeautifulSoup as S
from fake_useragent import UserAgent
from datetime import datetime
from telethon import TelegramClient, functions, errors, events
from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import CreateChannelRequest, UpdateUsernameRequest as UpdateChannelUsername, DeleteChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
import random

# --- إعدادات أساسية ---
api_id = '21348817'
api_hash = '545f481d612470ada5416f4f8b267c69'
session_string = '1ApWapzMBuxSJvaszaaz-MJmBDz9bt-fsiUSYIbIoCInkNVqNRJhLwo0dMtpQmK51eS9m41cdOlYQMHk2ZaGIycdEXiTMx_ZbeJy6wfFyvKAi521ghqXFle8vkGEuQueiOL1F2EPO91mfzMhh6_ktfyDh6W6hhO4wjYjP0C6LCHVBFH0FzsJGx9k-wKSd15ooE6wfGZNUCC6s8Tup4Fo-9KOvxx3kwBrA3AwHjZok2Eaw7Yr5c-t-ctEP7EJsdLhU9xTGFe32dLjkv0TtKgq6Hd5ax8EIfgWOxc_HHWvHrMjU6DJgLK08waOk55LiVfYVmDna8SxRdY6RY9UJ6XvRP7Hx3c3xSfU='
me = "@M_R_Q_P"
my_id = 7937540559 # ضع معرف حسابك الرقمي هنا للتحكم بالبوت

# --- متغيرات حالة البوت والإحصائيات ---
bot_running = True
users_checked = 0
users_claimed = 0
start_time = time.time()

# --- إعدادات المجلدات والملفات ---
data_dir = 'save/'
banned_file = os.path.join(data_dir, 'banned4.txt')
flood_file = os.path.join(data_dir, 'flood.txt')
claimed_file = os.path.join(data_dir, 'claimed.txt')

def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            print(f"Error creating directory {folder_path}: {e}")

check_and_create_folder(data_dir)
for file_path in [banned_file, flood_file, claimed_file]:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass

# --- تعريف الألوان ---
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'

# --- دوال مساعدة ---
async def fragment(username):
    headers = {'user-agent': UserAgent().random}
    url = f'https://fragment.com/username/{username}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                content = await response.text()
                soup = S(content, 'html.parser')
                ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name" in ok:
                    return True
                elif "is taken" in ok:
                    return "is taken"
                else:
                    return False
    except Exception:
        return "error"

def usernameG():
    # ... (نفس دالة توليد اليوزرات لم يتم تغييرها)
    y = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    b = ''.join(choice('1234567890') for i in range(1))
    z = ''.join(choice('1234567890') for i in range(1))
    o = ''.join(choice('1234567890') for i in range(1))
    k = ''.join(choice('1234567890') for i in range(1))
    j = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    w = ''.join(choice('qwertyuipoasdfghjklzxcvbnm') for i in range(1))
    v = ''.join(choice('v') for i in range(1))
    i = ''.join(choice('i') for i in range(1))
    p = ''.join(choice('p') for i in range(1))
    
    v1 = y+j+y+j+y
    v2 = v+i+p+y+w
    v3 = v+i+p+w+w+w
    v4 = y+j+j+j+w
    v5 = y+j+j+j+j+j+j
    v6 = y+w+j+j+j
    v7 = y+y+y+j+j
    v8 = y+y+'_'+j+y
    v9 = y+y+'_'+j+y
    v10 = j+j+w+'_'+j
    v11 = y+ '_'+w+w+y
    v12 = w+'_'+y+w+y
    v13 = y+j+y+'_'+j
    v14 = y+y+j+j+j+j
    v15 = y+j+j+y+j
    v16 = y+'_'+w+w+y
    v17 = w+'_'+w+y+w
    v18 = y+w+y+w+w
    v38 = j+j+y+y+j+y
    v39 = j+w+w+w+y
    v40 = w+w+w+'_'+w+w+w
    v41 = w+w+'_'+w+w+w+w
    v42 = w+'_'+w+w+w+w+w
    v43 = y+w+w+w+w+w+w
    v44 = w+w+w+w+'_'+w+w
    v45 = w+w+w+w+w+'_'+w
    v46 = w+w+w+w+w+w+y
    v47 = w+'_'+w+w+w+w+w+w
    v48 = w+w+'_'+w+w+w+w+w
    v49 = w+w+w+'_'+w+w+w+w
    v50 = w+w+w+w+'_'+w+w+w
    v51 = w+w+w+w+w+'_'+w+w
    v52 = w+w+w+w+w+w+'_'+w
    v53 = w+w+w+w+w+w+w+y
    v54 = j+y+y+y+j+y
    v55 = w+w+j+j+w+j
    v56 = w+y+w+y+w+w
    v57 = y+j+j+j+j
    v58 = y+y+y+j+y
    v59 = w+w+w+j+w+w+w+w
    v60 = y+'_'+j+j+y
    v61 = y+j+j+'_'+y
    v62 = y+j+j+j+y+y
    v63 = y+j+j+j+y
    v64 = y+j+j+y+y+y+y
    v65 = y+y+w+y+w+y
    v66 = w+y+y+y+y+w
    v67 = y+y+y+y+w+w
    v68 = y+w+y+y+w+y
    v70 = w+y+y+y+y+y+w
    v72 = y+y+j+y+j+y+y
    v73 = y+'_'+j+'_'+w
    v74 = y+y+j+j+w
    v75 = y+y+j+j+j+j+y
    v76 = y+j+y+y+j+y+y
    v77 = y+y+y+y+j+j+j
    v78 = y+b+y+y+y+y+b
    v79 = y+j+y+y+y+y+j
    v80 = y+y+b+j+j
    v81 = 'vip'+b+z+o
    v82 = 'vip'+b+'_'+z
    v83 = y+y+w+j+j
    v84 = y+b+y+'_'+y
    v85 = 'vip'+b+z+o+k
    v86 = 'vip'+b+b+o+z
    v88 = 'vip'+b+b+o
    v89 = y+j+y+j+'bot'
    
    ls = (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59,v60,v61,v62,v63,v64,v65,v66,v67,v68,v70,v72,v73,v74,v75,v76,v77,v78,v79,v80,v81,v82,v83,v84,v85,v86,v88,v89)
    return y+y+b+j+j

# --- دوال أساسية للفحص والصيد ---
async def climed(client, username):
    global users_claimed
    try:
        # إنشاء قناة مؤقتة
        result = await client(CreateChannelRequest(
            title=f'{username}',
            about=f'OWNER – {me}',
            megagroup=False))
        
        channel = result.chats[0]
        await client(UpdateChannelUsername(channel=channel, username=username))
        
        users_claimed += 1
        with open(claimed_file, "a") as f:
            f.write(username + '\n')
            
        yyj = [88, 50006, 89, 100, 80, 90, 63, 98, 507, 807, 597, 10, 20, 30, 40, 50, 60]
        trys = random.choice(yyj)
        
        caption_text = f'''** 
✅ DONE USER ⚡
- - - - - - - - - - - - - - - - - - - - - - - - - 
- UserName : ❲ @{username} ❳
- ClickS : ❲ {trys} ❳
- Data : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- - - - - - - - - - - - - - - - - - - - - - - - 
ThE Programmer ❲ {me} ❳**'''
        
        # إرسال رسالة إلى القناة الجديدة ثم حذفها
        await client.send_message(username, caption_text)
        await client(DeleteChannelRequest(channel=channel))
        
        # إرسال إشعار لنفسك
        await client.send_message('me', f"🎣 **New Catch!** \n@{username}")
        
        return True
    except Exception as e:
        print(f"{Z}Error in climed for @{username}: {e}")
        # إذا فشل الصيد، أرسل إشعارًا لنفسك باليوزر المتاح
        await client.send_message('me', f"⚠️ **Available but failed to claim:** \n@{username}\nReason: {e}")
        return False

async def checker(client, username):
    global users_checked
    users_checked += 1
    try:
        check = await client(CheckUsernameRequest(username=username))
        if check:
            print(f'{F}USER AVAILABLE  :  @{username}')
            # قبل محاولة الصيد، تحقق من fragment.com
            frag_status = await fragment(username)
            if frag_status is True:
                print(f'{X}Fragment says available, attempting to claim @{username}')
                await climed(client, username)
            else:
                print(f'{Z}Fragment says NOT available for @{username}: {frag_status}')
        else:
            print(f"{Z}USER taken : @{username}")
            
    except errors.rpcbaseerrors.BadRequestError:
        print(f'{Z}USER Fragment : @{username}')
        with open(banned_file, "a") as f:
            f.write(username + '\n')
    except errors.FloodWaitError as timer:
        print(f'{Z} Flood wait time – {timer.seconds} seconds')
        await asyncio.sleep(timer.seconds + 5) # إضافة 5 ثواني احتياط
    except errors.UsernameInvalidError:
        print(f'{Z}USER INVALID : @{username}')
    except Exception as e:
        print(f"{Z}Checker error for @{username}: {e}")

# --- حلقة الفحص الرئيسية ---
async def mortada_hunter(client):
    while True:
        if bot_running:
            tasks = []
            # قراءة ملف المحظورين مرة واحدة لكل دفعة
            with open(banned_file, 'r') as file:
                banned_list = file.read().splitlines()
            
            for _ in range(10): # زيادة عدد المهام المتزامنة
                username = usernameG()
                if username in banned_list:
                    print(f'{X}SKIPPING BANNED: @{username}')
                    continue
                tasks.append(checker(client, username))
            
            await asyncio.gather(*tasks)
            await asyncio.sleep(1) # فترة راحة قصيرة بين الدفعات
        else:
            await asyncio.sleep(5) # انتظر 5 ثوانٍ إذا كان البوت متوقفًا

# --- معالج الأوامر ---
async def setup_bot():
    client = TelegramClient(StringSession(session_string), int(api_id), api_hash)
    await client.start()
    print("✅ Login success, Bot is running...")
    
    try:
        await client(functions.channels.JoinChannelRequest("mortada"))
    except Exception:
        pass

    @client.on(events.NewMessage(from_users=my_id, pattern=r'^\.(.*)'))
    async def handler(event):
        global bot_running
        command = event.pattern_match.group(1).lower()

        if command == "فحص":
            ping_start = time.time()
            msg = await event.reply('`جاري الفحص...`')
            ping_end = time.time()
            ping_duration = round((ping_end - ping_start) * 1000, 2)
            status = "يعمل ✅" if bot_running else "متوقف ❌"
            await msg.edit(f"**💡 حالة البوت: {status}\n**⏱ سرعة الاستجابة (Ping): `{ping_duration}ms`")

        elif command == "الاحصائيات":
            uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
            speed = round(users_checked / (time.time() - start_time), 2) if (time.time() - start_time) > 0 else 0
            
            stats_msg = (
                f"**📊 إحصائيات الأداء:**\n\n"
                f"**⏳ مدة التشغيل:** `{uptime}`\n"
                f"**✔️ اليوزرات المفحوصة:** `{users_checked}`\n"
                f"**🎣 اليوزرات المصادة:** `{users_claimed}`\n"
                f"**⚡️ سرعة الفحص:** `{speed} يوزر/ثانية`"
            )
            await event.reply(stats_msg)

        elif command in ["الاوامر", "المساعدة"]:
            help_text = """
            

            `.فحص` - عرض حالة البوت الأساسية
            `.الاحصائيات` - إحصائيات مفصلة عن الأداء
            `.اليوزرات` - عرض آخر 5 يوزرات مصادة
            `.تصفية` - إحصائيات اليوزرات المحظورة
            `.المجلد` - عرض موقع مجلد الحفظ
            `.ايقاف` - إيقاف البوت مؤقتاً
            `.تشغيل` - تشغيل البوت
            `.المساعدة` - عرض هذه الرسالة

**DEV – @M_R_Q_P**
            """
            await event.reply(help_text)

        elif command == "اليوزرات":
            try:
                with open(claimed_file, 'r') as f:
                    lines = f.readlines()
                    last_five = lines[-5:]
                if last_five:
                    user_list = "".join([f"- `@{line.strip()}`\n" for line in last_five])
                    await event.reply(f"**🎣 آخر 5 يوزرات مصادة:**\n{user_list}")
                else:
                    await event.reply("لم يتم صيد أي يوزر بعد.")
            except FileNotFoundError:
                await event.reply("ملف اليوزرات المصادة غير موجود.")

        elif command == "تصفية":
            try:
                with open(banned_file, 'r') as f:
                    banned_count = len(f.readlines())
                await event.reply(f"**🚫 عدد اليوزرات المحظورة (المصفاة):** `{banned_count}`")
            except FileNotFoundError:
                await event.reply("ملف اليوزرات المحظورة غير موجود.")

        elif command == "المجلد":
            folder_path = os.path.abspath(data_dir)
            await event.reply(f"**📁 مسار مجلد الحفظ:**\n`{folder_path}`")

        elif command == "ايقاف":
            if bot_running:
                bot_running = False
                await event.reply("**❌ تم إيقاف البوت مؤقتاً.**")
            else:
                await event.reply("**البوت متوقف بالفعل.**")

        elif command == "تشغيل":
            if not bot_running:
                bot_running = True
                await event.reply("**✅ تم استئناف عمل البوت.**")
            else:
                await event.reply("**البوت يعمل بالفعل.**")

    # بدء حلقة الفحص في الخلفية
    asyncio.create_task(mortada_hunter(client))
    # إبقاء البوت متصلاً لاستقبال الأوامر
    await client.run_until_disconnected()

if __name__ == "__main__":
    # تأكد من استبدال my_id بمعرف حسابك
    if my_id == 0:
        print(f"{Z}!!! خطأ: يرجى وضع معرف حسابك الرقمي في متغير 'my_id' للتحكم بالبوت.")
    else:
        asyncio.run(setup_bot())
