from sklearn.metrics import mean_squared_error
from train import model
from preProcess import X_test,y_test
import matplotlib.pyplot as plt


# 预测测试集
y_pred = model.predict(X_test)

# 计算均方误差（MSE）
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差 (MSE): {mse}")

# 绘制回归线
plt.scatter(X_test, y_test, color="blue", label="Actual Sales")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted Sales")
plt.xlabel("TV Advertising Cost")
plt.ylabel("Product Sales")
plt.title("Linear Regression: TV Advertising vs Sales")
plt.legend()
plt.show()
