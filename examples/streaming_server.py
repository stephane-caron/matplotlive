#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Stream sine waves from streaming_server.py to TCP clients."""

import asyncio
import math
import socket

import msgpack
from loop_rate_limiters import AsyncRateLimiter

waves: dict = {}

OMEGA = 20.0  # rad/s


async def update():
    """Update time series in the global dictionary."""
    global waves
    rate = AsyncRateLimiter(frequency=200.0)
    t = 0.0
    while True:
        waves["sine"] = math.sin(OMEGA * t)
        waves["cosine"] = 3 * math.cos(OMEGA * t)
        t += rate.dt
        await rate.sleep()


async def serve(client, address) -> None:
    """Serve a new client.

    Args:
        client: Socket of the connection.
        address: Pair of IP address and port.
    """
    loop = asyncio.get_event_loop()
    request: str = "start"
    packer = msgpack.Packer(use_bin_type=True)
    print(f"New connection from {address[0]}:{address[1]}")
    while request != "stop":
        data = await loop.sock_recv(client, 4096)
        if not data:
            break
        request = data.decode("utf-8").strip()
        if request == "get":
            reply = packer.pack(waves)
            await loop.sock_sendall(client, reply)
    print(f"Closing connection with {address[0]}:{address[1]}")
    client.close()


async def listen():
    """Listen to incoming connections on port 4747."""
    loop = asyncio.get_event_loop()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 4747))
    server_socket.listen(8)
    server_socket.setblocking(False)  # required by loop.sock_accept
    while True:
        client_socket, address = await loop.sock_accept(server_socket)
        loop.create_task(serve(client_socket, address))


async def main():
    """Launch the two coroutines of this example server."""
    await asyncio.gather(update(), listen())


if __name__ == "__main__":
    asyncio.run(main())
