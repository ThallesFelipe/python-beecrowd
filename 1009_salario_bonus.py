_nome = input()
salario_fixo = float(input())
total_vendas_efetuadas_mes = float(input())

comissao = total_vendas_efetuadas_mes * 0.15

salario_com_comissao = salario_fixo + comissao
print(f"TOTAL = R$ {salario_com_comissao:.2f}")
