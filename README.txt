DUMMY_PROTOCOL Client-Server System

Описание:
Система состоит из клиента и сервера, взаимодействующих по протоколу DUMMY_PROTOCOL.
Протокол поддерживает передачу неотрицательного числа с проверкой корректности сообщений.

Функциональные возможности:
- Поддержка TCP и UDP транспорта
- Проверка корректности сообщений
- Логирование всех событий
- Гибкая настройка через аргументы командной строки

Инструкции по развертыванию (Linux):

1. Установите Python 3.8+
2. Создайте виртуальное окружение:
   python -m venv venv
   source venv/bin/activate

3. Установите зависимости:
   pip install -r requirements.txt

4. Запуск сервера (TCP):
   python -m server.server --host 127.0.0.1 --port 12345 --protocol tcp

5. Запуск клиента (TCP):
   python -m client.client --host 127.0.0.1 --port 12345 --protocol tcp --number 42

6. Для UDP замените --protocol на udp

Тестирование:
- Запуск тестов сервера:
  python -m server.tests.test_server

- Запуск тестов клиента:
  python -m client.tests.test_client

Требования:
- Python 3.8+
- Для тестов: pytest (опционально)