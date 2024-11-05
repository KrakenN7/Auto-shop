# Auto-shop
<!-- Добавить бэйджи -->

Интернэт магазин для продажи автомобилей.

## Содержание

- [Содержание](#содержание)
- [Технологии](#технологии)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-cicd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии

- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Postgresql](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Html](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [Css](https://developer.mozilla.org/ru/docs/Web/CSS)

## Начало работы

### Устанавливаем prodовые зависимости

```bash
pip3 install -r requirements/prod.txt
```

### Создаём миграции

```bash
python3 autoshop/manage.py makemigrations main
```

### Запускаем миграции

```bash
python3 autoshop/manage.py migrate main
```

### Запускаем development сервер

```bash
python3 autoshop/manage.py runserver
```

### Требования

  ![python 3.12](https://img.shields.io/badge/Python-3..12-green)

## Тестирование

```bash
python3 autoshop/manage.py test
```

## Deploy и CI/CD

Как запустить пайплайн?

## Contributing

 [Contributing.md](./CONTRIBUTING.md).

## To do

- [x] Добавить крутое README
- [ ] Всё переписать
- [ ] ...

## Команда проекта

- [Кирилл]([https://t.me/nkirill_tg) — Back-End Engineer
