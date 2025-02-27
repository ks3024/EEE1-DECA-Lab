from random import randint

n = 16

truncate_output = False

assert n % 2 == 0

count = 5

for i in range(count):
    op1 = randint(0, 2 ** n - 1)
    op2 = randint(0, 2 ** n - 1)
    result = op1 * op2

    op1_high = op1 >> (n // 2)
    op1_low = op1 % (2 ** (n // 2))

    op2_high = op2 >> (n // 2)
    op2_low = op2 % (2 ** (n // 2))

    result_low = result % (2 ** n)

    overflow = (result_low != result)

    if truncate_output:
        print(op1, op2, op1_high, op1_low, op2_high, op2_low, result_low, overflow)
    else:
        print(op1, op2, op1_high, op1_low, op2_high, op2_low, result)
