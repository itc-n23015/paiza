def short_hair(N, S):
    return '\n'.join([S] * N)

N, S = int(input()), input()

result = short_hair(N, S)
print(result)
