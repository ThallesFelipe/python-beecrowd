SENHA_CORRETA: str = "2002"

tentativa: str | None = None

while tentativa != SENHA_CORRETA:
    tentativa = input()

    if tentativa == SENHA_CORRETA:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
