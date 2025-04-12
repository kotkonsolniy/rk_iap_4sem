import argparse
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='server.log'
    )

def parse_args():
    parser = argparse.ArgumentParser(description='DUMMY_PROTOCOL UDP Server')
    parser.add_argument('--host', required=True, help='Host to bind')
    parser.add_argument('--port', required=True, type=int, help='Port to bind')
    return parser.parse_args()