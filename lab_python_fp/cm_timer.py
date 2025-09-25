import time
from contextlib import contextmanager

# Контекстный менеджер на основе класса
class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"time: {end - self.start:.3f}")

# Контекстный менеджер с использованием contextlib
@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"time: {end - start:.3f}")
