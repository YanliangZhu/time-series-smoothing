from collections import deque
from datetime import datetime, timedelta

class MovingAverage:
    def __init__(self, window_in_seconds=60):
        self.window = window_in_seconds
        self.data = deque()  # Store (timestamp, value) tuples

    def current(self, value):
        now = datetime.now()
        self.data.append((now, value))
        return self.get_moving_average(now=now)
    
    def get_moving_average(self, now=None):
        if not self.data:
            return 0
        else:
            now = datetime.now() if now is None else now
            while self.data and self.data[0][0] < now - timedelta(seconds=self.window):
                self.data.popleft()
            total = sum(entry[1] for entry in self.data)
            entries = len(self.data)
            return total / entries


class ExponentialMovingAverage:
    def __init__(self, window=120):
        self.window = window
        self.data = deque()  # Store (timestamp, value) tuples
        self.decay = 2 / (window + 1)

    def current(self, value):
        now = datetime.now()
        self.data.append((now, value))
        return self.get_exponential_moving_average(now=now)
    
    def get_exponential_moving_average(self, now=None):
        if not self.data:
            return 0
        else:
            now = datetime.now() if now is None else now
            while self.data and self.data[0][0] < now - timedelta(seconds=self.window):
                self.data.popleft()
            ema = self.data[0][1]
            for i in range(1, len(self.data)):
                timestamp_0, value_0 = self.data[i-1]
                timestamp_1, value_1 = self.data[i]
                time_diff = (timestamp_1 - timestamp_0).total_seconds()
                decay_i = 1 - pow(1 - self.decay, time_diff/1)
            ema = decay_i * value_1 + (1 - decay_i) * ema
            return ema