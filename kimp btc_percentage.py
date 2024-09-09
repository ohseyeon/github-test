import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

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

# 5. 차트 그리기
plt.figure(figsize=(12, 6))

# Bithumb 가격과 Binance 가격 차이의 백분율 그래프
plt.plot(df.index, df['percentage_difference'], label='Percentage Difference', color='blue')

# Binance 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 2% 미만의 구간을 노란색으로 표시
plt.fill_between(df.index, df['percentage_difference'],
                 where=(df['percentage_difference'].abs() < 2),
                 color='yellow', alpha=0.3, label='< 2% Difference')

# 5% 이상의 구간을 연두색으로 표시
plt.fill_between(df.index, df['percentage_difference'],
                 where=(df['percentage_difference'].abs() >= 5),
                 color='lightgreen', alpha=0.5, label='≥ 5% Difference')

# 6. y축 범위 설정: 적절한 범위로 설정
plt.ylim([df['percentage_difference'].min() - 5, df['percentage_difference'].max() + 5])  # 여유 추가

# 7. 그래프 설정
plt.title('Percentage Difference Between BTC_KRW_Bithumb and BTC_KRW_Binance Prices with Highlighted Ranges')
plt.xlabel('Date')
plt.ylabel('Percentage Difference (%)')
plt.legend()
plt.grid(True)

# 8. 그래프 보여주기
plt.show()