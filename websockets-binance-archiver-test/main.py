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
    while True:
        try:
            async with websockets.connect(BINANCE_FUTURES_DEPTH_URL) as websocket:
                print("Połączono z Binance Futures WebSocket.")
                while True:
                    message = await websocket.recv()
                    print(message)

        except websockets.ConnectionClosed as e:
            print(f"Rozłączono. Próba ponownego połączenia za 5 sekund... (Powód: {e})")
            await asyncio.sleep(5)

        except Exception as e:
            print(f"Wystąpił błąd: {e}. Ponowne łączenie za 5 sekund...")
            await asyncio.sleep(5)

async def main():
    await listen_depth_stream()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())