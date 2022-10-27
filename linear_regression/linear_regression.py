import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 가설함수

# 최적의 기울기와 y절편을 구해서 그래프를 하나 그리는데 가지고 있는 데이터와 가장 비슷하게 나오는 그래프를 그리는게 목적이다.
# 학습 데이터를


def hypothesis(theta, x):

    # please implement
    ret = theta[0] + theta[1] * x  # theta값을 조절해서 최적의 값을 찾아낸다.

    return ret  # 예측값

# 가장 데이터를 잘 예측하는 모델을 구하기 위해서는 내가 만든 모델의 예측값과 실제값의 오차를 줄여나가면서 최적의 모델을 만든다.
# 현재 모델이 얼마나 잘 표현하고 있는지 오차값을 이용해서 모델을 평가할 수 있다. 예측값과 실제값의 차이를 보여준다.


def cost_function(X, y, theta):
    ret = 0
    # n: Number of trainging examples
    n = len(X)

    for i in range(n):
        # 예측값과 결과의 차이를 더해준다. 제곱을 하는 이유는 양수로 통일하고
        ret = ret + ((hypothesis(theta, X[i]) - y[i])**2)

        # 결과값을 더 확실하게 알아보기 위해 제곱을해준다.
    ret = ret/n    # 오차의 평균값이 작을수록 잘 예측한 것이다.
    return ret


def comparison_cost(X, y, t1, t0):

    cost = cost_function(X, y, [t0, t1])

    # Evaluate the cost function as some values
    print("Cost for minimal parameters:", cost, ", with theta0 =", t0,
          " and theta1 =", t1,)  # Best possible(got it from numpy)
    # theta의 값에 따라서 오차 값이 차이가 난다.
    print("Cost for other theta:", cost_function(X, y, [8.4, 0.6]))


def gradient(X, y, theta):
    g = np.array([0, 0])
    n = len(X)

    # implement the update rule discribed

    pred = np.dot(X, theta[1])+theta[0]  # 임의의 theta값을 이용해서 예측값을 구한다.
    error = pred - y

    # 가설함수로 구한값에서 실제값을 뺀 값을 제곱해준다. 모든 입력변수와 결과값을 앞의 과정을 진행하고 더해준다.
    t0 = np.sum(error) / n
    # 그리고 입력변수의 개수로 나눠주는데 계산의 편의를 위해서 2로 더 나눠준 값을 theta0에 대해서 편미분한 값이다.
    t1 = np.sum((error) * X) / n
    # m개의 학습 데이터가 주어졌을 때, 각 학습 데이터에 대해서 현재 모델이 예측한 값과 실제 학습데이터에서의 값의 차이를 제곱한 값의 평균이다.
    g = np.array([t0, t1])

    # 각 벡터를 norm 값으로 나누면 회귀전 정규화가 가능하다. 정규화를 하면 overfitting 되는것을 방지할 수 있다.
    return (g / np.linalg.norm(g))
    # return g

# gradient descent를 하면서 cost function을 최소화 하면서 원하는 모델이 되도록 theta값을 구한다.
# 임의의 theta값이 있을때 cost function에서 해당 theta값이 위치하는 지점의 기울기를 보고, 극소 점으로 가기 위해 theta를 증가시켜야 하는지 감소시켜야 하는지 결정하고
# 극소점으로 점점 갈수록 cost 값이 작아지고 극소점일 때 cost가 가장 작아지게 된다.


def optimise_by_gradient_descent(X, y, t1, t0):
    # Start with some value for theta
    theta = np.array([0, 0])  # 임의의 theta값을 정해준다.

    listt0 = np.array([])
    listt1 = np.array([])

    # learning rate

    alpha = 0.01  # 어느 정도의 비율로 업데이트 해 나아갈 것인지 결정 짓는다. learning rate가 작을수록 느리지만 값이 정확한 값을 찾을수 있고
    # 값이 크면 빠른 시간 내에 찾지만 최소값으로 수렴하다가 다시 발산할 수도 있다.

    # number of steps
    steps = 10000  # 시간이 오래걸리긴 하지만 학습이 진행될수록 파라미터는 최적화 되었다.

    # gradient descent

    for s in range(steps):
        listt0 = np.append(listt0, theta[0])  # save data for drawing
        listt1 = np.append(listt1, theta[1])

    # parameter update part - Using gradient function, please implement
        error = gradient(X, y, theta)
        # theta[0]값을 cost function을 theta[0]에 대해서 편미분한 값과 학습률을 곱한 값을 빼서 업데이트 해준다.
        theta_0 = theta[0] - alpha * error[0]
        theta_1 = theta[1] - alpha * error[1]
        theta = np.array([theta_0, theta_1])

    print("Gradient descent gives after", steps, "steps: ", theta)
    print("Best theta: ", [t0, t1])


def main():

    # Training
    Tx = np.array([2, 7, 13, 16, 22, 27, 35, 45, 50])  # 입력변수
    Ty = np.array([5, 20, 14, 32, 22, 38, 39, 59, 70])  # 실제값
    t1, t0 = np.polyfit(Tx, Ty, 1)  # numpy library를 이용해서 구한 최적값

    '''# Draw the Training set
    plt.figure(figsize=(10, 8))
    plt.plot(Tx, Ty, 'X')
    plt.title("Training set", fontsize=20)
    plt.xlabel("Weeks living in Jeju", fontsize=18)
    plt.ylabel("# of having black-pork", fontsize=18)

    # Best fit (by using the built-in fuction of numpy)
    # This is what we want to find by ourself in the following

    t1, t0 = np.polyfit(Tx, Ty, 1) 
    plt.plot(Tx, t0 + t1 * Tx)
    print("theta0 :", t0, " theta1:", t1)
    plt.show()'''

    # HW part
    # t1,t0 is the fitted parameter which stands for the best possible(got it from numpy)
    comparison_cost(Tx, Ty, t1, t0)

    optimise_by_gradient_descent(Tx, Ty, t1, t0)


main()
