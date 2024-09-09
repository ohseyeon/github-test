import matplotlib.pyplot as plt

# 데이터 준비
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 그래프 그리기
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# 그래프 제목 및 레이블 설정
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

# 그래프 출력
plt.show()

