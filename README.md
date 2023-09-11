# MessageBot

MessageBot - это проект, который позволяет связать ваш аккаунт веб-сайта с Telegram ботом и отправлять уведомления из вашего веб-приложения на Telegram.

## Требования

Для работы с проектом вам потребуется:

- Python (версия 3.10 и выше)
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

   <pre lang="bash">python -m venv venv</pre>

   В macOS и Linux:

   <pre lang="bash">python3 -m venv venv</pre>

4. Активируйте виртуальное окружение (если оно не активировано):

   В Windows:

   <pre lang="bash">venv\Scripts\activate</pre>

   В macOS и Linux:

   ```bash
   source venv/bin/activate

5. Установите зависимости:

   ```bash
   pip install -r requirements.txt

6. Активируйте переменные окружения:

   В Windows:

   <pre lang="bash">setenv.bat</pre>

   В macOS и Linux:

   ```bash
   source setenv.sh

7. Перейдите в папку django_telegram_api:

   ```bash
   cd django_telegram_api

7. Создайте и примените миграции:

   В Windows:

   <pre lang="bash">python manage.py makemigrations
   python manage.py migrate</pre>

   В macOS и Linux:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate

8. Запустите сервер разработки:

   В Windows:

   <pre lang="bash">python manage.py runserver</pre>

   В macOS и Linux:

   ```bash
   python3 manage.py runserver

## Настройка Telegram

Для того чтобы Telegram знал, куда отправлять сообщения, выполните следующий запрос:

   <pre lang="bash">https://api.telegram.org/bot{токен телеграма}/setWebhook?url={url адрес сайта}/message</pre>

## API Endpoints

Регистрация нового пользователя: /api/v1/sign-up/<br>
Вход пользователя: /api/v1/token/login/<br>
Выход пользователя: /api/v1/token/logout/<br>
Получение профиля пользователя: /api/v1/user/slug_user/<br>
Создание сообщения: /api/v1/create_message/<br>

## Web Endpoints

Страница профиля пользователя: /user/slug_user/<br>
Страница регистрации: /sign-up/<br>
Страница входа: /login/<br>
Страница выхода: /logout/<br>
Панель администратора Django: /admin/<br>


#### PS файл setenv.sh намеренно добавлен в репозиторий для возможности проверки проекта