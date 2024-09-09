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

# 8. 매수 및 매도 시점 찾기
buy_dates = []
sell_dates = []

# 매수 및 매도 시점을 찾기 위한 이전 매수 시점을 저장
last_buy_date = None

for i in range(len(df)):
    current_date = df.index[i]
    percentage_diff = df['percentage_difference'].iloc[i]

    if percentage_diff < 2:
        # 매수 조건
        last_buy_date = current_date

    if last_buy_date and percentage_diff >= 5:
        # 매도 조건
        if (current_date - last_buy_date).days <= 7:
            buy_dates.append(last_buy_date)
            sell_dates.append(current_date)
        last_buy_date = None

# 9. 차트 그리기
plt.figure(figsize=(12, 6))

# 파란색 점선: USDT/KRW와 USD/KRW의 차이
plt.plot(df.index, df['price_difference'], label='USDT/KRW - USD/KRW Difference', color='blue', linestyle='--')

# 주황색 점선: 기준 가격 조정된 USD/KRW
plt.plot(df.index, df['usd_adjusted'], label='USD/KRW Adjusted (Relative to 2023-12-07)', color='orange', linestyle='--')

# 빨간색 실선: 주황색 점선과 파란색 선의 합
plt.plot(df.index, df['combined'], label='Combined (Orange + Blue)', color='red', linestyle='-', linewidth=2)

# 매수 및 매도 시점을 그래프에 점으로 표시
plt.scatter(buy_dates, df.loc[buy_dates]['combined'], color='black', label='Buy Signal', zorder=5)
plt.scatter(sell_dates, df.loc[sell_dates]['combined'], color='grey', label='Sell Signal', zorder=5)

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
plt.title('Difference Between USDT/KRW and USD/KRW Prices with Highlighted Ranges and Adjusted USD/KRW')
plt.xlabel('Date')
plt.ylabel('Price Difference / Adjusted USD/KRW')
plt.legend()
plt.grid(True)

# 그래프 보여주기
plt.show()