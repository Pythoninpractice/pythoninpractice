# first version
for num in range(1, 21):
    if num % 2 == 0:
        if num == 4:
            print(f"{num} is unlucky")
            continue
        else:
            print(f"{num} is even")
    elif num % 2 != 0:
        if num == 13:
            print(f"{num} is unlucky")
            continue
        else:
            print(f"{num} is odd")
print("\n-----\n")

# condensed version
for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
        continue
    elif num % 2 != 0:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
