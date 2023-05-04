import pandas as pd
import numpy as np

# 设置随机数种子，以便每次运行得到相同的结果
np.random.seed(42)

# 生成100个随机样本
num_samples = 100

# 生成四个随机变量的取值
x1 = np.random.randint(low=0, high=5, size=num_samples)
x2 = np.random.randint(low=10, high=501, size=num_samples)
x3 = np.random.randint(low=1, high=100, size=num_samples)
x4 = np.random.randint(low=0, high=5, size=num_samples)

# 计算因变量
y = 5 * np.exp(x1) + 3 * x2 - 50 * np.log2(x3) + 5 ** x4

# 将自变量和因变量存储在 DataFrame 中
df = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'y': y})

# 将 DataFrame 写入 CSV 文件中
df.to_csv('data.csv', index=False)
