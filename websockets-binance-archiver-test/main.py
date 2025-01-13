import asyncio
import websockets

BINANCE_FUTURES_DEPTH_URL = (
    "wss://fstream.binance.com/stream?"
    "streams=btcusdt@depth@100ms/"
    "ethusdt@depth@100ms/"
    "bnbusdt@depth@100ms/"
    "solusdt@depth@100ms/"
    "xrpusdt@depth@100ms/"
    "dogeusdt@depth@100ms/"
    "adausdt@depth@100ms/"
    "ltcusdt@depth@100ms/"
    "avaxusdt@depth@100ms/"
    "trxusdt@depth@100ms/"
    "dotusdt@depth@100ms/"
    "bchusdt@depth@100ms/"
    "suiusdt@depth@100ms"
)

async def listen_depth_stream():
    print("Łączenie z Binance Futures WebSocket...")
    async with websockets.connect(BINANCE_FUTURES_DEPTH_URL) as websocket:
        print("Połączono z Binance Futures WebSocket.")
        try:
            while True:
                message = await websocket.recv()
                print(f"\r{message}", end="", flush=True)
        except Exception as e:
            print(f"\nWystąpił błąd: {e}")
            return

async def main():
    await listen_depth_stream()

if __name__ == "__main__":
    asyncio.run(main())
