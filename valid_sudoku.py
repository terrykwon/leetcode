
# board2 = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'],
#           ['1','2','3','4','5','6','7','8','9'], ]

board = [".87654321",
         "2........",
         "3........",
         "4........",
         "5........",
         "6........",
         "7........",
         "8........",
         "9........"]


def isValidSudoku():
    board2 = list(map(list, board))
    vals = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    rows = [[] for c in range(0, 9)]
    cols = [[] for a in range(0, 9)]
    houses = [[] for b in range(0, 9)]

    for i in range(0, len(board2)):
        for j in range(0, len(board2[0])):
            if board2[i][j] != '.':
                rows[i].append(board2[i][j])
                cols[j].append(board2[i][j])

                x = i // 3
                y = j // 3
                houses[x * 3 + y].append(board2[i][j])

    # Check each row for duplicate numbers
    for r in rows:
        r_vals = set(r)
        if not (len(r_vals) == len(r)) or not (r_vals.issubset(vals)):
            return False

    for c in cols:
        c_vals = set(c)
        if not (len(c_vals) == len(c)) or not (c_vals.issubset(vals)):
            return False

    for h in houses:
        h_vals = set(h)
        if not (len(h_vals) == len(h)) or not (h_vals.issubset(vals)):
            return False

    return True

print(isValidSudoku())


