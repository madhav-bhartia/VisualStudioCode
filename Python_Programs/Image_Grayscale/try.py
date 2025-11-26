def power(base, expo):
    if expo == 1:
        return base
    return base * power(base, (expo-1))

base: int = int(input("-> "))
expo: int = int(input("-> "))
print(f"the result is: {power(base, expo)}")