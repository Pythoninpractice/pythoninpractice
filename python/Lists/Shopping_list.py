
print("WELCOME TO YOUR SHOPPING CART")

shopping_list = []
while True:
    inputval = input("Add something to the cart? Type q to quit: ")
    if inputval == "q":
        shopping_list.sort()
        print("YOUR FINAL GROCERY LIST")
        for val in shopping_list:
            print(f"- {val}")
        break
    else:
        shopping_list.append(inputval)
