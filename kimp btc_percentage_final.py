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

# 4. 가격 차이의 백분율 계산 (Binance 기준)
df['percentage_difference'] = (df['price_difference'] / df['close_Binance']) * 100

# 5. Buy/Sell 조건 로직
buy_signals = []
sell_signals = []
signal = None  # 'buy' 또는 'sell'을 기록할 변수

for i in range(len(df)):
    percentage_diff = df['percentage_difference'].iloc[i]

    if signal != 'buy' and percentage_diff < 0:
        # 0 미만일 때 매수 신호
        buy_signals.append(df.index[i])
        signal = 'buy'
    elif signal != 'sell' and percentage_diff > 1:
        # 1% 초과일 때 매도 신호
        sell_signals.append(df.index[i])
        signal = 'sell'

# 6. 차트 그리기
plt.figure(figsize=(12, 6))

# Binance 가격 기준으로의 차이 백분율 그래프
plt.plot(df.index, df['percentage_difference'], label='Percentage Difference (Bithumb - Binance)', color='blue')

# Binance 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 매수 신호 (초록색 점)
plt.scatter(buy_signals, df.loc[buy_signals]['percentage_difference'], color='green', label='Buy (Green)', marker='o')

# 매도 신호 (빨간색 점)
plt.scatter(sell_signals, df.loc[sell_signals]['percentage_difference'], color='red', label='Sell (Red)', marker='o')

# 7. y축 범위 설정
plt.ylim([df['percentage_difference'].min() - 5, df['percentage_difference'].max() + 5])  # 여유 추가

# y축을 절대값으로 그대로 표현 (과학적 표기법 비활성화)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# 8. 그래프 설정
plt.title('Percentage Difference with Buy (Green) and Sell (Red) Signals')
plt.xlabel('Date')
plt.ylabel('Percentage Difference (%)')
plt.legend()
plt.grid(True)

# 9. 그래프 보여주기
plt.show()