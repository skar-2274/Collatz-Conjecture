def collatz_step(n):
    """Returns the next step in the Collatz sequence, starting from n."""
    if n % 2 == 0:
        return n // 2
    elif n % 2 != 0:
        return 3 * n + 1
    else:
        return None

n = int(input("Input a value of n > "))

while n > 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
    else:
        n = 3 * n + 1
        print(n)

record_steps = 0
record_n = 0
n_max = 0
target_max = 0

for target in range(1, 1001):
    steps = 0
    n = target
    while n > 1:
        if n_max < n:
            n_max = n
            if target_max < target:
                target_max = target
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps += 1
    if steps > record_steps:
        record_n = target
        record_steps = steps

print("Below is the value of n for the record number of steps when n < 1000")
print(f'Record steps required: {record_steps} for n = {record_n}. Highest number reached is {n_max}, the number this is from is n = {target_max}')
