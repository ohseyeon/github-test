import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일에서 데이터를 불러오기
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 가격 차이 계산
df['price_difference'] = df['close_USDT'] - df['close_USD']

# 4. 가격 차이의 퍼센트 계산 (원화 기준)
df['percentage_difference'] = (df['price_difference'] / df['close_USD']) * 100

# 5. 월별 기준 가격 계산 (매월 1일의 종가, 2023년 12월은 7일의 종가)
monthly_baseline = df['close_USD'].resample('MS').first()
december_2023_baseline = df.loc['2023-12-07', 'close_USD']
monthly_baseline.loc['2023-12-01'] = december_2023_baseline

# 6. 기준 가격을 0으로 잡고 변동값 계산
df['monthly_adjusted'] = df['close_USD'] - df.index.to_series().map(lambda x: monthly_baseline.get(x.replace(day=1), december_2023_baseline))

# 7. 노란색 점선과 파란색 선의 합을 계산
df['combined'] = df['price_difference'] + df['monthly_adjusted']

# 8. 차트 그리기
plt.figure(figsize=(12, 6))

# 파란색 점선 (USDT/KRW와 USD/KRW의 차이)
plt.plot(df.index, df['price_difference'], label='USDT/KRW - USD/KRW Difference', color='blue', linestyle='dotted')

# 노란색 점선 (USD/KRW의 월별 변동)
plt.plot(df.index, df['monthly_adjusted'], label='Monthly Adjusted USD/KRW', color='orange', linestyle='dotted')

# 보라색 선 (파란색 점선과 노란색 점선의 합)
plt.plot(df.index, df['combined'], label='Combined (USDT Difference + Monthly Adjusted)', color='purple')

# USD/KRW 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 2% 미만의 구간을 노란색으로 표시
plt.fill_between(df.index, df['price_difference'],
                 where=(df['percentage_difference'].abs() < 2),
                 color='yellow', alpha=0.3, label='< 2% Difference')

# 5% 이상의 구간을 연두색으로 표시
plt.fill_between(df.index, df['price_difference'],
                 where=(df['percentage_difference'].abs() >= 5),
                 color='lightgreen', alpha=0.5, label='≥ 5% Difference')

# 그래프 설정
plt.title('Difference Between USDT/KRW and USD/KRW Prices with Monthly Adjusted USD/KRW')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.legend()
plt.grid(True)

# 그래프 보여주기
plt.show()