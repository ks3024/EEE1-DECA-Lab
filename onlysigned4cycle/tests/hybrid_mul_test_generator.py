from random import randint

n = 16
num_cases = 65536 // 4

tmp = ""
mem_offset = 0

for i in range(num_cases):
    mem_offset = 4 * i

    op_A = randint(0, 2 ** n - 1)
    op_B = randint(0, 2 ** n - 1)

    product = op_A * op_B
    product_high, product_low = product >> n, product % (2 ** n)

    tmp += hex(mem_offset) + "\t" + hex(op_A) + "\n"
    tmp += hex(mem_offset + 1) + "\t" + hex(op_B) + "\n"
    tmp += hex(mem_offset + 2) + "\t" + hex(product_low) + "\n"
    tmp += hex(mem_offset + 3) + "\t" + hex(product_high) + "\n"


with open("hybrid_mul_test_cases.ram", "w") as f:
    f.write(tmp)
