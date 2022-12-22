import numpy as np
import matplotlib.pyplot as plt

x1 = [1, 5, 1];
x6 = [-2, 0, 1]
x2 = [1, 4, 1];
x7 = [-1, -3, 1]
x3 = [1, 3, 1];
x8 = [-2, 2, 1]
x4 = [-1, 3, 1];
x9 = [-1, 1, 1]
x5 = [-1, -2, 1];
x10 = [-1, -1, 1]

x11 = [-1, 0, -1];
x16 = [-2, -1, -1]
x12 = [-1, -1, -1];
x17 = [-2, -2, -1]
x13 = [-1, 1, -1];
x18 = [-3, 1, -1]
x14 = [-3, -2, -1];
x19 = [-3, -4, -1]
x15 = [-4, -1, -1];
x20 = [-2, 1, -1]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

v = (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20)
v = np.array(v)
v_t = np.array(v).transpose()

print("V:\n", v, "\n        \n", "V tr:\n", v_t)

v_p = np.dot(v_t, v)
v_obr = np.linalg.inv(v_p)

print("v_p: ", v_p)
print("Обратная матрица: ", v_obr)

v_ = np.dot(v_obr, v_t)
print("Псевдо-Обратная матрица:", v_)

w = np.dot(v_, y)
print("w:", w)


def draw(w):
    t = np.linspace(0, 5)
    y_ = np.array((w[0] * t + w[2]) / -w[1])

    plt.plot(x1[0], x1[1], 'd m')
    plt.plot(x2[0], x2[1], 'd m')
    plt.plot(x3[0], x3[1], 'd m')
    plt.plot(x4[0], x4[1], 'd m')
    plt.plot(x5[0], x5[1], 'd m')
    plt.plot(x6[0], x6[1], 'd m')
    plt.plot(x7[0], x7[1], 'd m')
    plt.plot(x8[0], x8[1], 'd m')
    plt.plot(x9[0], x9[1], 'd m')
    plt.plot(x10[0], x10[1], 'd m')
    plt.title("Lab 1 v6")
    plt.plot(-x11[0], -x11[1], 'p c', mec='hotpink')
    plt.plot(-x12[0], -x12[1], 'p c', mec='hotpink')
    plt.plot(-x13[0], -x13[1], 'p c', mec='hotpink')
    plt.plot(-x14[0], -x14[1], 'p c', mec='hotpink')
    plt.plot(-x15[0], -x15[1], 'p c', mec='hotpink')
    plt.plot(-x16[0], -x16[1], 'p c', mec='hotpink')
    plt.plot(-x17[0], -x17[1], 'p c', mec='hotpink')
    plt.plot(-x18[0], -x18[1], 'p c', mec='hotpink')
    plt.plot(-x19[0], -x19[1], 'p c', mec='hotpink')
    plt.plot(-x20[0], -x20[1], 'p c', mec='hotpink')
    plt.plot(t, y_, 'hotpink', linewidth=1)
    plt.grid('green', linestyle='--', linewidth=0.5)
    plt.show()


def iteration(y, vw):
    h = 1
    Y = np.array((y + h(vw - y)))
    W = np.dot(v_, Y)
    print("w:", w)
    vw = np.dot(v, W)
    calculation(vw, W, Y)


def calculation(vw, w, y):
    print("vw > 0 Проверка")
    temp_arr = []
    for element in vw:
        if element > 0:
            temp_arr.append(True)
            draw(w)
        else:
            temp_arr.append(False)
            iteration(y, vw)
    newArr = vw[temp_arr]
    print(temp_arr)
    print(newArr)


vw = np.dot(v, w)
calculation(vw, w, y)
