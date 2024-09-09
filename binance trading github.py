from binance.client import Client

# Futures Testnet API 키와 시크릿 키 설정
api_key = '386a962c7d9b3ea652a13e54923ac72d54e48be14044a7ad91dcedd66cd33a92'
api_secret = '5a6b83a36bc56f64a5b83baae5da371d2fb57a0dad5b20d5e8b0378bf4ac7467'

# Futures 클라이언트 설정 (Testnet을 사용)
client = Client(api_key, api_secret, testnet=True)
client.FUTURES_API_URL = 'https://testnet.binancefuture.com'


# Futures 주문 함수 (레버리지 2배로 BTCUSDT 1 BTC 시장가 매수)
def futures_trade_btcusdt():
    symbol = 'BTCUSDT'
    quantity = 1  # 1 BTC 매수
    side = 'BUY'  # 매수
    leverage = 4  # 2배 레버리지
    price = '40000'
    order_type = 'LIMIT'  # 시장가 주문

    # 레버리지 설정
    client.futures_change_leverage(symbol=symbol, leverage=leverage)

    # 시장가 주문 제출
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=Client.ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce='GTC'
    )

    print(f"Futures 주문 결과: {order}")
    return order


# 주문 실행
futures_order_response = futures_trade_btcusdt()
print(futures_order_response)