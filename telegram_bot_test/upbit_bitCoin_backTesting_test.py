import pyupbit
import numpy as np

# 비트코인 현재가 조회
# btcPrice = pyupbit.get_current_price("KRW-BTC")
# print(btcPrice)

# 여러코인 현재가 조회
# coinPrices = pyupbit.get_current_price(["KRW-BTC", "KRW-XRP", "BTC-XRP"])
# print(coinPrices)

# 비트코인 일봉 데이터 조회
# df = pyupbit.get_ohlcv("KRW-BTC")
# 2018년도만 조회
# df = df['2018']

# 5줄만 조회
#print(df.tail(5))

# 조회정보 엑셀 저장
# df.to_excel("btc.xlsx")

# 호가 조회
# orderBook = pyupbit.get_orderbook("KRW-BTC")
# print(orderBook)

# bids_asks = orderBook['orderbook_units']

# for bids_ask in bids_asks:
    # print(bids_ask)


## 변동성 돌파 벡테스팅
# 레인지 계산
# df['range'] = (df['high'] - df['low']) * 0.5

# 목표가 계산 
# df[‘range’].shift(1)을 통해 ‘range’ 컬럼의 값을 1행 내려준 후 df[‘open’] 컬럼과 더하고 그 결괏값을 ‘target’ 이라는 컬럼으로 저장한다.
# 목표가 계산은 각 거래일을 기준으로 전날의 레인지를 사용하기 때문에 ‘range’ 컬럼을 1행씩 내려준다.
# shift(1)  데이터를 한 행 밑으로 내림
# shift(-1) 데이터를 한 행 위로 올림
# df['range_shift1'] = df['range'].shift(1)
# df['target'] = df['open'] + df['range'].shift(1)

# 수수료(임시)
#fee = 0.0032

# 매수,매도 했을시 수익률 (수수료,기타 제외)
# df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

# 누적 수익률
# totRor = df['ror'].cumprod()[-2]
# print(totRor)
# df.to_excel("btc.xlsx")

## 수익률 함수
# def get_ror(k=0.5):
#     df = pyupbit.get_ohlcv("KRW-BTC")

#     fee = 0.0032
#     df['range'] = (df['high'] - df['low']) * k
#     df['target'] = df['open'] + df['range'].shift(1)
#     df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

#     totRor = df['ror'].cumprod()[-2]
#     return totRor

# # 최적 K값 계산
# for k in np.arange(0.1, 1.0, 0.1):
#     totRor = get_ror(k)
#     print("%.1f %f" % (k, totRor))

df = pyupbit.get_ohlcv("KRW-BTC")
df = df.loc['2018']

df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['bull'] = df['open'] > df['ma5']

fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                    df['close'] / df['target'] - fee,
                    1)

df['hpr'] = df['ror'].cumprod()
df['mdd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['mdd'].max())
print("HPR(%): ", df['hpr'][-2])
df.to_excel("btc.xlsx")
