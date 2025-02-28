
# Приложение для заметок

Этот проект представляет собой RESTful API, разработанный с использованием FastAPI. Он предоставляет функциональность для управления заметками (создание, чтение, обновление, удаление).

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
2. Установите poetry (если ещё не установлен):
```bash
pip install poetry
```
3. Установите зависимости проекта:
```bash
poetry install
```
4. Активируйте виртуальное окружение:
```bash
poetry shell
```
5. Настройте переменные окружения:
Создайте файл .env в корне проекта и добавьте необходимые переменные. Например:
```env
APP__DB__URL=postgresql+asyncpg://user:password@host:port/db_name
APP__AUTH__RESET_PASSWORD_TOKEN_SECRET=SECRET
APP__AUTH__VERIFICATION_TOKEN_SECRET=SECRET
```
6. Добавьте необходимые переменные в docker-compose.yml: Например:
```yml
POSTGRES_DB: testDB
POSTGRES_USER: user
POSTGRES_PASSWORD: password
```
## **Запуск проекта**
1. Запустите сервер разработки:
```bash
poetry run main.py
```
2. Запустите docker-compose.yml:
```bash
docker-compose up -d
```
2.После запуска сервера откройте в браузере:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## **Технологии**
- FastAPI — фреймворк для создания API.
- SQLAlchemy — ORM для работы с базой данных.
- PostgreSQL — база данных.
- Docker — контейнеризация приложения.
- Poetry — управление зависимостями.

## **Лицензия**
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.