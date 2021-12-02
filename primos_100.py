primos_100 = [2]
for i in range(2, 100):
    centinel = True

    if i % 2 != 0:
        for d in range(2, i//2):
            if i % d == 0:
                centinel = False
                break
        if centinel:
            primos_100.append(i)


print(primos_100)
