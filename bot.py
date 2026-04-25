import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد السجلات (Logs) لمراقبة عمل البوت على السيرفر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# سحب التوكن من إعدادات السيرفر (Environment Variables)
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر البداية"""
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🌐 زيارة موقع M7 CyWeb Sy", url="https://m7mddevgh.github.io/M7-CyWeb-Sy/")],
        [InlineKeyboardButton("🔐 أداة Clavis", url="https://m7mddevgh.github.io/Clavin/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"أهلاً بك يا {user.first_name} في بوت شركة M7 CyWeb Sy للأمن السيبراني.\n\n"
        "نحن هنا لحماية فضائك الرقمي. اختر من الخيارات أدناه:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر المساعدة"""
    await update.message.reply_text("يمكنك التواصل مع الإدارة الفنية لشركة M7 عبر الموقع الرسمي.")

if __name__ == '__main__':
    # التأكد من وجود التوكن قبل التشغيل
    if not TOKEN:
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

