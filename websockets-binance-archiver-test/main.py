
import asyncio
import websockets
links = [
    "wss://stream.binance.com:443/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms/aptusdt@depth@100ms/sandusdt@depth@100ms/algousdt@depth@100ms/aaveusdt@depth@100ms/axsusdt@depth@100ms/maskusdt@depth@100ms/linkusdt@depth@100ms/atomusdt@depth@100ms/filusdt@depth@100ms/etcusdt@depth@100ms/opusdt@depth@100ms/dydxusdt@depth@100ms/galausdt@depth@100ms/apeusdt@depth@100ms/nearusdt@depth@100ms/arbusdt@depth@100ms/uniusdt@depth@100ms/eosusdt@depth@100ms/chzusdt@depth@100ms/sushiusdt@depth@100ms/1inchusdt@depth@100ms/grtusdt@depth@100ms/crvusdt@depth@100ms/cakeusdt@depth@100ms/xlmusdt@depth@100ms/runeusdt@depth@100ms/minausdt@depth@100ms/ldousdt@depth@100ms/stxusdt@depth@100ms/snxusdt@depth@100ms/kavausdt@depth@100ms/fetusdt@depth@100ms/rlcusdt@depth@100ms/ontusdt@depth@100ms/icxusdt@depth@100ms/hotusdt@depth@100ms/belusdt@depth@100ms",
    "wss://fstream.binance.com/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms/aptusdt@depth@100ms/sandusdt@depth@100ms/algousdt@depth@100ms/aaveusdt@depth@100ms/axsusdt@depth@100ms/maskusdt@depth@100ms/linkusdt@depth@100ms/atomusdt@depth@100ms/filusdt@depth@100ms/etcusdt@depth@100ms/opusdt@depth@100ms/dydxusdt@depth@100ms/galausdt@depth@100ms/apeusdt@depth@100ms/nearusdt@depth@100ms/arbusdt@depth@100ms/uniusdt@depth@100ms/eosusdt@depth@100ms/chzusdt@depth@100ms/sushiusdt@depth@100ms/1inchusdt@depth@100ms/grtusdt@depth@100ms/crvusdt@depth@100ms/cakeusdt@depth@100ms/xlmusdt@depth@100ms/runeusdt@depth@100ms/minausdt@depth@100ms/ldousdt@depth@100ms/stxusdt@depth@100ms/snxusdt@depth@100ms/kavausdt@depth@100ms/fetusdt@depth@100ms/rlcusdt@depth@100ms/ontusdt@depth@100ms/icxusdt@depth@100ms/hotusdt@depth@100ms/belusdt@depth@100ms",
    "wss://dstream.binance.com/stream?streams=aaveusd_perp@depth@100ms/adausd_perp@depth@100ms/algousd_perp@depth@100ms/aptusd_perp@depth@100ms/atomusd_perp@depth@100ms/avaxusd_perp@depth@100ms/axsusd_perp@depth@100ms/bchusd_perp@depth@100ms/bnbusd_perp@depth@100ms/btcusd_perp@depth@100ms/chzusd_perp@depth@100ms/dogeusd_perp@depth@100ms/dotusd_perp@depth@100ms/eosusd_perp@depth@100ms/etcusd_perp@depth@100ms/ethusd_perp@depth@100ms/filusd_perp@depth@100ms/linkusd_perp@depth@100ms/ltcusd_perp@depth@100ms/nearusd_perp@depth@100ms/opusd_perp@depth@100ms/runeusd_perp@depth@100ms/sandusd_perp@depth@100ms/solusd_perp@depth@100ms/suiusd_perp@depth@100ms/trxusd_perp@depth@100ms/uniusd_perp@depth@100ms/xlmusd_perp@depth@100ms/xrpusd_perp@depth@100ms",
    "wss://stream.binance.com:443/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade/aptusdt@trade/sandusdt@trade/algousdt@trade/aaveusdt@trade/axsusdt@trade/maskusdt@trade/linkusdt@trade/atomusdt@trade/filusdt@trade/etcusdt@trade/opusdt@trade/dydxusdt@trade/galausdt@trade/apeusdt@trade/nearusdt@trade/arbusdt@trade/uniusdt@trade/eosusdt@trade/chzusdt@trade/sushiusdt@trade/1inchusdt@trade/grtusdt@trade/crvusdt@trade/cakeusdt@trade/xlmusdt@trade/runeusdt@trade/minausdt@trade/ldousdt@trade/stxusdt@trade/snxusdt@trade/kavausdt@trade/fetusdt@trade/rlcusdt@trade/ontusdt@trade/icxusdt@trade/hotusdt@trade/belusdt@trade",
    "wss://fstream.binance.com/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade/aptusdt@trade/sandusdt@trade/algousdt@trade/aaveusdt@trade/axsusdt@trade/maskusdt@trade/linkusdt@trade/atomusdt@trade/filusdt@trade/etcusdt@trade/opusdt@trade/dydxusdt@trade/galausdt@trade/apeusdt@trade/nearusdt@trade/arbusdt@trade/uniusdt@trade/eosusdt@trade/chzusdt@trade/sushiusdt@trade/1inchusdt@trade/grtusdt@trade/crvusdt@trade/cakeusdt@trade/xlmusdt@trade/runeusdt@trade/minausdt@trade/ldousdt@trade/stxusdt@trade/snxusdt@trade/kavausdt@trade/fetusdt@trade/rlcusdt@trade/ontusdt@trade/icxusdt@trade/hotusdt@trade/belusdt@trade",
    "wss://dstream.binance.com/stream?streams=aaveusd_perp@trade/adausd_perp@trade/algousd_perp@trade/aptusd_perp@trade/atomusd_perp@trade/avaxusd_perp@trade/axsusd_perp@trade/bchusd_perp@trade/bnbusd_perp@trade/btcusd_perp@trade/chzusd_perp@trade/dogeusd_perp@trade/dotusd_perp@trade/eosusd_perp@trade/etcusd_perp@trade/ethusd_perp@trade/filusd_perp@trade/linkusd_perp@trade/ltcusd_perp@trade/nearusd_perp@trade/opusd_perp@trade/runeusd_perp@trade/sandusd_perp@trade/solusd_perp@trade/suiusd_perp@trade/trxusd_perp@trade/uniusd_perp@trade/xlmusd_perp@trade/xrpusd_perp@trade"
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
