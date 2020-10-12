l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
#Add item 70 after 60 in the given List
print(l1)
l1[2][2][2:0] = [70]
print(l1)