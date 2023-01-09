import ptbot
import sys
import pytimeparse

TG_TOKEN = sys.argv[1]
BOT = ptbot.Bot(TG_TOKEN)


def timer_end(chat_id):
    message = 'Время вышло!'
    BOT.send_message(chat_id, message)


def notify_progress(secs_left, chat_id, message_id, secs_total):
    message = f'Осталось секунд: {secs_left}\n{render_progressbar(total=secs_total, iteration=secs_total-secs_left)}'
    BOT.update_message(chat_id=chat_id, message_id=message_id, new_message=message)


def wait(chat_id, question):
    timer = pytimeparse.parse(question)
    message_id = BOT.send_message(chat_id=chat_id, message='Запускаю таймер')
    BOT.create_countdown(timer, notify_progress, secs_total=timer, chat_id=chat_id, message_id=message_id)
    BOT.create_timer(timer, timer_end, chat_id=chat_id)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    print('Бот запущен!')
    BOT.reply_on_message(wait)
    BOT.run_bot()


if __name__ == '__main__':
    main()
