import argparse #аналогичные импорты как и в сервере
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO, #уровень логирования
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='client.log' #запись логов в файл
    )
#парсер командной строки добавляет еще на вход и неотрицательное число для отправки
def parse_args():
    parser = argparse.ArgumentParser(description='DUMMY_PROTOCOL UDP Client')
    parser.add_argument('--host', required=True, help='Server host')
    parser.add_argument('--port', required=True, type=int, help='Server port')
    parser.add_argument('--number', type=int, required=True, help='Non-negative number to send')
    return parser.parse_args()
