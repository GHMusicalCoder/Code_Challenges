
Tn = 360
rt = 0.005
n = 12
pv = 98772 + 105

impt = (pv*rt*((rt + 1)**(Tn + 1) - (rt + 1)**n)) / ((rt + 1) * ((rt + 1)**Tn - 1))

print(impt)