import unittest
from unittest.mock import patch, MagicMock
from protocol import *
from ..client import send_udp_message


class TestUDPClient(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.number = 42
        self.valid_response = create_message(self.number + 12)
        self.invalid_response = b'invalid_data'

    @patch('socket.socket')
    def test_send_valid_message(self, mock_socket):
        mock_sock = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock
        mock_sock.recvfrom.return_value = (self.valid_response, (self.host, self.port))

        send_udp_message(self.host, self.port, self.number)

        # Проверяем отправленное сообщение
        sent_message = mock_sock.sendto.call_args[0][0]
        parsed = parse_message(sent_message)
        self.assertEqual(parsed['number'], self.number)

    @patch('socket.socket')
    def test_send_invalid_response(self, mock_socket):
        mock_sock = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock
        mock_sock.recvfrom.return_value = (self.invalid_response, (self.host, self.port))

        send_udp_message(self.host, self.port, self.number)

        # Должен быть вызов logging.error

    @patch('socket.socket')
    def test_timeout_handling(self, mock_socket):
        mock_sock = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock
        mock_sock.recvfrom.side_effect = socket.timeout()

        send_udp_message(self.host, self.port, self.number)

        # Должен быть вызов logging.error для таймаута

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            send_udp_message(self.host, self.port, -1)


if __name__ == '__main__':
    unittest.main()