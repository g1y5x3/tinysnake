import time
import random
import asyncio
import websockets

async def handler(websocket):
  while True:
    message = str(random.randint(0,3)) 
    print(message)
    await websocket.send(message)
    time.sleep(0.1)

async def main():
  async with websockets.serve(handler, "", 8001):
    await asyncio.Future()  # run forever

if __name__ == "__main__":
  # input("Press Enter to continue...")
  asyncio.run(main())