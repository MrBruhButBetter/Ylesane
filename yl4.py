while True:
    a = int(input("siseta arv: "))
    b = int(input("siseta arv: "))

    if a < b:
        print("a: ", a)
    elif b < a:
        print("b: ", b)
    else:
        print("a=b = ", a)