# Flask Web App – HW3

Простий веб-додаток з формою, маршрутизацією та збереженням повідомлень.

##  Структура проєкту

- `templates/index.html` — головна сторінка з описом курсів
- `templates/message.html` — форма відправки повідомлень
- `templates/read.html` — сторінка перегляду збережених повідомлень
- `templates/error.html` — кастомна сторінка 404
- `static/style.css` — стилі
- `static/logo.png` — логотип
- `storage/data.json` — збережені повідомлення у форматі JSON
- `app.py` — основний Flask-додаток

Додатково: 
- `Dockerfile` — інструкції для створення образу Docker
- `docker-compose.yml` — налаштування для запуску контейнера з volume
- `.dockerignore` — файли та каталоги, що не копіюються в образ

##  Запуск застосунку локально

Переконайтеся, що встановлений [Flask](https://flask.palletsprojects.com/):


pip install flask
