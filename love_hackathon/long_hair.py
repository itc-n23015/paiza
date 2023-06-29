def long_hair(N):
    return "lucky" if N % 7 == 0 else "unlucky"

N = int(input())

result = long_hair(N)
print(result)
