import math as m
#latihan list
#menghitung rata2, median, modus ,varian dan simpangan baku
#input data
# n = int(input("masukkan jumlah data yang ingin di hitung: "))
# data= []
# for i in range (n):
#     xn = float(input(f"masukkan data ke {i+1} : "))
#     data.append(xn)
# print(data)
data = [9,4,10,12,7,6]
n = len(data)

#mencari total data
xi = 0
for i in range(len(data)):
    xi += data[i]

#rata rata
x = xi/n
print(f"rata-rata dari data adalah : {x}")

#median
datam = data.copy()
datam.sort()
me = 0
if(len(data)%2== 0):
    me = (datam[int((n+1)/2)-1]+ datam[int((n+1)/2)])/2
else:
    me = datam[int((n+1)/2)-1]
print(f"median dari data adalah : {me}")

#varian
xs = 0
for i in range(len(data)):
    xs += (data[i]-x)**2
var = xs/n
print(f"varian data tersebut adalah : {var}")
print(f"simpangan baku dari data adalah : {m.sqrt(var)}")
