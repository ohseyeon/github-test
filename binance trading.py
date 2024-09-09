from binance.client import Client

# Testnet API 키와 시크릿 키 설정 (Futures Testnet)
api_key = '386a962c7d9b3ea652a13e54923ac72d54e48be14044a7ad91dcedd66cd33a92'
api_secret = '5a6b83a36bc56f64a5b83baae5da371d2fb57a0dad5b20d5e8b0378bf4ac7467'

from binance.client import Client

# Futures 클라이언트 설정 (Testnet을 사용)
client = Client(api_key, api_secret)
client.FUTURES_API_URL = 'https://testnet.binancefuture.com'  # Futures Testnet 엔드포인트 설정


def futures_trade(symbol, quantity, side, leverage, order_type='MARKET'):
    """
    Futures 시장에서 주문을 제출하는 함수
    symbol: 거래할 자산 (예: 'BTCUSDT')
    quantity: 매매할 수량
    side: 'BUY' 또는 'SELL'
    leverage: 레버리지 배율
    order_type: 'MARKET' 또는 'LIMIT'
    """
    try:
        # 레버리지 설정
        client.futures_change_leverage(symbol=symbol, leverage=leverage)

        if order_type == 'MARKET':
            # 시장가 주문
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
        elif order_type == 'LIMIT':
            if price is None:
                raise ValueError("지정가 주문 시 price를 지정해야 합니다.")
            # 지정가 주문
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_LIMIT,
                timeInForce=Client.TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
        print(f"Futures 주문 결과: {order}")
        return order
    except Exception as e:
        print(f"Futures 거래 오류: {e}")


# BTCUSDT Futures를 시장가로 1 BTC 매수 (레버리지 2배)
futures_order_response = futures_trade(symbol='BTCUSDT', quantity=1, side='BUY', leverage=2, order_type='MARKET')