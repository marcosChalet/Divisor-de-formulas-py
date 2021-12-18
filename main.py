import an_form
import os


def menu():

    print('[0] Sair')
    print('[1] Verificar Fórmula')
    print('[2] Dividir Formula')

    opcao = int(input('-> '))

    return opcao


def main():

    opcao = menu()

    if opcao < 1 or opcao > 2:
        return

    else:
        os.system('clear')
        print('Disjunção: #\nConjunção: &\nImplicação: >\n')
        formula = input('Entre com uma fórmula: ')
        formula = formula.replace(' ', '')
        lista = [formula]

        if opcao == 1:
            if an_form.verifica(formula):
                print('\nFormula Válida!')
            else:
                print('\nFormula Inválida!')

        if opcao == 2:
            if an_form.divide_formula(formula, lista, int(len(formula)-1), 0):
                lista.sort(key=an_form.complexidade)
                lista.reverse()

                print('\n\t\t########## Fórmulas ##########\n\n')
                for x in lista:
                    print(f'-> [{x}]')


if __name__ == "__main__":
    main()
