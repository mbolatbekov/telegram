import telebot
import schedule
import time
import threading

TOKEN = "7970425858:AAGaz_RIO6FEDIogmTXLLepRAlTupD9uo5E"
CHAT_ID = "-1002465564379"

bot = telebot.TeleBot(TOKEN)

# Исходный список людей
people = [
    "Алмат", "Абилкайыр", "Ануар", "Дархан", "Мадияр",
    "Абеке", "Жаке", "Фараби", "Мансур", "Алмаз"
]

# Текущая дата
current_day = 1  # Можно поменять, если нужно

def generate_schedule():
    """Генерирует расписание на текущий день."""
    global current_day
    shift = (current_day - 1) * 10  # Сдвигаем список каждый день на 10
    schedule_list = []
    
    for i, person in enumerate(people):
        start = (i * 10 + shift) % 100 + 1
        end = start + 9
        if i == len(people) - 1:  # Последний читает до 104
            end = 104
        schedule_list.append(f"{i+1}. {person} → {start}-{end}")

    return f"📅 *{current_day:02d}.MM* Расписание на сегодня:\n\n" + "\n".join(schedule_list)

def send_daily_schedule():
    """Отправляет сообщение с расписанием чтения."""
    global current_day
    message = generate_schedule()
    bot.send_message(CHAT_ID, message, parse_mode="Markdown")
    current_day += 1  # Переход к следующему дню

# Запускаем планировщик
schedule.every().day.at("09:00").do(send_daily_schedule)

def schedule_checker():
    """Фоновый процесс для запуска отправки сообщений по расписанию."""
    while True:
        schedule.run_pending()
        time.sleep(30)

# Запуск фонового потока
threading.Thread(target=schedule_checker, daemon=True).start()

# Запускаем бота
bot.polling()




