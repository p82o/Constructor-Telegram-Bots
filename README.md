# Constructor Telegram Bots

**Constructor Telegram Bots** - сайт, с помощью которого вы можете легко, бесплатно и без каких-либо знаний в программировании сделать своего многофункционального Telegram бота.

## Требования
- Python 3.11.x
- PostgreSQL
- MongoDB
- Redis

## Установка проекта и запуск сайта
1. Клонируем проект и запускаем скрипт для его установки:
```
git clone https://github.com/p82o/Constructor-Telegram-Bots.git
cd Constructor-Telegram-Bots
source scripts/setup.sh
```
2. Теперь запускаем сайт:
```
python manage.py runserver
```
3. Открываем ещё один терминал и запускаем Celery worker:
```
cd Constructor-Telegram-Bots
source env/bin/activate
cd constructor_telegram_bots
celery -A constructor_telegram_bots worker --loglevel=INFO -f logs/celery.log
```
4. Пользуемся сайтом ☺️!
