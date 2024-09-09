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

# 8. 손익 계산
trades = []

for buy_date, sell_date in zip(buy_dates, sell_dates):
    buy_price = df.loc[buy_date, 'combined']
    sell_price = df.loc[sell_date, 'combined']
    profit_loss = sell_price - buy_price
    trades.append({
        'Buy Date': buy_date,
        'Buy Price': buy_price,
        'Sell Date': sell_date,
        'Sell Price': sell_price,
        'Profit/Loss': profit_loss
    })

# 9. DataFrame으로 변환
trades_df = pd.DataFrame(trades)

# 10. 엑셀 파일로 저장
trades_df.to_excel(r'C:\Users\D-syoh\workspace\propbase\trades_profit_loss.xlsx', index=False)

print("엑셀 파일이 생성되었습니다: trades_profit_loss.xlsx")