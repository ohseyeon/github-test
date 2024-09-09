import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일에서 데이터를 불러오기
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 가격 차이 계산
df['price_difference'] = df['close_USDT'] - df['close_USD']

# 4. 가격 차이의 변동성 계산 (표준편차)
df['price_diff_volatility'] = df['price_difference'].rolling(window=14).std()  # 14일 이동 표준편차 예시

# 5. USDT/KRW의 가격이 USD/KRW보다 가장 낮은 경우 빨간색 점을 찍기 위한 조건 설정
df['color'] = df.apply(lambda row: 'red' if row['close_USDT'] < row['close_USD'] else None, axis=1)

# 6. 가격 차이의 최솟값과 최댓값 계산 (파란색 점의 색상 결정에 사용)
min_diff = df['price_difference'].min()
max_diff = df['price_difference'].max()

# 7. 파란색 점에 대한 색상 설정
def get_color(diff, min_diff, max_diff):
    if diff == max_diff:
        return 'blue'
    else:
        return None  # 나머지 경우는 점을 찍지 않음

# 색상 설정을 구간으로 나누어 적용하기
df['color'] = df.apply(
    lambda x: get_color(x['price_difference'], min_diff, max_diff) if x['color'] is None else x['color'], axis=1)

# 8. 색상 값이 None이 아닌 행만 필터링
df_filtered = df.dropna(subset=['color'])

# 9. 특정 컬럼 (예: 'close' 가격) 선택하여 비교
plt.figure(figsize=(14, 8))
plt.plot(df.index, df['close_USDT'], label='USDT/KRW Close', color='blue')
plt.plot(df.index, df['close_USD'], label='USD/KRW Close', color='red')

# 10. 괴리율에 따른 점 찍기 (빨간색과 파란색만)
plt.scatter(df_filtered.index, df_filtered['close_USDT'], color=df_filtered['color'],
            label='Price Difference Indicator', alpha=0.6, marker='o')

# 11. 빨간 점과 파란 점에 가격 텍스트 추가 및 검정색 점 추가
for i, row in df_filtered.iterrows():
    if row['color'] == 'blue':
        # 파란 점에 대해 검정색 점과의 가격 차이 계산
        black_price = df.loc[i, 'close_USD']  # 검정색 점 위치의 USD 가격
        blue_price = row['close_USDT']  # 파란 점 위치의 USDT 가격
        percentage_difference = ((blue_price - black_price) / black_price) * 100

        # 검정색 점 추가 및 가격 차이 표기
        plt.scatter(i, black_price, color='black', zorder=5)
        plt.annotate(f'{black_price:.2f}\n({percentage_difference:.2f}%)',
                     (i, black_price),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center',
                     fontsize=8,
                     color='black')

        # 파란색 점의 가격도 표시
        plt.annotate(f'{blue_price:.2f}',
                     (i, blue_price),
                     textcoords="offset points",
                     xytext=(0, -15),
                     ha='center',
                     fontsize=8,
                     color='blue')

    elif row['color'] == 'red':
        # 빨간 점에 대해 검정색 점과의 가격 차이 계산
        black_price = df.loc[i, 'close_USDT']  # 검정색 점 위치의 USDT 가격
        red_price = row['close_USD']  # 빨간 점 위치의 USD 가격
        percentage_difference = ((red_price - black_price) / black_price) * 100

        # 검정색 점 추가 및 가격 차이 표기
        plt.scatter(i, black_price, color='black', zorder=5)
        plt.annotate(f'{black_price:.2f}\n({percentage_difference:.2f}%)',
                     (i, black_price),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center',
                     fontsize=8,
                     color='black')

        # 빨간색 점의 가격도 표시
        plt.annotate(f'{red_price:.2f}',
                     (i, red_price),
                     textcoords="offset points",
                     xytext=(0, -15),
                     ha='center',
                     fontsize=8,
                     color='red')

# 12. 변동성 그래프 추가
plt.twinx()  # Create a second y-axis
plt.plot(df.index, df['price_diff_volatility'], label='Price Difference Volatility', color='gray', linestyle='--')
plt.ylabel('Price Difference Volatility')
plt.legend(loc='upper left')

# 13. 그래프 설정
plt.title('Comparison of USDT/KRW and USD/KRW Close Prices with Difference Indicators and Risk')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)

# 14. 그래프 보여주기
plt.show()