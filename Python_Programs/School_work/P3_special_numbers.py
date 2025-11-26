def main():
    
    def perfect_num(num):
        sum, count = 0, 1
        while count < num:
            if num % count == 0:
                sum += count
                count += 1
            else:
                count += 1
        if sum == num:
            #print(f"{num} is a perfect number!")
            print(num, "is a perfect number!")
        else:
            #print(f"{num} is not a perfect number!")
            print(num, "is not a perfect number!")
        return None
    
    
    def armstrong_num(num):
        str_num = str(num)
        sum, count = 0, len(str_num)
        for digit in str_num:
            sum += int(digit) ** count
        if sum == num:
            #print(f"{num} is a armstrong number!")
            print(num, "is a armstrong number!")
        else:
            #print(f"{num} is not a armstrong number!")
            print(num, "is not a armstrong number!")
        return None
    
    
    def palindrome_list(num):
        list_num = rev_list_num = []
        
        for digit in str(num):
            list_num.append(digit)
        
        str_num1 = ''.join(list_num)
        num1 = int(str_num1)
        print(num1)
        
        while len(list_num):
            rev_list_num.append(list_num.pop())
        
        str_num2 = ''.join(rev_list_num)
        num2 = int(str_num2)
        print(num2)
        
        if (num1+num2) == (num*2):
            print(num, 'is a palindrome')
        else:
            print(num, 'is not a palindrome')
    
    
    def palindrome(num):
        reverse_num, temp = 0, num
        while(temp>0):
            digit = temp % 10
            reverse_num = (reverse_num * 10) + digit
            temp = temp // 10
        if num == reverse_num:
            print(num, 'is a palindrome')
        else:
            print(num, 'is not a palindrome')
        
    
    
    num = int(input("Enter a number: "))
    perfect_num(num)
    armstrong_num(num)
    palindrome(num)


main()