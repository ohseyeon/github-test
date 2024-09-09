import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일에서 데이터를 불러오기
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 가격 차이 계산
df['price_difference'] = df['close_USDT'] - df['close_USD']

# 4. 월별 기준 가격 계산 (매월 1일의 종가, 2023년 12월은 7일의 종가)
monthly_baseline_usdt = df['close_USDT'].resample('MS').first()
monthly_baseline_usd = df['close_USD'].resample('MS').first()
december_2023_baseline_usdt = df.loc['2023-12-07', 'close_USDT']
december_2023_baseline_usd = df.loc['2023-12-07', 'close_USD']
monthly_baseline_usdt.loc['2023-12-01'] = december_2023_baseline_usdt
monthly_baseline_usd.loc['2023-12-01'] = december_2023_baseline_usd

# 5. 기준 가격을 0으로 잡고 변동값 계산 (파란색 점선)
df['monthly_adjusted_usdt'] = df['close_USDT'] - df.index.to_series().map(lambda x: monthly_baseline_usdt.get(x.replace(day=1), december_2023_baseline_usdt))
df['monthly_adjusted_usd'] = df['close_USD'] - df.index.to_series().map(lambda x: monthly_baseline_usd.get(x.replace(day=1), december_2023_baseline_usd))

# 6. 보라색 선의 계산 (노란색 점선 + 파란색 점선)
df['combined'] = df['monthly_adjusted_usdt'] - df['monthly_adjusted_usd']

# 7. 차트 그리기
plt.figure(figsize=(12, 6))

# 파란색 점선 (월별 기준으로 재계산된 USDT/KRW)
plt.plot(df.index, df['monthly_adjusted_usdt'], label='Monthly Adjusted USDT/KRW', color='blue', linestyle='dotted')

# 노란색 점선 (USD/KRW의 월별 변동)
plt.plot(df.index, df['monthly_adjusted_usd'], label='Monthly Adjusted USD/KRW', color='orange', linestyle='dotted')

# 보라색 선 (파란색 점선과 노란색 점선의 합)
plt.plot(df.index, df['combined'], label='Combined (USDT Adjusted - USD Adjusted)', color='purple')

# -20과 20 위치에 가로 점선 추가
plt.axhline(-20, color='red', linestyle='dotted', linewidth=1.5, label='-20 Level')
plt.axhline(20, color='orange', linestyle='dotted', linewidth=1.5, label='20 Level')

# 8. 보라색 선과 점선의 교차점에 작은 빨간 점 표시
cross_points = df[(df['combined'] <= -20) | (df['combined'] >= 20)]

# 진한 빨간색 작은 점 표시
plt.scatter(cross_points.index, cross_points['combined'], color='darkred', s=50, zorder=5)

# 그래프 설정
plt.title('Monthly Adjusted USDT/KRW and USD/KRW with Combined Value')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.legend()
plt.grid(True)

# 그래프 보여주기
plt.show()