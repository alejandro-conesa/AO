def algoritmo_nim(fichas_tablero, max_retirada):
    if fichas_tablero <= max_retirada:
        return True
    else:
        for i in range(1, max_retirada+1):
            if not (algoritmo_nim(fichas_tablero-i, max_retirada)):
                return True
        return False

print(algoritmo_nim(4, 4))
print(algoritmo_nim(5, 4))