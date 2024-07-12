'''
Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.
Nota:

Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
Solo le celle riempite devono essere convalidate secondo le regole menzionate.
'''

def valid_sudoku(board: list[list[str]]) -> bool:
    for row in range(9):
        elements = []
        for col in range(9):
            num = board[row][col]
            if num != '.':
                if num in elements:
                    return False
                elements.append(num)

    for col in range(9):
        elements = []
        for row in range(9):
            num = board[row][col]
            if num != '.':
                if num in elements:
                    return False
                elements.append(num)

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            elements = []
            for r in range(3):
                for c in range(3):
                    num = board[row + r][col + c]
                    if num != '.':
                        if num in elements:
                            return False
                        elements.append(num)

    return True


# Test

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))  # output: True


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))  # output: False