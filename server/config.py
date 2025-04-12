import argparse #для аргпарса
import logging  #для логирования

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s', #формат записей
        filename='server.log' #запись в файл
    )
#создает парсер аргументов добавялет 2 параметра
def parse_args():
    parser = argparse.ArgumentParser(description='DUMMY_PROTOCOL UDP Server')
    parser.add_argument('--host', required=True, help='Host to bind')
    parser.add_argument('--port', required=True, type=int, help='Port to bind')
    return parser.parse_args()
