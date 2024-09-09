from binance.client import Client

# 바이낸스 API 키와 시크릿 키 설정
api_key = '4j3YSqgrbZrpu2palBKi6IOSiI8MJNpH29Y4nE6ojg5jwSk5460NNDa75oYK4KUK'
api_secret = 'XQdxZrrlF5gt2STzUQDZPib6J79yZgXc8JykWb1if36g0Rxaa4bx9XmNRZYcGV8O'

# 클라이언트 객체 생성
client = Client(api_key, api_secret)

# 시세를 받아올 거래쌍 설정 (예: BTC/USDT)
symbol = 'BTCUSDT'

# 현재 시세 받아오기
ticker = client.get_symbol_ticker(symbol=symbol)

# 결과 출력
print(f"Symbol: {ticker['symbol']}")
print(f"Price: {ticker['price']}")