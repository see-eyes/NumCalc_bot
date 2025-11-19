import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен из переменной окружения
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def calculate_pythagoras_square(date_str):
    """Расчёт психоматрицы Пифагора"""
    try:
        day, month, year = map(int, date_str.split('.'))
        
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            return None, "❌ Некорректная дата. Используйте формат ДД.ММ.ГГГГ"
        
        # Расчётные числа
        all_digits = [int(d) for d in str(day) + str(month) + str(year)]
        first_number = sum(all_digits)
        second_number = sum(int(d) for d in str(first_number))
        first_digit_day = int(str(day)[0])
        third_number = first_number - (2 * first_digit_day)
        fourth_number = sum(int(d) for d in str(abs(third_number)))
        
        # Рабочая строка
        work_string = str(day) + str(month) + str(year) + str(first_number) + str(second_number) + str(third_number) + str(fourth_number)
        
        # Подсчёт цифр
        matrix = {}
        for i in range(1, 10):
            count = work_string.count(str(i))
            matrix[i] = count
        
        return {
            'date': date_str,
            'first': first_number,
            'second': second_number,
            'third': third_number,
            'fourth': fourth_number,
            'matrix': matrix,
            'work_string': work_string,
            'count': len(work_string)
        }, None
        
    except Exception as e:
        return None, f"❌ Ошибка: {str(e)}"

def format_matrix(result):
    """Форматирование результата"""
    m = result['matrix']
    
    text = f"""
🔮 **ПСИХОМАТРИЦА ПИФАГОРА**

📅 Дата: {result['date']}

📊 **Расчётные числа:**
1️⃣ {result['first']}
2️⃣ {result['second']}
3️⃣ {result['third']}
4️⃣ {result['fourth']}

🔢 Рабочая строка: `{result['work_string']}`
🎯 Количество цифр: {result['count']}

**МАТРИЦА:**
