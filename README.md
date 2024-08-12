# Time Series Smoothings

This repository contains Python classes for calculating time series smoothings (Moving Averages and Exponential Moving Averages) in real time. The data is stored as `(timestamp, value)` tuples in a deque, allowing for efficient calculation and time-window-based operations.

## Features

- **Moving Average (MA)**: 
  - Calculates the simple moving average over a specified time window in seconds.
  - Automatically manages the data to keep only relevant data within the time window.
  
- **Exponential Moving Average (EMA)**: 
  - Computes the exponential moving average, which gives more weight to recent data points.
  - Applying the decay factor based on the time difference from last relevant entry.

## Usage

```python
from moving_average import MovingAverage, ExponentialMovingAverage

# Initialize with a 60-second window
ma = MovingAverage(window_in_seconds=60)
current_ma = ma.current(value)

# Initialize with a 120-second window for EMA
ema = ExponentialMovingAverage(window=120)
current_ema = ema.current(value)
