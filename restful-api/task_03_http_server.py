#!/usr/bin/python3
"""
This module is a server to listening trafic in desired port
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps


class Handler(BaseHTTPRequestHandler):
    """
    Object server to catch spécific request
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(dumps(data).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {
                "version": "1.0", 
                "description": "A simple API built with http.server"
                }
            self.wfile.write(dumps(data).encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write("Not found".encode("utf-8"))


if __name__ == "__main__":
    print("server lauched")
    server = HTTPServer(("localhost", 8000), Handler)
    server.serve_forever()
