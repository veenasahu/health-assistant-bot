from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random

TOKEN = '8003515324:AAHug7b0bIcfFeN2UECuzL5YoZzpoJAxe1s'

health_tips = [
    "💧 Drink at least 8 glasses of water daily.",
    "🧘 Practice deep breathing to manage stress.",
    "🥗 Eat 5 servings of fruits and veggies daily.",
    "🏃‍♂️ Exercise for 30 minutes a day.",
    "😴 Aim for 7–9 hours of quality sleep."
]

calorie_dict = {
    "apple": 95, "banana": 105, "egg": 78, "bread": 66,
    "rice": 206, "chicken": 239, "milk": 103
}

# Function to create the main button options
def main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Health Tips", callback_data='tips')],
        [InlineKeyboardButton("Check BMI", callback_data='bmi')],
        [InlineKeyboardButton("Mental Health", callback_data='mental')]
    ])

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I’m your Health Assistant Bot.\nChoose from below options:",
        reply_markup=main_buttons()
    )

# /health command
async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Explore:\n- /tips\n- /hydration\n- /calories food_name\n- /bmi weight height\n- /stress\n- /reminder",
        reply_markup=main_buttons()
    )

# /tips command
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(health_tips), reply_markup=main_buttons())

# /bmi command
async def bmi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        weight, height = map(float, context.args)
        bmi_val = weight / (height ** 2)
        category = (
            "Underweight" if bmi_val < 18.5 else
            "Normal" if bmi_val < 24.9 else
            "Overweight" if bmi_val < 29.9 else
            "Obese"
        )
        await update.message.reply_text(f"⚖️ Your BMI is {bmi_val:.2f} — {category}", reply_markup=main_buttons())
    except:
        await update.message.reply_text("❗ Usage: /bmi weight(kg) height(m)\nExample: /bmi 70 1.75", reply_markup=main_buttons())

# /hydration command
async def hydration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💧 Drink water every 2 hours.", reply_markup=main_buttons())

# /calories command
async def calories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    food = ' '.join(context.args).lower()
    cal = calorie_dict.get(food)
    if cal:
        await update.message.reply_text(f"🍽️ 1 serving of {food} has ~{cal} kcal.", reply_markup=main_buttons())
    else:
        await update.message.reply_text("❌ Food not found. Try: apple, banana, egg, bread, rice, chicken, milk.", reply_markup=main_buttons())

# /reminder command
async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Daily Reminder:\n• Stretch\n• Drink water\n• Breathe\n• Walk",
        reply_markup=main_buttons()
    )

# /stress command
async def stress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips = [
        "🧘 Try deep breathing for 3 minutes.",
        "🎧 Listen to calming music.",
        "📴 Take a 15-minute screen break.",
        "👣 Take a short walk outside.",
        "📓 Journal your thoughts for 5 minutes."
    ]
    await update.message.reply_text(random.choice(tips), reply_markup=main_buttons())

# Inline button callback handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'tips':
        await query.message.reply_text(random.choice(health_tips), reply_markup=main_buttons())
    elif query.data == 'bmi':
        await query.message.reply_text("🧮 Use `/bmi weight height`\nExample: `/bmi 70 1.75`", reply_markup=main_buttons())
    elif query.data == 'mental':
        await query.message.reply_text("🧠 Mental Health Tip:\nTalk to someone, meditate, take breaks.", reply_markup=main_buttons())

# Bot Setup
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("health", health))
app.add_handler(CommandHandler("tips", tips))
app.add_handler(CommandHandler("bmi", bmi))
app.add_handler(CommandHandler("hydration", hydration))
app.add_handler(CommandHandler("calories", calories))
app.add_handler(CommandHandler("reminder", reminder))
app.add_handler(CommandHandler("stress", stress))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
