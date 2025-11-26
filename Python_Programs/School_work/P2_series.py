def main():
    x = int(input("Enter a number: "))
    n = int(input("Enter the final exponent for the series: "))


    def series1(x, n):
        # Series 1: 1 + x^1 + x^2 + x^n
        sum = count = 1
        while count <= n:
            sum += x**count
            count += 1
        # print(f"Sum: {sum}")
        print("Sum: ", sum)
        return None


    def series2(x, n):
        # Series 2: 1 - x^1 + x^2 - x^3 + x^4 (+-) x^n |('+' if n is +ve ; '-' if n is -ve)
        sum = count = 1
        while count <= n:
            if (count % 2) == 0:
                sum += x**count
            else:
                sum -= x**count
            count += 1
        # print(f"Sum: {sum}")
        print("Sum: ", sum)
        return None


    def series3(x, n):
        # Series 3: (x^1)/1 + (x^2)/2 - (x^3)/3 + (x^4)/4 + (x^n)/n
        sum, count = 0, 1
        while count <= n:
            if count % 2 == 0:
                sum += (x**count)/count
            else:
                sum -= (x**count)/count
            count += 1
        # print(f"Sum: {sum}")
        print("Sum: ", sum)
        return None


    def series4(x, n):
        # Series 4: (x^1)/1! + (x^2)/2! - (x^3)/3! + (x^4)/4! + (x^n)/n!
        sum, count = 0, 1
        while count <= n:
            factorial = 1
            for num in range(1, count+1):
                factorial *= num
            if (count % 2) == 0:
                sum += (x**count)/factorial
            else:
                sum -= (x**count)/factorial
            count += 1
      # print(f"Sum: {sum}")
        print("Sum: ", sum)
        return None

    series1(x, n)
    series2(x, n)
    series3(x, n)
    series4(x, n)


while True:
    try:
        main()
        break
    except ValueError:
        print("Invalid value! ¯\_(ツ)_/¯")
        print("Try entering an integer instead.")