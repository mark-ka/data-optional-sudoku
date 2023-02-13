# pylint: disable=missing-docstring


def sudoku_validator(grid):
    #checking the rows:
    for row in grid:
        for num in range(1,10):
            if num in row:
                print(f'{num} is in row.nr.{num}!')
            else:
                return False

    #checking the collums:
    for col in range(9):
        col_li = []
        for row in range(9):
            col_li.append(grid[row][col])
            print(col_li)
        for num in range(1,10):
            if num in col_li:
                print(f'{num} is in collum.nr.{col+1}!')
            else:
                return False

    #checking the blocks:
    for shift_1 in range(0,9,3):
        for shift_2 in range(0,9,3):
            block_li = []
            for row in range(3):
                for col in range(3):
                    block_li.append(grid[row+shift_1][col+shift_2])
                    print(block_li)
            for num in range(1,10):
                if num in block_li:
                    print(f'{num} is in block nr.{block_li}!')
                else:
                    return False
        return True
