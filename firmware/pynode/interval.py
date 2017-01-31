from machine import Timer

_timer = Timer(-1)

_timers = []

INTERVAL = 100 # ms


def add(name: str, f: callable, interval: int):
    _timers.append({
        'name': name,
        'f': f,
        'interval': interval,
        'current': 0
    })


def start():
    _timer.init(period=INTERVAL, mode=Timer.PERIODIC, callback=__iteration)


def stop():
    _timer.deinit()


def __iteration(data):
    for timer in _timers:
        timer['current'] += INTERVAL
        if timer['current'] >= timer['interval']:
            timer['current'] = 0
            timer['f']()
