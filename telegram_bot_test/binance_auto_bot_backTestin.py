import ccxt
import pandas as pd

#분봉/일봉 캔들 정보를 가져온다 첫번째: 바이낸스 객체, 두번째: 코인 티커, 세번째: 기간 (1d,4h,1h,15m,10m,1m ...)
def GetOhlcv(binance, Ticker, period):
    btc_ohlcv = binance.fetch_ohlcv(Ticker, period)
    df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    return df

#RSI지표 수치를 구해준다. 첫번째: 분봉/일봉 정보, 두번째: 기간, 세번째: 기준 날짜
def GetRSI(ohlcv,period,st):
    ohlcv["close"] = ohlcv["close"]
    delta = ohlcv["close"].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    _gain = up.ewm(com=(period - 1), min_periods=period).mean()
    _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    RS = _gain / _loss
    return float(pd.Series(100 - (100 / (1 + RS)), name="RSI").iloc[st])

def GetRSI_2(ohlcv):
    print("RSI7:  ",GetRSI(ohlcv, 7, -3), "->",GetRSI(ohlcv, 7, -2), "->",GetRSI(ohlcv, 7, -1))
    print("RSI14: ",GetRSI(ohlcv, 14, -3), "->",GetRSI(ohlcv, 14, -2), "->",GetRSI(ohlcv, 14, -1))
    print("RSI21: ",GetRSI(ohlcv, 21, -3), "->",GetRSI(ohlcv, 21, -2), "->",GetRSI(ohlcv, 21, -1))
    print("RES7_21 : ", GetRSI(ohlcv, 7, -1) - GetRSI(ohlcv, 21, -1))

def GetGainLoss(delta, period):
    

def GetRSIToBackTesting(ohlcv):
    ohlcv["close"] = ohlcv["close"]
    delta = ohlcv["close"].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0 
    down[down > 0] = 0
    _gain = up.ewm(com=(period - 1), min_periods=period).mean()
    _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    RS = _gain / _loss
    ohicv['rsi7'] = 
    return float(pd.Series(100 - (100 / (1 + RS)), name="RSI").iloc[st])
    ohicv.to_excel('rsi.xlsx')    

#거래할 코인 티커와 심볼
Target_Coin_Ticker = "BTC/USDT"
Target_Coin_Symbol = "BTCUSDT"

binanceX = ccxt.binance()

df_15 = GetOhlcv(binanceX,Target_Coin_Ticker, '15m')

GetRSI(df_15, 7, -1)

