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

# Zmienna globalna, w której przechowujemy ostatnio odebraną wiadomość
last_message = None

async def listen_depth_stream():
    """
    Łączy się z WebSocketem Binance Futures,
    odbiera wiadomości i zapisuje je w globalnej zmiennej last_message.
    """
    global last_message
    print("Łączenie z Binance Futures WebSocket...")
    async with websockets.connect(BINANCE_FUTURES_DEPTH_URL) as websocket:
        print("Połączono z Binance Futures WebSocket.")
        try:
            while True:
                message = await websocket.recv()
                # Zapisujemy wiadomość do zmiennej globalnej
                last_message = message
        except Exception as e:
            print(f"\nWystąpił błąd: {e}")
            return

async def check_keyboard():
    """
    W osobnej pętli asynchronicznej nasłuchuje klawisza.
    Gdy użytkownik wciśnie 'g', wyświetla ostatnią wiadomość.
    """
    global last_message
    while True:
        # Czekamy, aż user wpisze coś w stdin (nie blokujemy głównej pętli)
        user_input = await asyncio.to_thread(input, "\nWciśnij 'g', aby wyświetlić ostatnią wiadomość (lub Ctrl+C, by przerwać): ")
        if user_input.lower() == 'g':
            if last_message is not None:
                print(f"Ostatnia wiadomość: {last_message}")
            else:
                print("Brak wiadomości (jeszcze nic nie odebrano).")

async def main():
    # Tworzymy dwie współbieżne (asynchroniczne) zadania:
    task_listen = asyncio.create_task(listen_depth_stream())
    task_keyboard = asyncio.create_task(check_keyboard())

    # Uruchamiamy je równolegle do czasu, aż któreś zakończy się wyjątkiem
    await asyncio.gather(task_listen, task_keyboard)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nZatrzymano przez użytkownika.")
