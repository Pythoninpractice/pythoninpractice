times = 10
while times >= 1:
    print(":-) " * times)
    times -= 1

times = 10
for num in range(1, 11):
    print(" " * times + "+" * num + "+" * (num-1))
    times -= 1

times = 10
for num in range(1, 11):
    print("   " * times + ":-)" * num + ":-)" * (num-1))
    times -= 1
