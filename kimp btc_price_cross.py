import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# 1. CSV 파일에서 데이터 불러오기
binance_file = 'C:/Users/D-syoh/workspace/propbase/data/BTC_KRW_Binance.csv'
bithumb_file = 'C:/Users/D-syoh/workspace/propbase/data/BTC_KRW_Bithumb.csv'

df_binance = pd.read_csv(binance_file, parse_dates=['time'], index_col='time')
df_bithumb = pd.read_csv(bithumb_file, parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_binance, df_bithumb, left_index=True, right_index=True, suffixes=('_Binance', '_Bithumb'))

# 3. 가격 차이 계산
df['price_difference'] = df['close_Bithumb'] - df['close_Binance']

# 4. Buy/Sell 조건 로직
buy_signals = []
sell_signals = []
signal = None  # 'buy' 또는 'sell'을 기록할 변수

for i in range(len(df)):
    price_diff = df['price_difference'].iloc[i]

    if signal != 'buy' and price_diff < 0:
        # 0 미만일 때 매수 신호
        buy_signals.append(df.index[i])
        signal = 'buy'
    elif signal != 'sell' and price_diff > 1000000:
        # 1,000,000 초과일 때 매도 신호
        sell_signals.append(df.index[i])
        signal = 'sell'

# 5. 차트 그리기
plt.figure(figsize=(12, 6))

# Bithumb 가격과 Binance 가격 차이의 절대값 그래프
plt.plot(df.index, df['price_difference'], label='Price Difference (Bithumb - Binance)', color='blue')

# Binance 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 매수 신호 (초록색 점)
plt.scatter(buy_signals, df.loc[buy_signals]['price_difference'], color='green', label='Buy (Green)', marker='o')

# 매도 신호 (빨간색 점)
plt.scatter(sell_signals, df.loc[sell_signals]['price_difference'], color='red', label='Sell (Red)', marker='o')

# 6. y축 범위 설정
plt.ylim([df['price_difference'].min() - 500, df['price_difference'].max() + 500])  # 여유 추가

# y축을 절대값으로 그대로 표현 (과학적 표기법 비활성화)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# 7. 그래프 설정
plt.title('Absolute Price Difference with Buy (Green) and Sell (Red) Signals')
plt.xlabel('Date')
plt.ylabel('Price Difference (KRW)')
plt.legend()
plt.grid(True)

# 8. 그래프 보여주기
plt.show()