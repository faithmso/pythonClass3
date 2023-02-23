def prime_number():
    i = 1
    if i < 1000:
        if all(i % j == 0 for j in range(1, i + 1)):
            return i
        i += 1
    else:
        return i

print(prime_number())
