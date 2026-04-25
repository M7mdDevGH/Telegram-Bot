from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = '8270317238:AAENqg5dFdXoSOtN1nsBlPjZDg93xz-5LK0'

# 1. رسالة الترحيب - /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎯 مرحباً بك في بوت M7 CyWeb Sy!\n\n"
        "أنا المساعد الرسمي لشركة M7 CyWeb Sy، شركة سورية رائدة في مجال الأمن السيبراني والتوعية الرقمية.\n\n"
        "📌 الأوامر المتاحة:\n"
        "/start - رسالة الترحيب\n"
        "/about - عن شركتنا\n"
        "/services - خدماتنا\n"
        "/contact - طرق التواصل معنا\n"
        "/clavis - أداة Clavis لتوليد كلمات المرور\n\n"
        "🚀 كيف أقدر أساعدك اليوم؟"
    )
    await update.message.reply_text(text)

# 2. رسالة عن الشركة - /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏢 عن M7 CyWeb Sy\n\n"
        "شركة تقنية سورية ناشئة متخصصة في:\n"
        "• الأمن السيبراني\n"
        "• تطوير البرمجيات\n"
        "• التدريب والتوعية الرقمية\n"
        "• حلول الحماية المتكاملة\n\n"
        "👨‍💻 المؤسس: M7\n"
        "🤖 الشريك التقني: DeepSeek AI\n\n"
        "🌍 المقر: سوريا 🇸🇾\n\n"
        "💡 رؤيتنا: الريادة في الأمن السيبراني والتوعية الرقمية في العالم العربي.\n\n"
        "🔗 للمزيد: https://m7mddevgh.github.io/M7-CyWeb-Sy/about.html"
    )
    await update.message.reply_text(text)

# 3. خدماتنا - /services
async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🛡️ خدمات M7 CyWeb Sy:\n\n"
        "1️⃣ Clavis - أداة كلمات المرور\n"
        "مولد ومحلل كلمات مرور قوية\n"
        "🔗 /clavis\n\n"
        "6️⃣ استشارات أمنية\n"
        "تقييم الثغرات، تدريب الموظفين، سياسات أمنية\n"
        "🔗 /contact\n\n"
        "📌 كل هذه الأدوات مجانية ومتاحة للجميع!"
    )
    await update.message.reply_text(text)

# 4. طرق التواصل - /contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📧 تواصل معنا:\n\n"
        "📧 البريد الإلكتروني:\nalsbamodi@gmail.com\n\n"
        "🌐 الموقع الرسمي:\nhttps://m7mddevgh.github.io/M7-CyWeb-Sy/\n\n"
        "💼 GitHub:\nhttps://github.com/m7mddevgh\n\n"
        "📋 نموذج الإبلاغ عن حادث أمني:\nhttps://m7mddevgh.github.io/M7-CyWeb-Sy/report.html\n\n"
        "📞 للاستشارات والخدمات المخصصة:\nاستخدم نموذج 'راسلني' على موقعنا\n\n"
        "⏰ نرد على جميع الاستفسارات خلال 24 ساعة"
    )
    await update.message.reply_text(text)

# 5. أداة Clavis - /clavis
async def clavis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔐 Clavis - حامي كلمات المرور\n\n"
        "أداة مجانية لتوليد وتحليل كلمات المرور:\n\n"
        "✨ المميزات:\n"
        "• توليد كلمات مرور عشوائية قوية\n"
        "• تحليل قوة كلمة المرور\n"
        "• كشف الكلمات الضعيفة\n"
        "• واجهة بسيطة وسهلة\n\n"
        "🛡️ لا تخزن الأداة أي بيانات، كل شي يتم محلياً\n\n"
        "🔗 جرب Clavis الآن:\nhttps://m7mddevgh.github.io/Clavin/\n\n"
        "💡 نصيحة: استخدم كلمات مرور لا تقل عن 12 حرفاً مع أرقام ورموز"
    )
    await update.message.reply_text(text)

# 6. المساعدة - /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ المساعدة - M7 CyWeb Sy Bot\n\n"
        "📌 جميع الأوامر:\n"
        "/start - الصفحة الرئيسية\n"
        "/about - معلومات عن الشركة\n"
        "/services - الخدمات والمنتجات\n"
        "/contact - طرق التواصل\n"
        "/clavis - أداة كلمات المرور\n"
        "/help - هذه القائمة\n\n"
        "💬 للاستفسارات : alsbamodi@gmail.com"
    )
    await update.message.reply_text(text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # تسجيل جميع الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("clavis", clavis))
    app.add_handler(CommandHandler("help", help_command))
    
    print("-" * 30)
    print("تم تشغيل بوت M7 CyWeb Sy بنجاح!")
    print("الرابط: https://t.me/M7CyWeb_bot")
    print("-" * 30)
    
    app.run_polling()
