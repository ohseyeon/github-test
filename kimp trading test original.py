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

# 5. 기준 날짜 설정
baseline_date = '2023-12-07'
baseline_price_usd = df.loc[baseline_date, 'close_USD']

# 6. 기준 가격을 0으로 잡고 변동값 계산
df['usd_adjusted'] = df['close_USD'] - baseline_price_usd

# 7. 빨간색 실선: 주황색 점선 데이터와 파란색 선의 합
df['combined'] = df['price_difference'] + df['usd_adjusted']

# 시그널 초기화
buy_signal_given = False
sell_signal_given = False

buy_dates = []
sell_dates = []

# 시그널 결정
for i in range(1, len(df)):
    if df['price_difference'].iloc[i] < 25 and not buy_signal_given and (not sell_signal_given or sell_signal_given):
        buy_dates.append(df.index[i])
        buy_signal_given = True
        sell_signal_given = False
    elif df['price_difference'].iloc[i] >= 50 and not sell_signal_given and buy_signal_given:
        sell_dates.append(df.index[i])
        sell_signal_given = True
        buy_signal_given = False

# 8. 차트 그리기
plt.figure(figsize=(12, 6))

# 파란색 점선: USDT/KRW와 USD/KRW의 차이
plt.plot(df.index, df['price_difference'], label='USDT/KRW - USD/KRW Difference', color='blue', linestyle='--')

# 주황색 점선: 기준 가격 조정된 USD/KRW
plt.plot(df.index, df['usd_adjusted'], label='USD/KRW Adjusted (Relative to 2023-12-07)', color='orange', linestyle='--')

# 빨간색 실선: 주황색 점선과 파란색 선의 합
plt.plot(df.index, df['combined'], label='Combined (Orange + Blue)', color='red', linestyle='-', linewidth=2)

# 연두색 영역: 파란색 점선이 25 미만일 때
plt.fill_between(df.index, df['price_difference'], 25, where=(df['price_difference'] < 25), color='lightgreen', alpha=0.5, label='< 25')

# 연한 빨간색 영역: 파란색 점선이 50 이상일 때
plt.fill_between(df.index, df['price_difference'], 50, where=(df['price_difference'] >= 50), color='lightcoral', alpha=0.5, label='≥ 50')

# USD/KRW 가격을 기준으로 원점 선 (0 차이선)
plt.axhline(0, color='red', linestyle='--', label='0 Difference Line')

# 그래프 설정
plt.title('Buy/Sell Signals Based on Combined Price Difference and Adjusted USD/KRW')
plt.xlabel('Date')
plt.ylabel('Price Difference / Adjusted USD/KRW')
plt.legend()
plt.grid(True)

# 그래프 보여주기
plt.show()