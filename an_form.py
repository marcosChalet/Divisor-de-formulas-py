def atomo(formula):
    if len(formula) == 1:
        return True


def caractere_valido(formula, x):
    if ord(formula[x]) < 97 or ord(formula[x]) > 122:
        if formula[x] != '&' and formula[x] != '#' and formula[x] != '>':
            if formula[x] != '-' and formula[x] != '(' and formula[x] != ')':
                return False
    return True


def op_bin_logico(formula, x):
    if(formula[x] == '&' or formula[x] == '#' or formula[x] == '>'):
        return True
    return False


def op_un_logico(formula, x):
    if formula[x] == '-':
        return True
    return False


def qtd_igual_parenteses(formula):

    total = 0
    for x in formula:
        if x == '(':
            total += 1
        if x == ')':
            total -= 1

    if total == 0:
        return True
    return False


def verifica(formula):

    if not qtd_igual_parenteses(formula):
        return False

    for x in range(len(formula)):
        if not caractere_valido(formula, x):
            return False

        if op_bin_logico(formula, x):
            if op_bin_logico(formula, x+1):
                return False

        if op_un_logico(formula, x):
            if formula[x-1] == ')':
                return False

            if op_bin_logico(formula, x+1):
                return False

        if formula[x] == '-':
            if op_bin_logico(formula, x+1):
                return False

        if formula[x] == '(' and formula[x+1] == ')':
            return False

        if(formula[0] != '(' and formula[len(formula)-1] != ')'):
            if formula[0] != '-':
                return False
    return True


def separa(lista, formula, x, tipo_div):
    if tipo_div == 'binario':
        if formula[0] != '-':
            esq_f, dir_f = formula[1:x], formula[x+1:-1]
        else:
            esq_f, dir_f = formula[0:x], formula[x+1:-1]

        lista.append(esq_f)
        lista.append(dir_f)
        divide_formula(esq_f, lista, len(esq_f)-1, 0)
        divide_formula(dir_f, lista, len(dir_f)-1, 0)

    else:
        dir_f = formula[1:]
        lista.append(dir_f)
        divide_formula(dir_f, lista, len(dir_f)-1, 0)


def divide_formula(formula, lista, x, op_divisao):

    if atomo(formula) or x == 0:
        return True

    if not verifica(formula):
        print("formula incorreta!\n")
        return False

    if formula[x] == ')':
        op_divisao += 1
    elif formula[x] == '(':
        op_divisao -= 1

    if op_bin_logico(formula, x) and op_divisao == 1:
        separa(lista, formula, x, 'binario')

    elif op_un_logico(formula, 0):
        separa(lista, formula, 0, 'unario')

    else:
        x -= 1
        divide_formula(formula, lista, x, op_divisao)

    return True


def complexidade(formula):

    tam = 0
    for x in formula:
        if x != '(' and x != ')':
            tam += 1
    return tam
