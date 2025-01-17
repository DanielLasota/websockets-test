import asyncio
import websockets

links = [
    "wss://stream.binance.com:443/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/shibusdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms",
    "wss://fstream.binance.com/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms",
    "wss://dstream.binance.com/stream?streams=btcusd_perp@depth@100ms/ethusd_perp@depth@100ms/bnbusd_perp@depth@100ms/solusd_perp@depth@100ms/xrpusd_perp@depth@100ms/dogeusd_perp@depth@100ms/adausd_perp@depth@100ms/ltcusd_perp@depth@100ms/avaxusd_perp@depth@100ms/trxusd_perp@depth@100ms/dotusd_perp@depth@100ms/bchusd_perp@depth@100ms/suiusd_perp@depth@100ms",
    "wss://stream.binance.com:443/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/shibusdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade",
    "wss://fstream.binance.com/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade",
    "wss://dstream.binance.com/stream?streams=btcusd_perp@trade/ethusd_perp@trade/bnbusd_perp@trade/solusd_perp@trade/xrpusd_perp@trade/dogeusd_perp@trade/adausd_perp@trade/ltcusd_perp@trade/avaxusd_perp@trade/trxusd_perp@trade/dotusd_perp@trade/bchusd_perp@trade/suiusd_perp@trade"
]

last_messages = [None for _ in links]

async def listen_stream(link_index: int, link: str):
    """
    Łączy się z WebSocketem określonym w 'link'.
    Odbiera wiadomości i zapisuje je w last_messages[link_index].
    """
    global last_messages

    print(f"[{link_index}] Łączenie z {link} ...")
    async with websockets.connect(link) as websocket:
        print(f"[{link_index}] Połączono z {link}")
        try:
            while True:
                message = await websocket.recv()
                # Zapisujemy wiadomość do last_messages
                last_messages[link_index] = message
        except Exception as e:
            print(f"[{link_index}] Wystąpił błąd: {e}")
            return


async def check_keyboard():
    """
    W osobnej pętli asynchronicznej nasłuchuje klawisza 'g'.
    Gdy użytkownik wciśnie 'g', wyświetla ostatnie wiadomości ze wszystkich linków.
    """
    global last_messages
    while True:
        user_input = await asyncio.to_thread(input, "\nWciśnij 'g', aby wyświetlić ostatnie wiadomości (lub Ctrl+C, by przerwać): ")
        if user_input.lower() == 'g':
            for i, msg in enumerate(last_messages):
                if msg is not None:
                    print(f"\n--- Ostatnia wiadomość z link[{i}]: ---\n{msg}")
                else:
                    print(f"\n--- Link[{i}] Brak wiadomości (jeszcze nic nie odebrano). ---")


async def main():
    listen_tasks = [
        asyncio.create_task(listen_stream(idx, link))
        for idx, link in enumerate(links)
    ]

    task_keyboard = asyncio.create_task(check_keyboard())

    await asyncio.gather(*listen_tasks, task_keyboard)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nZatrzymano przez użytkownika.")
