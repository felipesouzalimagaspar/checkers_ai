from board import default, bprint, diagonal, brc
from move import check
#bprint(default())

#print(check(5,1,4,0,default()))
#print(check(2,1,3,0,default()))

#bprint(brc())

def test_moves(board, moves):
    for x0, y0, x, y, expected_result in moves:
        result = check(x0, y0, x, y, board)
        if result == expected_result:
            print(f"Movimento ({x0}, {y0}) para ({x}, {y}) foi validado corretamente.")
        else:
            print(f"Movimento ({x0}, {y0}) para ({x}, {y}) foi validado incorretamente. Deveria ser {expected_result} e deu {result}")
            bprint(board)

# Instância 1: Movimento válido de peão preto
board1 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1]
]
moves1 = [
    (2, 3, 3, 4,True),  # Movimento válido de peão branco
    (6, 0, 5, 1, True),  # Movimento válido de peão preto
    (1, 0, 2, 0, False),  # Movimento inválido - mesma coluna peão branco
    (1, 0, 2, 1, False),  # Movimento inválido - mesma diagonal peão branco
]

# Instância 2: Movimento válido de peão branco
board2 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
moves2 = [
    (2, 3, 3, 4, True),  # Movimento válido de peão branco
    (2, 5, 3, 6, True),  # Movimento válido de peão branco
    (2, 3, 1, 4, False),  # Movimento inválido - casa ocupoada
    (2, 3, 3, 3, False),  # Movimento inválido - mesma coluna
]

# Instância 3: Movimento inválido - célula ocupada
board3 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
moves3 = [
    (0, 1, 1, 2, False),  # Movimento inválido - célula ocupada por peça branca
    (6, 5, 5, 4, True),  # Movimento válido de peão preto
    (2, 0, 3, 1, False),  # Movimento inválido de célula vazia
]

board4 = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]
moves4 = [
    #comer duas peças em salto não funciona
    #(2, 1, 6, 5,True),  # Movimento válido comendo duas peças
    (2, 1, 4, 3,True),  # Movimento válido comendo duas peças - salto 1
    (4, 3, 6, 5,True),  # Movimento válido comendo duas peças - salto 2
    #(6, 0, 5, 1, True),  # Movimento válido de peão preto
]

# Você pode adicionar mais instâncias de teste conforme necessário


# Você pode adicionar mais instâncias de teste conforme necessário


#test_moves(board1, moves1)
#test_moves(board2, moves2)
#test_moves(board3, moves3)
test_moves(board4, moves4)