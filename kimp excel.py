import pandas as pd

# 1. CSV 파일에서 데이터를 불러오기
df_usdt = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDTKRW.csv', parse_dates=['time'], index_col='time')
df_usd = pd.read_csv(r'C:\Users\D-syoh\workspace\propbase\data\USDKRW.csv', parse_dates=['time'], index_col='time')

# 2. 두 데이터셋을 날짜 기준으로 병합
df = pd.merge(df_usdt, df_usd, left_index=True, right_index=True, suffixes=('_USDT', '_USD'))

# 3. 김치 프리미엄 계산 (백분율로 표현)
df['kimchi_premium'] = (df['close_USDT'] / df['close_USD'] - 1) * 100

# 4. 매수와 매도 신호 생성
df['buy_signal'] = (df['kimchi_premium'] < 2)
df['sell_signal'] = (df['kimchi_premium'] > 5)

# 5. 매수 및 매도 시점을 기록할 리스트
trades = []
position = None

# 6. 매수 및 매도 시점 찾기
for date, row in df.iterrows():
    if position is None:
        # 매수 신호가 나오면 매수
        if row['buy_signal']:
            position = row['close_USDT']
            trades.append({'date': date, 'action': 'buy', 'price': position})
    else:
        # 매도 신호가 나오면 매도하고 포지션 해제
        if row['sell_signal']:
            profit = row['close_USDT'] - position
            trades.append({'date': date, 'action': 'sell', 'price': row['close_USDT'], 'profit': profit})
            position = None

# 7. 거래 결과를 데이터프레임으로 변환
df_trades = pd.DataFrame(trades)

# 8. 결과를 CSV 파일로 저장
output_path = r'C:\Users\D-syoh\workspace\propbase\data\kimchi_premium_trades.csv'
df_trades.to_csv(output_path, index=False)

# 9. 완료 메시지 출력
print(f"CSV 파일이 저장되었습니다: {output_path}")