# Django Hotel Project

Этот проект представляет собой систему управления отелем, созданную с использованием Django и PostgreSQL. Ниже приведены инструкции по установке и запуску проекта на локальном компьютере.

## Требования

- Python 3.x
- PostgreSQL
- pip (менеджер пакетов Python)

## Установка

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/sergei-er/Django_hotel.git
cd Django_hotel

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```
Убедитесь, что PostgreSQL установлен и запущен на вашем компьютере. Если PostgreSQL не установлен, следуйте официальным инструкциям по установке для вашей операционной системы

Создайте новую базу данных и пользователя для проекта:
```bash
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'yourpassword';
ALTER ROLE hotel_user WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;
```
Выполнение миграций

После того, как база данных настроена, выполните миграции для создания необходимых таблиц в базе данных:

```bash
python manage.py makemigrations
python manage.py migrate
```
Создание суперпользователя

Для доступа к админ-панели Django создайте суперпользователя(доступен по адресу http://127.0.0.1:8000/admin):
```bash
python manage.py createsuperuser
```

