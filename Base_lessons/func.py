def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

result = get_summ("Learn", "Python")
print(result)
print(result.upper())