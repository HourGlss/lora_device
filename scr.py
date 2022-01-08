import time

led = False


def toggle_led(val: bool) -> None:
    global led
    led = val
    print(f"led is now {val}")


toggle_for = 1
start = None
led_last_off = 0
while True:
    now = time.time()
    if not led and now - led_last_off > toggle_for:
        toggle_led(True)
        start = time.time()

    if led and now - start > toggle_for:
        toggle_led(False)
        led_last_off = now
