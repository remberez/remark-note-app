
# Приложение для заметок Remark

Этот проект представляет собой RESTful API + Frontend, разработанный с использованием FastAPI + React. Он предоставляет функциональность для управления заметками (создание, чтение, обновление, удаление).

---

## **Оглавление**
1. [Установка](#установка)
2. [Запуск проекта](#запуск-проекта)
3. [Технологии](#технологии)
4. [Лицензия](#лицензия)

---

## **Установка**

1. Клонируйте репозиторий:
```bash
git clone https://github.com/remberez/NoteApp
cd NoteApp
```
2. Установите Docker (если ещё не установлен):
3. Настройте переменные окружения:
Создайте файл .env в корне проекта и добавьте необходимые переменные. Например:
```env
APP__DB__URL=postgresql+asyncpg://user:password@pg/db_name
APP__AUTH__RESET_PASSWORD_TOKEN_SECRET=SECRET
APP__AUTH__VERIFICATION_TOKEN_SECRET=SECRET
```
6. Добавьте необходимые переменные в docker-compose.yml: Например:
```yml
POSTGRES_DB: db_name
POSTGRES_USER: user
POSTGRES_PASSWORD: password
```
## **Запуск проекта**
1. Запустите сервер docker-compose:
```bash
docker-compose up
```
2.После запуска сервера откройте в браузере:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **Frontend**: http://localhost

## **Технологии**
- FastAPI — фреймворк для создания API.
- SQLAlchemy — ORM для работы с базой данных.
- PostgreSQL — база данных.
- Docker — контейнеризация приложения.
- Poetry — управление зависимостями.
- React - фронтенд часть приложения.
- Vite - для настройки среды разработки.
- Nginx - обратынй прокси-сервер и веб-сервер для статических файлов.

## **Лицензия**
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
