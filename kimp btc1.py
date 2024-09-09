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

# 4. 가격 차이의 절대값 계산
df['abs_price_difference'] = df['price_difference'].abs()

# 5. 가격 차이의 퍼센트 계산 (Binance 기준)
df['percentage_difference'] = (df['price_difference'] / df['close_Binance']) * 100

# 6. 차트 그리기
plt.figure(figsize=(12, 6))

# Bithumb 가격을 기준으로 Binance 가격과의 상대적인 차이 그래프 (절대값 사용)
plt.plot(df.index, df['abs_price_difference'], label='Absolute Price Difference', color='blue')

# Binance 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 2% 미만의 구간을 노란색으로 표시
plt.fill_between(df.index, df['abs_price_difference'],
                 where=(df['percentage_difference'].abs() < 2),
                 color='yellow', alpha=0.3, label='< 2% Difference')

# 5% 이상의 구간을 연두색으로 표시
plt.fill_between(df.index, df['abs_price_difference'],
                 where=(df['percentage_difference'].abs() >= 5),
                 color='lightgreen', alpha=0.5, label='≥ 5% Difference')

# 7. y축 범위 설정: y축을 데이터의 실제 절대값으로 맞추기
plt.ylim([0, df['abs_price_difference'].max() * 1.1])  # 10% 여유 추가

# 8. y축 레이블 포맷 설정: 100만 원 단위로 표시
def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.0fM' % (x * 1e-6)

formatter = FuncFormatter(millions)
plt.gca().yaxis.set_major_formatter(formatter)

# 9. 그래프 설정
plt.title('Absolute Price Difference Between BTC_KRW_Bithumb and BTC_KRW_Binance Prices with Highlighted Ranges')
plt.xlabel('Date')
plt.ylabel('Absolute Price Difference (KRW)')
plt.legend()
plt.grid(True)

# 10. 그래프 보여주기
plt.show()