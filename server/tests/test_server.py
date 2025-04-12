import unittest
from unittest.mock import patch, MagicMock
from protocol import *
from ..server import handle_udp_message


class TestUDPServer(unittest.TestCase):
    def setUp(self):
        self.valid_message = create_message(42)
        self.invalid_message = b'invalid_data'
        self.mock_sock = MagicMock()
        self.addr = ('127.0.0.1', 12345)

    def test_handle_valid_udp_message(self):
        self.mock_sock.recvfrom.return_value = (self.valid_message, self.addr)

        handle_udp_message(self.mock_sock)

        # Проверяем отправку ответа с числом +12
        response = self.mock_sock.sendto.call_args[0][0]
        parsed = parse_message(response)
        self.assertEqual(parsed['number'], 54)

    def test_handle_invalid_udp_message(self):
        self.mock_sock.recvfrom.return_value = (self.invalid_message, self.addr)

        handle_udp_message(self.mock_sock)

        # Проверяем отправку INVALID_PROTOCOL
        response = self.mock_sock.sendto.call_args[0][0]
        self.assertTrue(response.startswith(b'INVALID_PROTOCOL'))

    def test_handle_short_message(self):
        short_msg = b'short'
        self.mock_sock.recvfrom.return_value = (short_msg, self.addr)

        handle_udp_message(self.mock_sock)

        response = self.mock_sock.sendto.call_args[0][0]
        self.assertTrue(response.startswith(b'INVALID_PROTOCOL'))


if __name__ == '__main__':
    unittest.main()