Banco_de_dados = {
    'BOX1': {
        'um:': 1,
        'dois': 2,
        'três': 3,
        'quatro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9,
        'dez': 10
    },
    'BOX2': {
        'onze': 11,
        'doze': 12,
        'treze': 13,
        'quatorze': 14,
        'quinze': 15,
        'dezeseis': 16,
        'dezesete': 17,
        'dezoito': 18,
        'dezenove': 19,
    },
    'BOX3': {
        'vinte': 20,
        'trinta': 30,
        'quarenta': 40,
        'cinquenta': 50,
        'sessenta': 60,
        'setenta': 70,
        'oitenta': 80,
        'noventa': 90,
    },
    'BOX4': {
        'cento': 100,
        'duzentos': 200,
        'trezentos': 300,
        'quatrocentos': 400,
        'quinhentos': 500,
        'seiscentos': 600,
        'setecentos': 700,
        'oitocentos': 800,
        'novecentos': 900,
    },
}

numero = input('Digite um numero :')
if numero.isnumeric():
    tamanho = len(numero)

def unidade():

    if tamanho == 1:
        for ID_palavra,ID_numeral in Banco_de_dados['BOX1'].items():
            if int(numero) == ID_numeral:
                print("--\n{}\n--".format(ID_palavra))

    if tamanho == 2 and numero[0] == '1' and numero[1] == '0':
        print("--\n{}\n--".format(list(Banco_de_dados['BOX1'])[9]))

    if tamanho == 2 and numero[0] == '1':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX2'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[1] == tamanho_ID_numeral[1]:
                print("--\n{}\n--".format(ID_palavra))

    if tamanho == 2 and numero[0] != '1':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX3'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                Copia_ID_palavra = ID_palavra
                for ID_palavra,ID_numeral in Banco_de_dados['BOX1'].items():
                    if numero[1] == str(ID_numeral):
                        print("--\n{} e {}\n--".format(Copia_ID_palavra,ID_palavra))

    if tamanho == 2 and numero[1] == '0':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX2'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                print("--\n{}\n--".format(ID_palavra))

    if tamanho == 3 and numero[1] != '0' and numero[2] != '0':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX4'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                centena = ID_palavra

        if (int(numero[1])) > 0 and (int(numero[1])) < 2:
            for ID_palavra,ID_numeral in Banco_de_dados['BOX2'].items():
                tamanho_ID_numeral = str(ID_numeral)
                if numero[1] == tamanho_ID_numeral[0] and numero[2] == tamanho_ID_numeral[1]:
                    dezena = ID_palavra

        else:
            for ID_palavra,ID_numeral in Banco_de_dados['BOX3'].items():
                tamanho_ID_numeral = str(ID_numeral)
                if numero[1] == tamanho_ID_numeral[0]:
                    dezena = ID_palavra

            for ID_palavra,ID_numeral in Banco_de_dados['BOX1'].items():
                tamanho_ID_numeral = str(ID_numeral)
                if numero[2] == tamanho_ID_numeral:
                    unidade = ID_palavra
        print("--\n{} e {} {}\n--".format(centena,dezena,unidade))


    elif tamanho == 3 and numero[1] == '0' and numero[2] == '0':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX4'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                print("--\n{}\n--".format(ID_palavra))

    elif tamanho == 3 and numero[1] != '0' and numero[2] == '0':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX4'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                centena = ID_palavra
        for ID_palavra,ID_numeral in Banco_de_dados['BOX2'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[1] == tamanho_ID_numeral[0]:
                dezena = ID_palavra
        print("--\n{} e {}\n--".format(centena, dezena))

    elif tamanho == 3 and numero[1] == '0' and numero[2] != '0':
        for ID_palavra,ID_numeral in Banco_de_dados['BOX4'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[0] == tamanho_ID_numeral[0]:
                centena = ID_palavra
        for ID_palavra,ID_numeral in Banco_de_dados['BOX1'].items():
            tamanho_ID_numeral = str(ID_numeral)
            if numero[2] == tamanho_ID_numeral:
                unidade = ID_palavra
        print("--\n{} e {}\n--".format(centena, unidade))


while tamanho != 1000:
    unidade()

    numero = input('Digite um numero :')

    tamanho = numero
    if numero.isnumeric():
        tamanho = len(numero)