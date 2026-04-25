import os
import logging
import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")

# تخزين مؤقت لأسماء المستخدمين (سيتم مسحها عند إعادة تشغيل السيرفر في النسخة المجانية)
# للحفاظ عليها بشكل دائم نحتاج لقاعدة بيانات، لكن حالياً سنستخدم قائمة بسيطة.
users_log = {}

# --- الدوال الأساسية (التي برمجناها سابقاً) ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    users_log[user.id] = f"@{user.username}" if user.username else user.first_name
    
    keyboard = [[InlineKeyboardButton("🌐 الموقع الرسمي", url="https://m7mddevgh.github.io/M7-CyWeb-Sy/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"🎯 مرحباً بك {user.first_name} في بوت M7 CyWeb Sy!\nاستخدم /help لرؤية الأوامر الجديدة.", reply_markup=reply_markup)

# --- الدوال الجديدة الاحترافية ---

async def generate_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/gen [الطول] [رموز] [أرقام] [كبيرة] [صغيرة]"""
    try:
        args = context.args
        length = int(args[0]) if len(args) > 0 else 12
        use_symbols = args[1].lower() == 'نعم' if len(args) > 1 else True
        use_numbers = args[2].lower() == 'نعم' if len(args) > 2 else True
        use_upper = args[3].lower() == 'نعم' if len(args) > 3 else True
        use_lower = args[4].lower() == 'نعم' if len(args) > 4 else True

        chars = ""
        if use_symbols: chars += string.punctuation
        if use_numbers: chars += string.digits
        if use_upper: chars += string.ascii_uppercase
        if use_lower: chars += string.ascii_lowercase
        
        if not chars: chars = string.ascii_letters + string.digits

        password = "".join(random.choice(chars) for _ in range(length))
        await update.message.reply_text(f"🔐 كلمة المرور المولدة:\n`{password}`", parse_mode='MarkdownV2')
    except Exception:
        await update.message.reply_text("❌ خطأ في الصيغة! استخدم:\n/gen 16 نعم نعم نعم نعم")

async def check_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/check [الرابط]"""
    if not context.args:
        await update.message.reply_text("⚠️ يرجى وضع الرابط بعد الأمر. مثال:\n/check google.com")
        return
    
    link = context.args[0]
    # محاكاة فحص أمني بسيط (توعوي)
    await update.message.reply_text(
        f"🔍 جاري تحليل الرابط: {link}\n\n"
        "💡 نصيحة أمنية من M7:\n"
        "1. تأكد من بروتوكول HTTPS.\n"
        "2. انتبه من الروابط المختصرة.\n"
        "3. لا تقم بإدخال بياناتك الحساسة إلا بعد التأكد من النطاق (Domain) الرسمي."
    )

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/admin - عرض المستخدمين"""
    # يمكنك وضع ID حسابك هنا لضمان أنك الوحيد الذي يرى البيانات
    count = len(users_log)
    names = "\n".join(users_log.values())
    await update.message.reply_text(
        f"📊 إحصائيات البوت (الإدارة):\n\n"
        f"👥 عدد المستخدمين: {count}\n"
        f"📝 القائمة:\n{names if names else 'لا يوجد مستخدمين بعد'}"
    )

if __name__ == '__main__':
    if not TOKEN:
        print("خطأ: TOKEN مفقود!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('gen', generate_password))
        app.add_handler(CommandHandler('check', check_link))
        app.add_handler(CommandHandler('admin', admin_panel))
        
        print("البوت يعمل بالأوامر المتقدمة...")
        app.run_polling()
        print("خطأ: لم يتم العثور على TELEGRAM_TOKEN في إعدادات السيرفر!")
    else:
        print("جاري تشغيل بوت M7 CyWeb Sy بنجاح...")
        
        # بناء التطبيق
        application = ApplicationBuilder().token(TOKEN).build()
        
        # إضافة الأوامر
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))
        
        # بدء العمل
        application.run_polling()

