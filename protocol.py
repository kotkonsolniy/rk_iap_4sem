#реализуем работу  с протоколом DUMMY_PROTOCOL
import struct
from datetime import datetime

BMSTU_PROTOCOL_HEADER = b'BMSTU_PROTOCOL\x00\x00\x00' #можно сделать b'BMSTU_PROTOCOL\x00\x00, тогда в 16 уложимся))
DATE_FORMAT = "%d%m%Y"
HEADER_LENGTH = 17 #BMSTU protocol это 14 байт, \x00\x00\xoo 3 байта 14+3 = 17, поэтому нужно ожидать 17 а не 16
DATE_LENGTH = 8 #длина поля даты
NUMBER_LENGTH = 4 #длина числового поля
MESSAGE_LENGTH = HEADER_LENGTH + DATE_LENGTH + NUMBER_LENGTH #общая длина сообщения 29 байт

#функция получения текущей даты
def create_message(number: int) -> bytes:
    current_date = datetime.now().strftime(DATE_FORMAT).encode('ascii')
    number_bytes = struct.pack('>I', number)  # uint32
    return BMSTU_PROTOCOL_HEADER + current_date + number_bytes

#проверяет длину сообщения извлекает и проверяет заголовок
def parse_message(message: bytes) -> dict:
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

#создает сообщение об ошибке
def create_invalid_response() -> bytes:
    return b'INVALID_PROTOCOL' + bytes(HEADER_LENGTH - len('INVALID_PROTOCOL')) + b'\x00' * (
                DATE_LENGTH + NUMBER_LENGTH)