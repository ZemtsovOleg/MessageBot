# MessageBot

MessageBot - это проект, который позволяет связать ваш аккаунт веб-сайта с Telegram ботом и отправлять уведомления из вашего веб-приложения на Telegram.

## Требования

Для работы с проектом вам потребуется:

- Python (версия 3.10)
- Другие зависимости, указанные в `requirements.txt`

## Установка

1. Склонируйте репозиторий на свой компьютер:

   ```bash
   git clone https://github.com/ZemtsovOleg/MessageBot.git

2. Перейдите в папку проекта:

   ```bash
   cd MessageBot

3. Создайте виртуальное окружение:

В Windows:

   ```bash
   python -m venv venv

В macOS и Linux:

   ```bash
   python3 -m venv venv

4. Активируйте виртуальное окружение (если оно не активировано):

В Windows:

   ```bash
   venv\Scripts\activate

В macOS и Linux:

   ```bash
   source venv/bin/activate

5. Установите зависимости:

   ```bash
   pip install -r requirements.txt

6. Активируйте переменные окружения:

В Windows:

   ```bash
   setenv.bat

В macOS и Linux:

   ```bash
   source setenv.sh

7. Перейдите в папку django_telegram_api:

   ```bash
   cd django_telegram_api

7. Создайте и примените миграции:

В Windows:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

В macOS и Linux:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate

8. Запустите сервер разработки:

В Windows:

   ```bash
   python manage.py runserver

В macOS и Linux:

   ```bash
   python3 manage.py runserver


## API Endpoints

Регистрация нового пользователя: /api/v1/sign-up/
Вход пользователя: /api/v1/token/login/
Выход пользователя: /api/v1/token/logout/
Получение профиля пользователя: /api/v1/user/slug_user/
Создание сообщения: /api/v1/create_message/

## Web Endpoints

Страница профиля пользователя: /user/slug_user/
Страница регистрации: /sign-up/
Страница входа: /login/
Страница выхода: /logout/
Панель администратора Django: /admin/

## Настройка Telegram

Для того чтобы Telegram знал, куда отправлять сообщения, выполните следующий запрос:

```bash
https://api.telegram.org/bot{токен телеграма}/setWebhook?url={url адрес сайта}/message