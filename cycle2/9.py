lst=[int(num) for num in input("enter list elements(seperated by space):").split()]

for i in range(len(lst)):
        if lst[i] > 100:
                lst[i]="over"
print(lst)
