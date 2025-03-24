import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("data/Advertising.csv")

# 提取特征 (X) 和标签 (y)
X = data[["TV"]]  # 只用 TV 作为单变量线性回归的特征
y = data["Sales"]

# 划分训练集和测试集（80% 训练，20% 测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "main":
    print(f"训练集大小: {X_train.shape}, 测试集大小: {X_test.shape}")
