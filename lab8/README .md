# 📋 Todo List API

Простое REST API для управления задачами, построенное на FastAPI + PostgreSQL с асинхронным доступом к базе данных через SQLAlchemy. В комплекте идёт готовый веб-интерфейс.

--

## Описание

Приложение позволяет создавать, просматривать, редактировать и удалять задачи. Каждая задача имеет название, описание и статус, который можно переключать по циклу. Весь бэкенд работает асинхронно; фронтенд представляет собой одностраничное HTML-приложение, общающееся с API напрямую.

**Стек:**
- **FastAPI** - веб-фреймворк
- **SQLAlchemy 2.0 (async)** + **asyncpg** - работа с базой данных
- **PostgreSQL 15** - хранилище данных
- **Docker / Docker Compose** - контейнеризация

--

## Быстрый старт

### Требования

- [Docker](https://docs.docker.com/get-docker/) и Docker Compose

### 1. Клонируйте репозиторий

```bash
git clone <url-репозитория>
cd <папка-проекта>
```

### 2. Создайте файл `.env`

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=todoapi
DB_URL=postgresql+asyncpg://admin:password@database:5432/todoapi
```

### 3. Запустите проект

```bash
docker compose up -build
```

После запуска:
- API доступно по адресу: [http://localhost:8000](http://localhost:8000)
- Интерактивная документация: [http://localhost:8000/docs](http://localhost:8000/docs)
- Веб-интерфейс: откройте `index.html` в браузере

### 4. Остановка

```bash
docker compose down
```

Чтобы также удалить данные базы:

```bash
docker compose down -v
```

--

## Структура проекта

```
.
├── app/
│   ├── main.py               # Точка входа, настройка FastAPI
│   ├── session_dep.py        # Dependency Injection сессии БД
│   ├── database/
│   │   ├── database.py       # Подключение к БД, движок SQLAlchemy
│   │   └── models.py         # ORM-модель Node
│   ├── routers/
│   │   └── nodes.py          # HTTP-роуты /nodes
│   ├── cruds/
│   │   └── nodes.py          # CRUD-операции с БД
│   └── schemas/
│       └── nodes.py          # Pydantic-схемы запросов и ответов
├── index.html                # Веб-интерфейс
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

--

## Справка по API

Базовый URL: `http://localhost:8000`

| Метод    | Путь              | Описание                        |
|-----|----------|-----------------|
| `GET`    | `/nodes`          | Список задач (с пагинацией)     |
| `POST`   | `/nodes`          | Создать задачу                  |
| `GET`    | `/nodes/{id}`     | Получить задачу по ID           |
| `PUT`    | `/nodes/{id}`     | Обновить задачу                 |
| `DELETE` | `/nodes/{id}`     | Удалить задачу                  |

### Параметры пагинации (`GET /nodes`)

| Параметр | Тип   | По умолчанию | Описание                  |
|-----|----|-------|--------------|
| `limit`  | `int` | `10`         | Количество записей        |
| `offset` | `int` | `0`          | Смещение от начала списка |

### Статусы задачи

Задача может находиться в одном из трёх состояний:

| Значение         | Описание      |
|---------|--------|
| `not-completed`  | Не выполнена  |
| `in-progress`    | В процессе    |
| `completed`      | Выполнена     |

### Примеры запросов

**Создать задачу:**
```bash
curl -X POST http://localhost:8000/nodes \
  -H "Content-Type: application/json" \
  -d '{"name": "Купить молоко", "description": "2 литра, 3.2%"}'
```

**Получить список задач:**
```bash
curl "http://localhost:8000/nodes?limit=10&offset=0"
```

**Обновить статус:**
```bash
curl -X PUT http://localhost:8000/nodes/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

**Удалить задачу:**
```bash
curl -X DELETE http://localhost:8000/nodes/1
```
