def prime_chk(num):
    prime = False
    final_num = (num//2) + 1
    if num > 1:
        for number in range(2, final_num):
            if num % number == 0:
                prime = False
                break
        else:
            prime = True
    else:
        pass
    
    
    if prime == True:
        print(num, 'is prime.')
    else:
        print(num, 'is composite.')


num = int(input('Enter a number.\n-> '))
prime_chk(num)