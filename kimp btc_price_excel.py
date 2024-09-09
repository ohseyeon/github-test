import pandas as pd

# 1. CSV 파일에서 데이터 불러오기
binance_file = 'C:/Users/D-syoh/workspace/propbase/data/BTC_KRW_Binance.csv'
bithumb_file = 'C:/Users/D-syoh/workspace/propbase/data/BTC_KRW_Bithumb.csv'

df_binance = pd.read_csv(binance_file, parse_dates=['time'], index_col='time')
df_bithumb = pd.read_csv(bithumb_file, parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_binance, df_bithumb, left_index=True, right_index=True, suffixes=('_Binance', '_Bithumb'))

# 3. 가격 차이 계산
df['price_difference'] = df['close_Bithumb'] - df['close_Binance']

# 4. Buy/Sell 시그널 추출 (Buy 후 Sell 순서 유지)
buy_signals = []
sell_signals = []
signal = None  # 'buy' 또는 'sell'을 기록할 변수

for i in range(1, len(df)):
    price_diff = df['price_difference'].iloc[i]

    if signal != 'buy' and price_diff < 0:
        # Buy 신호: 0 미만일 때
        buy_signals.append({
            'Date': df.index[i],
            'Bithumb Price': df['close_Bithumb'].iloc[i],
            'Binance Price': df['close_Binance'].iloc[i],
            'Price Difference': df['price_difference'].iloc[i]
        })
        signal = 'buy'
    elif signal == 'buy' and price_diff > 1000000:
        # Sell 신호: 1,000,000 초과일 때
        sell_signals.append({
            'Date': df.index[i],
            'Bithumb Price': df['close_Bithumb'].iloc[i],
            'Binance Price': df['close_Binance'].iloc[i],
            'Price Difference': df['price_difference'].iloc[i]
        })
        signal = 'sell'

# 5. Buy와 Sell 신호를 DataFrame으로 변환
buy_df = pd.DataFrame(buy_signals)
sell_df = pd.DataFrame(sell_signals)

# 6. Buy와 Sell 데이터 통합
signal_df = pd.DataFrame({
    'Buy Date': buy_df['Date'],
    'Buy Bithumb Price': buy_df['Bithumb Price'],
    'Buy Binance Price': buy_df['Binance Price'],
    'Buy Price Difference': buy_df['Price Difference'],
    'Sell Date': sell_df['Date'],
    'Sell Bithumb Price': sell_df['Bithumb Price'],
    'Sell Binance Price': sell_df['Binance Price'],
    'Sell Price Difference': sell_df['Price Difference']
})

# 7. Excel 파일로 저장
signal_df.to_excel('buy_sell_signals_correct_order.xlsx', index=False)

print("차트에 표시된 Buy와 Sell 신호가 엑셀 파일로 저장되었습니다.")