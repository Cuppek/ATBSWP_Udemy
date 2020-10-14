def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Nie dziel przez 0')

print(div42by(2))
print(div42by(42))
print(div42by(0))
print(div42by(1))
print(div42by(12))
