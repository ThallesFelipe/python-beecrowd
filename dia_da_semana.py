def eh_bissexto(ano: int) -> bool:
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


codigos_meses = {
    1: 6,
    2: 2,
    3: 2,
    4: 5,
    5: 0,
    6: 3,
    7: 5,
    8: 1,
    9: 4,
    10: 6,
    11: 2,
    12: 4,
}


def calc_dia_semana() -> str:
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))

    y_ultimos_2_digitos_ano = ano % 100

    l = 0

    if mes < 1 or mes > 12:
        return "Mês inválido"

    

    if eh_bissexto(ano) and (mes == 1 or mes == 2):
        l = -1

    B = (5 * ((ano // 100) % 4)) % 7
    DIA_DA_SEMANA = (
        y_ultimos_2_digitos_ano
        + y_ultimos_2_digitos_ano // 4
        + B
        + l
        + codigos_meses[mes]
        + dia
    ) % 7

    match DIA_DA_SEMANA:
        case 1:
            return "Segunda"
        case 2:
            return "Terça"
        case 3:
            return "Quarta"
        case 4:
            return "Quinta"
        case 5:
            return "Sexta"
        case 6:
            return "Sábado"
        case 0:
            return "Domingo"
        case _:
            return "Erro... :("


print(calc_dia_semana())
