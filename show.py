import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
data = pd.read_csv("data/Advertising.csv")

# 查看数据前 5 行
print(data.head())

# 可视化 TV 广告费用与销量的关系
plt.scatter(data["TV"], data["Sales"])
plt.xlabel("TV Advertising Cost")
plt.ylabel("Product Sales")
plt.title("TV Advertising vs Sales")
plt.show()
