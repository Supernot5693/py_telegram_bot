import pyupbit

# 비트코인 현재가 조회
# btcPrice = pyupbit.get_current_price("KRW-BTC")
# print(btcPrice)

# 여러코인 현재가 조회
# coinPrices = pyupbit.get_current_price(["KRW-BTC", "KRW-XRP", "BTC-XRP"])
# print(coinPrices)

# 비트코인 일봉 데이터 조회
df = pyupbit.get_ohlcv("KRW-BTC")

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
df['range'] = (df['high'] - df['low']) * 0.5

# 목표가 계산 
# df[‘range’].shift(1)을 통해 ‘range’ 컬럼의 값을 1행 내려준 후 df[‘open’] 컬럼과 더하고 그 결괏값을 ‘target’ 이라는 컬럼으로 저장한다.
# 목표가 계산은 각 거래일을 기준으로 전날의 레인지를 사용하기 때문에 ‘range’ 컬럼을 1행씩 내려준다.
# shift(1)  데이터를 한 행 밑으로 내림
# shift(-1) 데이터를 한 행 위로 올림
df['range_shift1'] = df['range'].shift(1)
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel("btc.xlsx")
