import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일에서 데이터를 불러오기
# 'time' 열을 날짜로 파싱하고 인덱스로 설정
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 특정 컬럼 (예: 'close' 가격) 선택하여 비교
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close_USDT'], label='USDT/KRW Close', color='blue')
plt.plot(df.index, df['close_USD'], label='USD/KRW Close', color='red')

# 4. 그래프 설정
plt.title('Comparison of USDT/KRW and USD/KRW Close Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# 5. 그래프 보여주기
plt.show()