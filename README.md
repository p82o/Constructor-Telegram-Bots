# Constructor Telegram Bots

**Constructor Telegram Bots** - сайт, с помощью которого вы можете легко, бесплатно и без каких-либо знаний в программирование, сделать своего многофункционального Telegram бота.

Сайт является некоммерческим и не преследует цель заработать на своих пользователях.

Сайт был создан, потому-что к сожелению все похожие сайты являються коммерческими и преследуют цель заработать на своих пользователях, а бесплатный тариф на таких сайтах очень сильно ограничивает своих же пользователей сайта.

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
