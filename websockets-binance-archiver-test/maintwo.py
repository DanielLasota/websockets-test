import threading
import time
from websocket import WebSocketApp

# Lista 6 linków (tak jak w pytaniu)
links = [
    "wss://stream.binance.com:443/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/shibusdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms",
    "wss://fstream.binance.com/stream?streams=btcusdt@depth@100ms/ethusdt@depth@100ms/bnbusdt@depth@100ms/solusdt@depth@100ms/xrpusdt@depth@100ms/dogeusdt@depth@100ms/adausdt@depth@100ms/ltcusdt@depth@100ms/avaxusdt@depth@100ms/trxusdt@depth@100ms/dotusdt@depth@100ms/bchusdt@depth@100ms/suiusdt@depth@100ms",
    "wss://dstream.binance.com/stream?streams=btcusd_perp@depth@100ms/ethusd_perp@depth@100ms/bnbusd_perp@depth@100ms/solusd_perp@depth@100ms/xrpusd_perp@depth@100ms/dogeusd_perp@depth@100ms/adausd_perp@depth@100ms/ltcusd_perp@depth@100ms/avaxusd_perp@depth@100ms/trxusd_perp@depth@100ms/dotusd_perp@depth@100ms/bchusd_perp@depth@100ms/suiusd_perp@depth@100ms",
    "wss://stream.binance.com:443/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/shibusdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade",
    "wss://fstream.binance.com/stream?streams=btcusdt@trade/ethusdt@trade/bnbusdt@trade/solusdt@trade/xrpusdt@trade/dogeusdt@trade/adausdt@trade/ltcusdt@trade/avaxusdt@trade/trxusdt@trade/dotusdt@trade/bchusdt@trade/suiusdt@trade",
    "wss://dstream.binance.com/stream?streams=btcusd_perp@trade/ethusd_perp@trade/bnbusd_perp@trade/solusd_perp@trade/xrpusd_perp@trade/dogeusd_perp@trade/adausd_perp@trade/ltcusd_perp@trade/avaxusd_perp@trade/trxusd_perp@trade/dotusd_perp@trade/bchusd_perp@trade/suiusd_perp@trade"
]

# Globalna lista do przechowywania ostatnich wiadomości z każdego linku
last_messages = [None] * len(links)

# Flaga do zatrzymania wątków (kiedy użytkownik przerwie program Ctrl+C)
stop_threads = False


def on_message(ws, message, link_index):
    """
    Funkcja wywoływana za każdym razem, gdy z linku link_index przyjdzie nowa wiadomość.
    """
    global last_messages
    last_messages[link_index] = message


def on_error(ws, error, link_index):
    """
    Funkcja wywoływana w razie wystąpienia błędu.
    """
    print(f"[{link_index}] Wystąpił błąd: {error}")


def on_close(ws, close_status_code, close_msg, link_index):
    """
    Wywoływana przy zamknięciu połączenia WebSocket (np. z powodu błędu).
    """
    print(f"[{link_index}] Zamykanie połączenia, kod={close_status_code}, msg={close_msg}")


def on_open(ws, link_index):
    """
    Wywoływana po udanym otwarciu połączenia WebSocket.
    """
    print(f"[{link_index}] Połączono z {links[link_index]}")


def run_ws_app(link_index, link):
    """
    Tworzy obiekt WebSocketApp z podpiętymi callbackami,
    a następnie uruchamia go w pętli (run_forever).
    """
    ws_app = WebSocketApp(
        link,
        on_open    = lambda ws: on_open(ws, link_index),
        on_message = lambda ws, msg: on_message(ws, msg, link_index),
        on_error   = lambda ws, err: on_error(ws, err, link_index),
        on_close   = lambda ws, code, msg: on_close(ws, code, msg, link_index)
    )

    # Uruchamiamy pętlę odbierającą komunikaty tak długo, aż wątek nie zostanie przerwany
    while not stop_threads:
        # run_forever() zwraca, gdy połączenie się zamknie lub wystąpi błąd
        ws_app.run_forever()
        # Możemy dać krótki 'sleep', by nie wchodzić w pętlę spinującą w razie rozłączeń
        time.sleep(1)


def main():
    global stop_threads

    # Utworzymy listę wątków, każdy wątek będzie obsługiwał inny link
    threads = []
    for i, link in enumerate(links):
        t = threading.Thread(target=run_ws_app, args=(i, link), daemon=True)
        t.start()
        threads.append(t)

    print("Naciśnij 'g', by wyświetlić ostatnie wiadomości; Ctrl+C, aby zakończyć.")
    try:
        while True:
            user_input = input()
            if user_input.lower() == 'g':
                for i, msg in enumerate(last_messages):
                    if msg is not None:
                        print(f"\n--- Ostatnia wiadomość z link[{i}]: ---\n{msg}")
                    else:
                        print(f"\n--- Link[{i}] Brak wiadomości (jeszcze nic nie odebrano). ---")
    except KeyboardInterrupt:
        print("\nZatrzymano przez użytkownika.")
    finally:
        # Ustawiamy flagę stopu i czekamy, aż wątki się zakończą
        stop_threads = True
        for t in threads:
            t.join()


if __name__ == "__main__":
    main()
