def check_prime_nb(number):
    state = True
    for n in range(2,number):
        if number % n == 0:
            print(number, "is not a prime number and is divisible with", n)
            state = False
            break
    if state == True:
        print(number, "is a Prime Number!\n")

while True:
    x = int(input("Enter Prime number here : \n---> "))
    print("")
    check_prime_nb(x)
