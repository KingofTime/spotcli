import asyncio

import uvicorn

class Listener(object):
    port: int
    config: uvicorn.Config
    server: uvicorn.Server

    def __init__(self, port:int=8000):
        self.port = port
        self.config = uvicorn.Config(
            "spotcli.http.server:app",
            port=self.port,
            log_level="info"
        )

    def run(self):
        self.server = uvicorn.Server(self.config)
        try:
            asyncio.run(self.server.serve())
        except RuntimeError:
            ...

    def __str__(self):
        return f"HTTP Listener - Port {self.port}"
