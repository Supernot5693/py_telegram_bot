import ccxt
import pandas as pd

def GetOhlcv(binance, Ticker, period):
    btc_ohlcv = binance.fetch_ohlcv(Ticker, period)
    df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    return df

def FindEma(source, length):
    ep = 2/(length+1)
    ema = ep * source + (1-ep) * ema

def FindA4(clo, fLen, sLen):
    return a4

#거래할 코인 티커와 심볼
Target_Coin_Ticker = "BTC/USDT"
Target_Coin_Symbol = "BTCUSDT"

binanceX = ccxt.binance()

df_15 = GetOhlcv(binanceX,Target_Coin_Ticker, '15m')

eema = df_15['close'].ewm(26).mean()

print(eema)

close = df_15['close']
tLength = 20
fastLength = 26
slowLength = 50
