import matplotlib.pyplot as plt
import numpy as np

# 日本語設定
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')
plt.figure(figsize=(15, 8))

# 模擬試験の記録（例）
months = list(range(1, 13))
scores_python = [70, 80, 75, 85, 90, 92, 88, 95, 96, 97, 98, 100]
scores_sql = [50, 55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 90]
scores_git = [30, 40, 45, 50, 55, 58, 60, 63, 65, 68, 70, 75]

# データを積み上げる
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(months, scores_python, label='Python', color='lightblue')
ax.bar(months, scores_sql, bottom=scores_python, label='SQL', color='lightgreen')
bottom_sum = np.array(scores_python) + np.array(scores_sql)
ax.bar(months, scores_git, bottom=bottom_sum, label='Git', color='plum')

ax.set_title("模擬試験 成長記録チャート")
ax.set_xlabel("月")
ax.set_ylabel("得点（累積）")
ax.legend()
plt.xticks(months)
plt.grid(axis='y')

plt.tight_layout()
plt.show()


