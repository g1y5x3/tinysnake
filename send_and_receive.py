import time
import json
import random
import asyncio
import websockets

async def handler(websocket):
  while True:
    await websocket.send('s')
    msg = await websocket.recv()
    states = json.loads(msg)
    print(states)

    msg = str(random.randint(0,3))
    print(msg)
    await websocket.send(msg)

    time.sleep(1/30)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())