from random import randint
import numpy as np
from scipy.stats import f, t

def findA(a, b=None):
    if b is None:
        return sum([a[i] ** 2 for i in range(len(a))]) / len(a)
    else:
        return sum(a[i] * b[i] for i in range(len(a))) / len(a)

def cramer(arr, ins, pos):
    matrix = np.insert(np.delete(arr, pos, 1), pos, ins, 1)

    return np.linalg.det(matrix) / np.linalg.det(arr)

def getDispersion(y, y_r):
    return [round(sum([(y[i][j] - y_r[i]) ** 2 for j in range(len(y[i]))]) / 3, 3) for i in range(len(y_r))]

def cochran(disp, m):
    Gp = max(disp) / sum(disp)
    Gt = [.9065, .7679, .6841, .6287, .5892, .5598, .5365, .5175, .5017, .4884]

    if Gp < Gt[m - 2]:
        return [round(Gp, 4), Gt[m - 2]]
    else:
        return

def student(disp, m, y_r, x_n):
    table = {
        8: 2.306,
        12: 2.179,
        16: 2.120,
        20: 2.086,
        24: 2.064,
        28: 2.048,
        'inf': 1.960
    }

    x_nT = x_n.T
    N = len(y_r)

    Sb = sum(disp) / len(y_r)
    Sbeta = (Sb / (m * N)) ** (1 / 2)

    beta = [sum([y_r[j] * x_nT[i][j] for j in range(N)]) / N for i in range(N)]
    t = [abs(beta[i]) / Sbeta for i in range(len(beta))]

    f3 = N * (m - 1)

    if f3 > 30:
        t_t = table['inf']
    elif f3 > 0:
        t_t = table[f3]
    else:
        return

    result = []
    for i in t:
        if i < t_t:
            result.append(False)
        else:
            result.append(True)

    return result

def fisher(y_r, y_st, b_det, disp, m):
    table = {
        8: [5.3, 4.5, 4.1, 3.8, 3.7, 3.6],
        12: [4.8, 3.9, 3.5, 3.3, 3.1, 3.0],
        16: [4.5, 3.6, 3.2, 3.0, 2.9, 2.7],
        20: [4.5, 3.5, 3.1, 2.9, 2.7, 2.6],
        24: [4.3, 3.4, 3.0, 2.8, 2.6, 2.5]
    }

    N = len(y_r)
    Sb = sum(disp) / N
    d = 0
    for b in b_det:
        if b:
            d += 1

    f4 = N - d
    f3 = N * (m - 1)
    Sad = (m / f4) * sum([(y_st[i] - y_r[i]) ** 2 for i in range(N)])
    Fap = Sad / Sb
    Ft = table[f3][f4 - 1]

    if Fap < Ft:
        return f"\nРівняння регресії адекватно оригіналу:\nFap < Ft: {round(Fap, 2)} < {Ft}"
    else:
        return f"\nРівняння регресії неадекватно оригіналу: \nFap > Ft: {round(Fap, 2)} > {Ft}"


def experiment(m, min_x1, max_x1, min_x2, max_x2, min_x3, max_x3):
    y_min = round((min_x1 + min_x2 + min_x3) / 3) + 200
    y_max = round((max_x1 + max_x2 + max_x3) / 3) + 200

    x_norm = np.array([
        [1, -1, -1, -1],
        [1, -1, 1, 1],
        [1, 1, -1, 1],
        [1, 1, 1, -1]
    ])

    x = np.array([
        [min_x1, min_x2, min_x3],
        [min_x1, max_x2, max_x3],
        [max_x1, min_x2, max_x3],
        [max_x1, max_x2, min_x3]
    ])

    y = [[randint(y_min, y_max) for _ in range(m)] for _ in range(len(x))]
    y_r = [round(sum(y[i]) / len(y[i]), 2) for i in range(len(y))]
    N = len(y_r)

    disp = getDispersion(y, y_r)
    cochran_cr = cochran(disp, m)

    if cochran_cr is None:
        raise Exception("Need more experiments")
    else:
        pass

    mx = [sum(i) / len(i) for i in x.T]
    my = sum(y_r) / N

    x_T = x.T

    a1 = findA(x_T[0], y_r)
    a2 = findA(x_T[1], y_r)
    a3 = findA(x_T[2], y_r)

    a11 = findA(x_T[0])
    a22 = findA(x_T[1])
    a33 = findA(x_T[2])

    a12 = a21 = findA(x_T[0], x_T[1])
    a13 = a31 = findA(x_T[0], x_T[2])
    a23 = a32 = findA(x_T[1], x_T[2])

    b_delta = np.array([
        [1, mx[0], mx[1], mx[2]],
        [mx[0], a11, a12, a13],
        [mx[1], a21, a22, a23],
        [mx[2], a31, a32, a33]
    ])

    b_set = np.array([my, a1, a2, a3])
    b = [cramer(b_delta, b_set, i) for i in range(N)]

    b_det = student(disp, m, y_r, x_norm)
    b_cut = b.copy()

    if b_det is None:
        raise Exception("Need more experiments")
    else:
        for i in range(N):
            if not b_det[i]:
                b_cut[i] = 0

        y_st = [round(b_cut[0] + x[i][0] * b_cut[1] + x[i][1] * b_cut[2] + x[i][2] * b_cut[3], 2) for i in range(N)]

    f1 = m - 1
    f2 = N
    f3 = f1 * f2

    student = t.ppf(q=1 - 0.025)
    t_student = student(df=f3)
    ts = student()
    res = [t for t in ts if t > t_student]

    d = len(res)
    f4 = N - d

    fisher_cr = f.ppf(dfn=f4, dfd=f3, q=1 - 0.05)

    print(f"\nМатриця планування для m = {m}:")
    for i in range(m):
        print(f"Y{i + 1} - {np.array(y).T[i]}")

    print(f"\nСередні значення функції відгуку за рядками:\nY_R: {y_r}")
    print(f"\nКоефіцієнти рівняння регресії:")
    for i in range(len(b)):
        print(f"b{i} = {round(b[i], 3)}")

    print("\nДисперсії по рядках:\nS²{y} = ", disp, sep="")
    print(f"\nЗа критерієм Кохрена дисперсія однорідна:\nGp < Gt - {cochran_cr[0]} < {cochran_cr[1]}")

    print(f"\nЗа критерієм Стьюдента коефіцієнти ", end="")
    for i in range(len(b_det)):
        if not b_det[i]:
            print(f"b{i} ", end="")
    print("приймаємо незначними")

    print(f"\nОтримані функції відгуку зі спрощеними коефіцієнтами:\nY_St - {y_st}")
    print(fisher_cr)

def startExperiment(Min_x1, Max_x1, Min_x2, Max_x2, Min_x3, Max_x3):
    global M
    try:
        experiment(M, Min_x1, Max_x1, Min_x2, Max_x2, Min_x3, Max_x3)
    except:
        print("Збільшуємо кількість експеритентів")
        M += 1
        startExperiment(Min_x1, Max_x1, Min_x2, Max_x2, Min_x3, Max_x3)

if __name__ == '__main__':
    Min_x1, Max_x1 = -20, 30
    Min_x2, Max_x2 = 30, 80
    Min_x3, Max_x3 = 30, 45

    M = 3
    startExperiment(Min_x1, Max_x1, Min_x2, Max_x2, Min_x3, Max_x3)
