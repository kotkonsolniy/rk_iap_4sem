import socket #тут импорты аналогичные в сервере
import logging
from protocol import *
from .config import parse_args, setup_logging

#создает udp сокет, формирует и отправляет сообщение, разбирает ответ и проверяет его, если все верно то урааа
def send_udp_message(host, port, number):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = create_message(number)
        s.sendto(message, (host, port))

        s.settimeout(5)  # таймаут 5 секунд
        try:
            response, _ = s.recvfrom(MESSAGE_LENGTH)
            try:
                parsed = parse_message(response)
                if parsed['number'] != number + 12:
                    raise ValueError("Number in response is not increased by 12")

                logging.info("Valid response from server")
                print("Клиентом получено корректное сообщение от сервера.")
                print(f"Поле 1 (Header): {parsed['header']}")
                print(f"Поле 2 (Date): {parsed['date']}")
                print(f"Поле 3 (Number): {parsed['number']}")
            except Exception as e:
                logging.error(f"Invalid response from server: {str(e)}")
                print("Клиентом получено некорректное сообщение от сервера.")
        except socket.timeout:
            logging.error("No response from server")
            print("Клиентом не получен ответ от сервера (таймаут).")

#проверка числа
def run_client():
    setup_logging()
    args = parse_args()

    if args.number < 0:
        logging.error("Number must be non-negative")
        print("Ошибка: число должно быть неотрицательным")
        return

    send_udp_message(args.host, args.port, args.number)

#запуск клиента
if __name__ == "__main__":
    run_client()
