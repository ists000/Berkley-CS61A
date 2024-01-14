def double_eights(n):
    pre_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and pre_eight:
            return True
        elif last_digit == 8:
            pre_eight = True
        else:
            pre_eight = False
        n = n // 10
    return False

a = double_eights(3743289818823)

print(a)
