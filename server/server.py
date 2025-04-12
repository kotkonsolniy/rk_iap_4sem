import socket
import logging
from protocol import *
from .config import parse_args, setup_logging


def handle_udp_message(sock):
    data, addr = sock.recvfrom(MESSAGE_LENGTH)
    try:
        if len(data) != MESSAGE_LENGTH:
            raise ValueError("Invalid message length")

        message = parse_message(data)
        logging.info(f"Valid message from {addr[0]}:{addr[1]}")
        print(f"Сервером получено корректное сообщение от клиента с ip: {addr[0]}, port: {addr[1]}")
        print(f"Поле 1 (Header): {message['header']}")
        print(f"Поле 2 (Date): {message['date']}")
        print(f"Поле 3 (Number): {message['number']}")

        response = create_message(message['number'] + 12)
        sock.sendto(response, addr)
    except Exception as e:
        logging.error(f"Invalid message from {addr[0]}:{addr[1]}: {str(e)}")
        print(f"Сервером получено некорректное сообщение от клиента с ip: {addr[0]}, port: {addr[1]}")
        sock.sendto(create_invalid_response(), addr)


def run_server():
    setup_logging()
    args = parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((args.host, args.port))
        logging.info(f"UDP Server started on {args.host}:{args.port}")
        print(f"UDP Server started on {args.host}:{args.port}")

        while True:
            handle_udp_message(s)


if __name__ == "__main__":
    run_server()