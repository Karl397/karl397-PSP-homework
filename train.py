from sklearn.linear_model import LinearRegression
from preProcess import X_train,y_train

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

if __name__ == "name":
# 输出模型参数
    print(f"回归系数: {model.coef_[0]}, 截距: {model.intercept_}")
