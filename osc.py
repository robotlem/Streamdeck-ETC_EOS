# Streamdeck-ETC_EOS
# osc
# Author: S. Pauthner
# Date:   17.02.2026
import socket
import threading


class TCPClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = None
        self._running = False
        self._recv_thread = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)  # optional
        self.sock.connect((self.host, self.port))
        self._running = True

        self._recv_thread = threading.Thread(target=self._receive_loop, daemon=True)
        self._recv_thread.start()

        print("Connected")

    def send(self, data: bytes):
        if self.sock:
            self.sock.sendall(data)

    def _receive_loop(self):
        try:
            while self._running:
                data = self.sock.recv(4096)
                if not data:
                    print("Connection closed by peer")
                    break

                self.on_data(data)

        except Exception as e:
            print("Receive error:", e)

        finally:
            self._running = False
            self.on_disconnect()

    def on_data(self, data: bytes):
        """Override in subclass"""
        print("Received:", data)

    def on_disconnect(self):
        """Override in subclass"""
        print("Disconnected")

    def close(self):
        self._running = False
        if self.sock:
            self.sock.close()

class EOSClient(TCPClient):

    def on_data(self, data: bytes):
        print("EOS:", data)

    def on_disconnect(self):
        print("EOS connection lost")


