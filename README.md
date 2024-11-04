# Auto-shop

## Стэк:

- Django
- Bootstrap
- Postgresql

## Требования:

- python 3.12

## Запуск приложения

### Установка зависимостей

```bash
pip3 install -r requirements/prod.txt
```

### Запуск миграций

```bash
cd autoshop
python3 manage.py makemigrations main
```

### Запуск тестов

```bash
python3 manage.py test
```

### Запуск сервера для разработки

```bash
python3 manage.py runserver
```
