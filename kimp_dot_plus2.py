import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일에서 데이터를 불러오기
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 괴리율 계산
df['price_difference'] = df['close_USDT'] - df['close_USD']
df['percentage_difference'] = (df['price_difference'] / df['close_USD']) * 100

# 4. 매수 및 매도 신호 결정
df['buy_signal'] = (df['percentage_difference'] < 1) | (df['percentage_difference'] < 0)
df['sell_signal'] = df['percentage_difference'] > 5

# 5. 매수와 매도가 번갈아가면서 나올 수 있도록 신호 선택
signals = []
buy_active = False

for i in range(len(df)):
    if df.iloc[i]['buy_signal'] and not buy_active:
        signals.append((df.index[i], df.iloc[i]['close_USD'], 'Buy', 'red'))
        buy_active = True
    elif df.iloc[i]['sell_signal'] and buy_active:
        signals.append((df.index[i], df.iloc[i]['close_USDT'], 'Sell', 'blue'))
        buy_active = False

# 6. 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close_USDT'], label='USDT/KRW Close', color='blue')
plt.plot(df.index, df['close_USD'], label='USD/KRW Close', color='red')

# 7. 매수와 매도 포인트 추가
for signal in signals:
    date, price, signal_type, color = signal
    plt.scatter(date, price, color=color, marker='o', label=f'{signal_type} Signal', zorder=5)
    plt.annotate(f'{signal_type}: {price:.2f}', (date, price),
                 textcoords="offset points", xytext=(0, 10 if color == 'red' else -15),
                 ha='center', fontsize=8, color=color)

# 8. 그래프 설정
plt.title('Comparison of USDT/KRW and USD/KRW Close Prices with Alternating Buy and Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# 9. 그래프 보여주기
plt.show()