def obter_valor_saque():
    while True:
        saque_input = input('Qual valor você vai sacar? R$: ')
        try:
            saque = int(saque_input)
            if saque > 0:
                return saque
            else:
                print('Valor inválido para saque! Tente outro valor.')
        except ValueError:
            print('Valor inválido. Tente um valor inteiro.')
saque = obter_valor_saque()
total = saque
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            while ced != 1:
                print(f'Total de {totced} cédulas de R${ced}')
                if ced == 100:
                    ced = 50
                elif ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 5
                elif ced == 5:
                    ced = 2
                elif ced == 2:
                    ced = 1
            break
