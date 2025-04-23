import telebot
import threading
import subprocess
import os
import time
import zipfile
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ==================== الإعدادات الأساسية ====================
TOKEN = "7544847046:AAFyhfhUq03LrPQulSfDYmb2zZ5K5OhkKsI"
OWNER_ID = 5833417353
CHANNEL = "@GJwXSznFVn44YTg0"
USER_PASSWORD = "SecureZero$1"
ADMIN_PASSWORD = "Z3r0_Host#99"

# ==================== إعدادات النظام ====================
def setup_directories():
    """إنشاء الهيكل الأساسي للمجلدات"""
    try:
        base_dir = os.getcwd()
        users_dir = os.path.join(base_dir, "users")
        os.makedirs(users_dir, exist_ok=True)
        print("✅ تم إنشاء هيكل الملفات")
    except Exception as e:
        print(f"❌ خطأ في إنشاء المجلدات: {str(e)}")
        exit(1)

setup_directories()

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# ==================== قواعد البيانات ====================
users_db = {
    "active": {},
    "banned": set(),
    "stats": {
        "total_users": 0,
        "total_files": 0,
        "total_runs": 0
    },
    "command_log": {}
}

running_scripts = {}

# ==================== وظائف مساعدة ====================
def check_subscription(user_id):
    """التحقق من اشتراك المستخدم في القناة"""
    try:
        chat = bot.get_chat(CHANNEL)
        status = bot.get_chat_member(chat.id, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"⚠️ خطأ في التحقق: {str(e)}")
        return False

def scan_for_malware(file_path):
    """فحص الملفات للكشف عن الأوامر الخطيرة"""
    dangerous_patterns = [
        "os.system", 
        "subprocess.call", 
        "shutil.rmtree",
        "rm -rf", 
        "eval(", 
        "exec(",
        "import os, subprocess"
    ]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            for line in content.split('\n'):
                line = line.split('#')[0].strip()  # تجاهل التعليقات
                if any(pattern in line for pattern in dangerous_patterns):
                    return True
            return False
    except:
        return False

# ==================== إدارة العمليات ====================
def stop_script(user_id, file_index):
    if user_id in running_scripts and file_index in running_scripts[user_id]:
        running_scripts[user_id][file_index].terminate()
        del running_scripts[user_id][file_index]
        return True
    return False

def delete_file(user_id, file_index):
    try:
        file_path = users_db["active"][user_id]["files"][file_index]["path"]
        if os.path.exists(file_path):
            os.remove(file_path)
        return True
    except:
        return False

# ==================== واجهات المستخدم ====================
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📤 رفع ملف", "🔄 الترقية")
    markup.row("📂 ملفاتي", "📊 إحصائياتي")
    return markup

def admin_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("👑 لوحة التحكم", "📜 سجل الأوامر")
    return markup

# ==================== معالجة الأوامر ====================
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    if user_id in users_db["banned"]:
        bot.send_message(user_id, "🚫 تم حظرك!")
        return
    
    if not check_subscription(user_id):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("انضم للقناة", url=f"https://t.me/{CHANNEL[1:]}"))
        bot.send_message(user_id, "❗ اشترك في القناة أولاً", reply_markup=markup)
        return
    
    if user_id not in users_db["active"]:
        msg = bot.send_message(user_id, "🔐 أدخل كلمة المرور:")
        bot.register_next_step_handler(msg, process_password)
    else:
        send_welcome(message)

def process_password(message):
    user_id = message.chat.id
    password = message.text
    
    if password == ADMIN_PASSWORD and user_id == OWNER_ID:
        users_db["active"][user_id] = {"files": [], "runs_count": 0}
        send_welcome(message)
    elif password == USER_PASSWORD:
        users_db["active"][user_id] = {"files": [], "runs_count": 0}
        users_db["stats"]["total_users"] += 1
        send_welcome(message)
    else:
        bot.send_message(user_id, "❌ كلمة مرور خاطئة!")

def send_welcome(message):
    user_id = message.chat.id
    if user_id == OWNER_ID:
        bot.send_message(user_id, "👑 مرحبًا المالك!", reply_markup=admin_menu())
    else:
        bot.send_message(user_id, "🚀 أهلاً بك!", reply_markup=main_menu())

# ==================== إدارة الملفات ====================
@bot.message_handler(content_types=['document'])
def handle_file(message):
    user_id = message.chat.id
    if user_id not in users_db["active"]:
        return
    
    file_info = bot.get_file(message.document.file_id)
    file_name = message.document.file_name
    file_ext = file_name.split('.')[-1].lower()
    
    user_dir = os.path.join("users", str(user_id))
    os.makedirs(user_dir, exist_ok=True)
    
    file_path = os.path.join(user_dir, file_name)
    downloaded_file = bot.download_file(file_info.file_path)
    
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)
    
    if file_ext == 'py' and scan_for_malware(file_path):
        os.remove(file_path)
        users_db["banned"].add(user_id)
        bot.send_message(user_id, "🚨 ملف خبيث!")
        bot.send_message(OWNER_ID, f"⚠️ تم حظر {user_id}")
        return
    
    if file_ext == 'zip':
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(user_dir)
            os.remove(file_path)
            bot.send_message(user_id, "📦 تم الاستخراج!")
        except Exception as e:
            bot.send_message(user_id, f"❌ خطأ: {str(e)}")
    elif file_ext == 'py':
        def run_script():
            process = subprocess.Popen(
                ["python3", file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if user_id not in running_scripts:
                running_scripts[user_id] = {}
            running_scripts[user_id][len(users_db["active"][user_id]["files"])] = process
            users_db["stats"]["total_runs"] += 1
            users_db["active"][user_id]["runs_count"] += 1
        
        threading.Thread(target=run_script).start()
        bot.send_message(user_id, "✅ تم التشغيل!")
    
    users_db["active"][user_id]["files"].append({
        "name": file_name,
        "path": file_path,
        "status": "running" if file_ext == 'py' else "uploaded"
    })
    users_db["stats"]["total_files"] += 1

# ==================== التحكم في الملفات ====================
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    user_id = call.message.chat.id
    data = call.data
    
    if data.startswith("stop_"):
        index = int(data.split("_")[1])
        if stop_script(user_id, index):
            users_db["active"][user_id]["files"][index]["status"] = "stopped"
            bot.answer_callback_query(call.id, "⏹ تم الإيقاف")
        else:
            bot.answer_callback_query(call.id, "⚠️ لا يوجد عملية نشطة")
    
    elif data.startswith("delete_"):
        index = int(data.split("_")[1])
        if delete_file(user_id, index):
            del users_db["active"][user_id]["files"][index]
            bot.answer_callback_query(call.id, "🗑️ تم الحذف")
        else:
            bot.answer_callback_query(call.id, "❌ فشل الحذف")
    
    elif data.startswith("restart_"):
        index = int(data.split("_")[1])
        file_path = users_db["active"][user_id]["files"][index]["path"]
        def run_script():
            process = subprocess.Popen(["python3", file_path])
            running_scripts[user_id][index] = process
        threading.Thread(target=run_script).start()
        users_db["active"][user_id]["files"][index]["status"] = "running"
        bot.answer_callback_query(call.id, "🔄 تم إعادة التشغيل")

# ==================== التشغيل ====================
if __name__ == "__main__":
    print("✅ البوت يعمل...")
    bot.infinity_polling()
