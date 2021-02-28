import random
from tkinter import *

root = Tk()
root.title("Main W+N+S+Eindow")

frame1=Frame(root)
frame1.pack(side=TOP,fill=X)

frame2=Frame(root)
frame2.pack(side=BOTTOM, fill=X)

frame3=Frame(root)
frame3.pack(side=BOTTOM, fill=X)

x = [[0 for i in range(3)] for i in range(8)]
y = []
x1 = []
x2 = []
x3 = []
x0 = []
dx = []
xnorm = [[0 for i in range(3)] for i in range(8)]
a = [9, 1, 0, 5]  # Любые 4 числа

for i in range(0, 8):
    for j in range(0, 3):
        x[i][j] = random.randrange(0, 20)

for i in range(0, 8):
    temp = a[0] + a[1] * x[i][0] + a[2] * x[i][1] + a[3] * x[i][2]
    y.append(temp)

for i in range(0, len(x)):
    x1.append(x[i][0])
    x2.append(x[i][1])
    x3.append(x[i][2])

xabs = [x1, x2, x3]

for i in range(0, 3):
    temp = (max(xabs[i]) + min(xabs[i])) / 2
    x0.append(temp)

for i in range(0, 3):
    temp = x0[i] - min(xabs[i])
    dx.append(temp)

for i in range(0, len(x)):
    for j in range(0, 3):
        xnorm[i][j] = round((x[i][j] - x0[j]) / dx[j], 2)

Yetalon = a[0] + a[1] * x0[0] + a[2] * x0[1] + a[3] * x0[2]

ymax = y[0]
for i in range(0, len(y)):
    if y[i] > ymax:
        ymax = y[i]

num1 = Label(frame1, text='1', font='arial 20')
num2 = Label(frame1, text='2', font='arial 20')
num3 = Label(frame1, text='3', font='arial 20')
num4 = Label(frame1, text='4', font='arial 20')
num5 = Label(frame1, text='5', font='arial 20')
num6 = Label(frame1, text='6', font='arial 20')
num7 = Label(frame1, text='7', font='arial 20')
num8 = Label(frame1, text='8', font='arial 20')
txtx1 = Label(frame1, text='X₁', font='arial 20')
txtx2 = Label(frame1, text='X₂', font='arial 20')
txtx3 = Label(frame1, text='X₃', font='arial 20')
txtY = Label(frame1, text='Y', font='arial 20')
txtxn1 = Label(frame1, text='Xₙ₁', font='arial 20')
txtxn2 = Label(frame1, text='Xₙ₂', font='arial 20')
txtxn3 = Label(frame1, text='Xₙ₃', font='arial 20')
txtx0 = Label(frame1, text='X₀', font='arial 20')
txtdx = Label(frame1, text='dx', font='arial 20')
txtYetalon = Label(frame3, text='Еталонне значення У = ' + str(Yetalon), font='arial 20')
txtYmax = Label(frame2, text='Точка плану за варіантом 103 : max(y) = ' + str(ymax), font='arial 20')

xnum1 = Label(frame1, text=x[0][0], font='arial 20')
xnum2 = Label(frame1, text=x[0][1], font='arial 20')
xnum3 = Label(frame1, text=x[0][2], font='arial 20')
xnum4 = Label(frame1, text=x[1][0], font='arial 20')
xnum5 = Label(frame1, text=x[1][1], font='arial 20')
xnum6 = Label(frame1, text=x[1][2], font='arial 20')
xnum7 = Label(frame1, text=x[2][0], font='arial 20')
xnum8 = Label(frame1, text=x[2][1], font='arial 20')
xnum9 = Label(frame1, text=x[2][2], font='arial 20')
xnum10 = Label(frame1, text=x[3][0], font='arial 20')
xnum11 = Label(frame1, text=x[3][1], font='arial 20')
xnum12 = Label(frame1, text=x[3][2], font='arial 20')
xnum13 = Label(frame1, text=x[4][0], font='arial 20')
xnum14 = Label(frame1, text=x[4][1], font='arial 20')
xnum15 = Label(frame1, text=x[4][2], font='arial 20')
xnum16 = Label(frame1, text=x[5][0], font='arial 20')
xnum17 = Label(frame1, text=x[5][1], font='arial 20')
xnum18 = Label(frame1, text=x[5][2], font='arial 20')
xnum19 = Label(frame1, text=x[6][0], font='arial 20')
xnum20 = Label(frame1, text=x[6][1], font='arial 20')
xnum21 = Label(frame1, text=x[6][2], font='arial 20')
xnum22 = Label(frame1, text=x[7][0], font='arial 20')
xnum23 = Label(frame1, text=x[7][1], font='arial 20')
xnum24 = Label(frame1, text=x[7][2], font='arial 20')

ynum1 = Label(frame1, text=y[0], font='arial 20')
ynum2 = Label(frame1, text=y[1], font='arial 20')
ynum3 = Label(frame1, text=y[2], font='arial 20')
ynum4 = Label(frame1, text=y[3], font='arial 20')
ynum5 = Label(frame1, text=y[4], font='arial 20')
ynum6 = Label(frame1, text=y[5], font='arial 20')
ynum7 = Label(frame1, text=y[6], font='arial 20')
ynum8 = Label(frame1, text=y[7], font='arial 20')

xnnum1 = Label(frame1, text=xnorm[0][0], font='arial 20')
xnnum2 = Label(frame1, text=xnorm[0][1], font='arial 20')
xnnum3 = Label(frame1, text=xnorm[0][2], font='arial 20')
xnnum4 = Label(frame1, text=xnorm[1][0], font='arial 20')
xnnum5 = Label(frame1, text=xnorm[1][1], font='arial 20')
xnnum6 = Label(frame1, text=xnorm[1][2], font='arial 20')
xnnum7 = Label(frame1, text=xnorm[2][0], font='arial 20')
xnnum8 = Label(frame1, text=xnorm[2][1], font='arial 20')
xnnum9 = Label(frame1, text=xnorm[2][2], font='arial 20')
xnnum10 = Label(frame1, text=xnorm[3][0], font='arial 20')
xnnum11 = Label(frame1, text=xnorm[3][1], font='arial 20')
xnnum12 = Label(frame1, text=xnorm[3][2], font='arial 20')
xnnum13 = Label(frame1, text=xnorm[4][0], font='arial 20')
xnnum14 = Label(frame1, text=xnorm[4][1], font='arial 20')
xnnum15 = Label(frame1, text=xnorm[4][2], font='arial 20')
xnnum16 = Label(frame1, text=xnorm[5][0], font='arial 20')
xnnum17 = Label(frame1, text=xnorm[5][1], font='arial 20')
xnnum18 = Label(frame1, text=xnorm[5][2], font='arial 20')
xnnum19 = Label(frame1, text=xnorm[6][0], font='arial 20')
xnnum20 = Label(frame1, text=xnorm[6][1], font='arial 20')
xnnum21 = Label(frame1, text=xnorm[6][2], font='arial 20')
xnnum22 = Label(frame1, text=xnorm[7][0], font='arial 20')
xnnum23 = Label(frame1, text=xnorm[7][1], font='arial 20')
xnnum24 = Label(frame1, text=xnorm[7][2], font='arial 20')

dxnum1 = Label(frame1, text=dx[0], font='arial 20')
dxnum2 = Label(frame1, text=dx[1], font='arial 20')
dxnum3 = Label(frame1, text=dx[2], font='arial 20')

x0num1 = Label(frame1, text=x0[0], font='arial 20')
x0num2 = Label(frame1, text=x0[1], font='arial 20')
x0num3 = Label(frame1, text=x0[2], font='arial 20')

num1.grid(row=1, column=0, sticky=W+N+S+E, pady=5, padx=5)
num2.grid(row=2, column=0, sticky=W+N+S+E, pady=5, padx=5)
num3.grid(row=3, column=0, sticky=W+N+S+E, pady=5, padx=5)
num4.grid(row=4, column=0, sticky=W+N+S+E, pady=5, padx=5)
num5.grid(row=5, column=0, sticky=W+N+S+E, pady=5, padx=5)
num6.grid(row=6, column=0, sticky=W+N+S+E, pady=5, padx=5)
num7.grid(row=7, column=0, sticky=W+N+S+E, pady=5, padx=5)
num8.grid(row=8, column=0, sticky=W+N+S+E, pady=5, padx=5)
txtx1.grid(row=0, column=1, sticky=W+N+S+E, pady=5, padx=5)
txtx2.grid(row=0, column=2, sticky=W+N+S+E, pady=5, padx=5)
txtx3.grid(row=0, column=3, sticky=W+N+S+E, pady=5, padx=5)
txtY.grid(row=0, column=4, sticky=W+N+S+E, pady=5, padx=5)
txtxn1.grid(row=0, column=5, sticky=W+N+S+E, pady=5, padx=5)
txtxn2.grid(row=0, column=6, sticky=W+N+S+E, pady=5, padx=5)
txtxn3.grid(row=0, column=7, sticky=W+N+S+E, pady=5, padx=5)
txtx0.grid(row=9, column=0, sticky=W+N+S+E, pady=5, padx=5)
txtdx.grid(row=10, column=0, sticky=W+N+S+E, pady=5, padx=5)

xnum1.grid(row=1, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum2.grid(row=1, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum3.grid(row=1, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum4.grid(row=2, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum5.grid(row=2, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum6.grid(row=2, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum7.grid(row=3, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum8.grid(row=3, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum9.grid(row=3, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum10.grid(row=4, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum11.grid(row=4, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum12.grid(row=4, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum13.grid(row=5, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum14.grid(row=5, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum15.grid(row=5, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum16.grid(row=6, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum17.grid(row=6, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum18.grid(row=6, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum19.grid(row=7, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum20.grid(row=7, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum21.grid(row=7, column=3, sticky=W+N+S+E, pady=5, padx=5)
xnum22.grid(row=8, column=1, sticky=W+N+S+E, pady=5, padx=5)
xnum23.grid(row=8, column=2, sticky=W+N+S+E, pady=5, padx=5)
xnum24.grid(row=8, column=3, sticky=W+N+S+E, pady=5, padx=5)

xnnum1.grid(row=1, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum2.grid(row=1, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum3.grid(row=1, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum4.grid(row=2, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum5.grid(row=2, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum6.grid(row=2, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum7.grid(row=3, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum8.grid(row=3, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum9.grid(row=3, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum10.grid(row=4, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum11.grid(row=4, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum12.grid(row=4, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum13.grid(row=5, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum14.grid(row=5, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum15.grid(row=5, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum16.grid(row=6, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum17.grid(row=6, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum18.grid(row=6, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum19.grid(row=7, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum20.grid(row=7, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum21.grid(row=7, column=7, sticky=W+N+S+E, pady=5, padx=5)
xnnum22.grid(row=8, column=5, sticky=W+N+S+E, pady=5, padx=5)
xnnum23.grid(row=8, column=6, sticky=W+N+S+E, pady=5, padx=5)
xnnum24.grid(row=8, column=7, sticky=W+N+S+E, pady=5, padx=5)

ynum1.grid(row=1, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum2.grid(row=2, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum3.grid(row=3, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum4.grid(row=4, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum5.grid(row=5, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum6.grid(row=6, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum7.grid(row=7, column=4, sticky=W+N+S+E, pady=5, padx=5)
ynum8.grid(row=8, column=4, sticky=W+N+S+E, pady=5, padx=5)

x0num1.grid(row=9, column=1, sticky=W+N+S+E, pady=5, padx=5)
x0num2.grid(row=9, column=2, sticky=W+N+S+E, pady=5, padx=5)
x0num3.grid(row=9, column=3, sticky=W+N+S+E, pady=5, padx=5)

dxnum1.grid(row=10, column=1, sticky=W+N+S+E, pady=5, padx=5)
dxnum2.grid(row=10, column=2, sticky=W+N+S+E, pady=5, padx=5)
dxnum3.grid(row=10, column=3, sticky=W+N+S+E, pady=5, padx=5)

txtYetalon.pack(side=LEFT)
txtYmax.pack(side=LEFT)

root.mainloop()