import re


def is_valid_cpf(value):
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        total = sum(
            int(cpf[num]) * ((i + 1) - num)
            for num in range(i)
        )
        digit = (total * 10) % 11
        digit = 0 if digit == 10 else digit

        if digit != int(cpf[i]):
            return False

    return True
