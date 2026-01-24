for num in range(2,101):
    is_prime = True

    # for d in range(2, (num//2)+1):
    d = 2
    while (d*d)<num:
        if(num%d==0):
            is_prime = False
            break
        # else:
        #     d = d+1
        #     continue
        d = d + 1

    if(is_prime==True):
        print(f"{num} is a Prime Number")
