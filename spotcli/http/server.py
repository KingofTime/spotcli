import sys
import signal
import urllib.parse

import asyncio


async def app(scope, receive, send):
    loop = asyncio.get_running_loop()
    if scope['path'] == "/callback":
        encoded_query_string = scope['query_string'].decode('utf-8')
        query_string = urllib.parse.parse_qs(encoded_query_string)
        code = query_string.get('code', None)

        if code:
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [
                    [b'content-type', b'application/json'],
                ]
            })
        else:
            await send({
                'type': 'http.response.start',
                'status': 400,
                'headers': [
                    [b'content-type', b'application/json'],
                ]
            })

        loop.stop()
