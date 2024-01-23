## Описание

Currency Rate - это приложение на базе Django, предназначенное для отслеживания и отображения текущего курса доллара к рублю. Проект использует ExchangeRateAPI для получения актуальных курсов валют и отображает последние 10 запросов курса.

## Основные функции

- Получение актуального курса доллара к рублю с использованием внешнего API.
- Отображение 10 последних запросов курса.
- Автоматическое обновление курса валют с интервалом в 10 секунд.

## Технологии

- **Backend**: Django
- **Database**: SQLite (по умолчанию для Django)
- **Task Queue**: Celery
- **Message Broker**: Redis

## Начало работы

### Предварительные требования

Убедитесь, что у вас установлены следующие инструменты:
- Python (версия 3.10)
- pip
- Virtualenv

### Установка и настройка

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/Abdunazarov/currency_rate.git
   cd currency_rate
   ```

2. **Настройка виртуального окружения**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка базы данных**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Запуск сервера разработки**

   ```bash
   python manage.py runserver
   ```

   После запуска сервера приложение будет доступно по адресу `http://localhost:8000/`.

6. **Запуск Celery Worker и Celery Beat**

   Откройте новые терминалы и активируйте виртуальное окружение. Затем выполните:

   ```bash
   # В одном терминале
   celery -A currency_rate worker -l info

   # В другом терминале
   celery -A currency_rate beat -l info
   ```

## Использование

Для получения текущего курса доллара и просмотра последних запросов в формате JSON перейдите по адресу:

```
http://localhost:8000/get-current-usd/
```

## Тесты

Для тестирования эндпоинта, можно воспользоваться тестами, написанными ```django.test.TestCase```. Выполните в терминале:

```bash
python manage.py test currency_rate
```
