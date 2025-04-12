import struct
from datetime import datetime

BMSTU_PROTOCOL_HEADER = b'BMSTU_PROTOCOL\x00\x00\x00'
DATE_FORMAT = "%d%m%Y"
HEADER_LENGTH = 16
DATE_LENGTH = 8
NUMBER_LENGTH = 4
MESSAGE_LENGTH = HEADER_LENGTH + DATE_LENGTH + NUMBER_LENGTH


def create_message(number: int) -> bytes:
    """Создает сообщение по протоколу DUMMY_PROTOCOL"""
    current_date = datetime.now().strftime(DATE_FORMAT).encode('ascii')
    number_bytes = struct.pack('>I', number)  # uint32 big-endian
    return BMSTU_PROTOCOL_HEADER + current_date + number_bytes


def parse_message(message: bytes) -> dict:
    """Парсит сообщение по протоколу DUMMY_PROTOCOL"""
    if len(message) != MESSAGE_LENGTH:
        raise ValueError("Invalid message length")

    header = message[:HEADER_LENGTH]
    if header != BMSTU_PROTOCOL_HEADER:
        raise ValueError("Invalid protocol header")

    date_str = message[HEADER_LENGTH:HEADER_LENGTH + DATE_LENGTH].decode('ascii')
    try:
        datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        raise ValueError("Invalid date format")

    number = struct.unpack('>I', message[HEADER_LENGTH + DATE_LENGTH:])[0]

    return {
        'header': header,
        'date': date_str,
        'number': number
    }


def create_invalid_response() -> bytes:
    """Создает сообщение об ошибке"""
    return b'INVALID_PROTOCOL' + bytes(HEADER_LENGTH - len('INVALID_PROTOCOL')) + b'\x00' * (
                DATE_LENGTH + NUMBER_LENGTH)