#Chess | No En Passant | No Castling | No Draw By Insufficient Material | No Queening | Checkmate & Stalemate |
import sys

column_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
}

chess_board = [
    ['BR', 'BK', 'BB', 'BQ', 'BKI', 'BB', 'BK', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    [ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
    [ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
    [ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
    [ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR', 'WK', 'WB', 'WQ', 'WKI', 'WB', 'WK', 'WR']
]

moves_board =[
         ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
         ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
         ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
         ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
         ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
         ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
         ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
         ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        ]

valid_moves = [square for row in moves_board for square in row]

valid_pieces = [
    'WP', 'WR', 'WB', 'WK', 'WQ', 'WKI',
    'BP', 'BR', 'BB', 'BK', 'BQ', 'BKI'
]

def white_move():
    print('White Moves')
    move = input('What is your move: ')
    if not move.startswith('W'):
        print('White moves')
        move = input('What is your move?')
    if move.startswith('WKI'):
        while move[-2:] not in valid_moves or move[-4:-2] not in valid_moves or len(move) != 7:
            print('Invalid Move')
            move = input('What is your move?')
    else:
        while move[-2:] not in valid_moves or move[-4:-2] not in valid_moves or len(move) != 6:
            print('Invalid Move')
            move = input('What is your move?')
    row, col = find_position(move[-4:-2], moves_board)
    if move.startswith('WKI'):
        piece_code = move[:3]
    else:
        piece_code = move[:2]
    if chess_board[row][col] != piece_code:
        print(f'No {piece_code} at position {move[-4:-2]}')
        white_move()
    WB = 'White'
    to_row, to_col = find_position(move[-2:], moves_board)
    if chess_board[to_row][to_col] == 'BKI':
        print('Invalid Move')
        white_move()
    move_piece(move, chess_board, moves_board, WB)
    print_board(chess_board)

def black_move():
    print('Black Moves')
    move = input('What is your move: ')
    if not move.startswith('B'):
        print('Black moves')
        move = input('What is your move?')
    if move.startswith('BKI'):
        while move[-2:] not in valid_moves or move[-4:-2] not in valid_moves or len(move) != 7:
            print('Invalid Move')
            move = input('What is your move?')
    else:
        while move[-2:] not in valid_moves or move[-4:-2] not in valid_moves or len(move) != 6:
            print('Invalid Move')
            move = input('What is your move?')
    row, col = find_position(move[-4:-2], moves_board)
    if move.startswith('BKI'):
        piece_code = move[:3]
    else:
        piece_code = move[:2]

    if chess_board[row][col] != piece_code:
        print(f'No {piece_code} at position {move[-4:-2]}')
        black_move()
    WB = 'Black'
    to_row, to_col = find_position(move[-2:], moves_board)
    if chess_board[to_row][to_col] == 'WKI':
        print('Invalid Move')
        black_move()
        return
    move_piece(move, chess_board, moves_board, WB)
    print_board(chess_board)

def print_board(board):
    print()
    str_board = ""
    for row in board:
        for col in row:
            str_board += str(col)
            if str(col) == '0':
                str_board += " "
            str_board += " "
        str_board += '\n'
    print(str_board)

def find_position(square, moves_board):
    #Returns Row and Column Index of Square
    for row_index, row in enumerate(moves_board):
        if square in row:
            col_index = row.index(square)
            return (row_index, col_index)
    return None

def move_piece(move, chess_board, moves_board, WB):
    #Validate the logical boundary of the move.
    #Move input e.g WPe2e4 - White Pawn from e2 to e4
    from_pos = move[-4:-2]
    piece = move[:3] if move.startswith('WKI') or move.startswith('BKI') else move[:2]
    current_row, current_col = find_position(from_pos, moves_board)

    if chess_board[current_row][current_col] == piece:
        if chess_board[current_row][current_col] == piece:
            if piece == 'WP' or piece == 'BP':
                pawn_move(move, chess_board, moves_board, WB)
            elif piece == 'WB' or piece == 'BB':
                bishop_move(move, chess_board, moves_board, WB)
            elif piece == 'WR' or piece == 'BR':
                rook_move(move, chess_board, moves_board, WB)
            elif piece == 'WK' or piece == 'BK':
                knight_move(move, chess_board, moves_board, WB)
            elif piece == 'WKI' or piece == 'BKI':
                king_move(move, chess_board, moves_board, WB)
            elif piece == 'WQ' or piece == 'BQ':
                queen_move(move, chess_board, moves_board, WB)
    else:
        '''Invalid Move'''
        print('Invalid Move')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def pawn_move(move, chess_board, moves_board, WB):
    from_pos = move[-4:-2]
    to_pos = move[-2:]
    from_row, from_col = find_position(from_pos, moves_board)
    capture_position = find_position(to_pos, moves_board)
    valid_pawn_moves = allowable_pawn_moves(from_pos, chess_board, moves_board, WB)
    if capture_position in valid_pawn_moves:
        '''Valid Pawn Move'''
        chess_board[from_row][from_col] = 0
        if WB == 'White':
            chess_board[capture_position[0]][capture_position[1]] = 'WP'
        else:
            chess_board[capture_position[0]][capture_position[1]] = 'BP'
    else:
        print('Invalid Move')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_pawn_moves(from_pos, chess_board, moves_board, WB):
   #Returns an Array of Legal Pawn Moves
    allowable_pawn_moves = []
    current_position = find_position(from_pos, moves_board)
    current_row, current_col = find_position(from_pos, moves_board)
    '''Starting Position - Move 1 or 2 Up'''
    '''White'''
    if WB == 'White':
        if current_row == 6:
            '''If both front spaces are empty [Complete]'''
            if not (current_row - 1 > 7 or current_row - 1 < 0 or current_col - 2 > 7 or current_col - 2 < 0):
                if chess_board[current_row-1][current_col] == 0 and chess_board[current_row-2][current_col] == 0:
                    allowable_pawn_moves.append((current_row-2, current_col))
                if chess_board[current_row-1][current_col] == 0:
                    allowable_pawn_moves.append((current_row - 1, current_col))
        '''Non Starting Position - Move 1 Up [Complete]'''
        if not (current_row -1 > 7 or current_row - 1 < 0):
            if chess_board[current_row-1][current_col] == 0:
                allowable_pawn_moves.append((current_row - 1, current_col))
        '''Left Capture [Complete]'''
        if not (current_row - 1 > 7 or current_row - 1 < 0 or current_col - 1 > 7 or current_col - 1 < 0):
            if chess_board[current_row-1][current_col - 1] != 0:
                    if chess_board[current_row-1][current_col - 1].startswith('B'):
                        '''Capturable Black Pawn'''
                        allowable_pawn_moves.append((current_row - 1, current_col - 1))
        '''Right Capture [Complete]'''
        if not (current_row - 1 > 7 or current_row - 1 < 0 or current_col + 1 > 7):
            if chess_board[current_row-1][current_col + 1] != 0:
                if chess_board[current_row-1][current_col + 1].startswith('B'):
                    '''Capturable Black Pawn'''
                    allowable_pawn_moves.append((current_row-1, current_col+1))
        if current_position in allowable_pawn_moves:
            del allowable_pawn_moves[allowable_pawn_moves.index(current_position)]
    '''Black'''
    if WB == 'Black':
        if current_row == 1:
            '''If both front spaces are empty [Complete]'''
            if not (current_row + 1 > 7 or current_row + 1 < 0 or current_col + 2 > 7 or current_col + 2 < 0):
                if chess_board[current_row+1][current_col] == 0 and chess_board[current_row+2][current_col] == 0:
                    allowable_pawn_moves.append((current_row+2, current_col))
                if chess_board[current_row+1][current_col] == 0:
                    allowable_pawn_moves.append((current_row + 1, current_col))
        '''Non Starting Position - Move 1 Up [Complete]'''
        if not (current_row  + 1 > 7 or current_row + 1 < 0):
            if chess_board[current_row+1][current_col] == 0:
                allowable_pawn_moves.append((current_row + 1, current_col))
        '''Left Capture [Complete]'''
        if not (current_row + 1 > 7 or current_row + 1 < 0 or current_col - 1 > 7 or current_col - 1 < 0):
            if chess_board[current_row+1][current_col - 1] != 0:
                    if chess_board[current_row+1][current_col - 1].startswith('W'):
                        '''Capturable White Pawn'''
                        allowable_pawn_moves.append((current_row + 1, current_col - 1))
        '''Right Capture'''
        if not (current_row + 1 > 7 or current_row + 1 < 0 or current_col + 1 > 7):
            if chess_board[current_row+1][current_col + 1] != 0:
                if chess_board[current_row+1][current_col + 1].startswith('W'):
                    '''Capturable White Pawn'''
                    allowable_pawn_moves.append((current_row+1, current_col+1))
        if current_position in allowable_pawn_moves:
            del allowable_pawn_moves[allowable_pawn_moves.index(current_position)]
    allowable_pawn_moves = list(set(allowable_pawn_moves))
    return allowable_pawn_moves

def pawn_capture(from_pos, to_pos, piece, move_length, chess_board, moves_board, WB):
    #Handles Pawn Captures (Diagonals)
    if move_length >= 2 or move_length == 0:
        print('Invalid Move')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return
    '''White Capture'''
    current_row, current_col = find_position(from_pos, moves_board)
    capture = find_position(to_pos, moves_board)
    if WB == 'White':
        left_capture_row = current_row - 1
        left_capture_col = current_col - 1

        right_capture_row = current_row - 1
        right_capture_col = current_col + 1
        right_cap = (right_capture_row, right_capture_col)
        left_cap = (left_capture_row, left_capture_col)
        if capture == left_cap or capture == right_cap:
            chess_board[current_row][current_col] = 0
            capture_row = capture[0]
            capture_col = capture[1]
            chess_board[capture_row][capture_col] = piece
        return chess_board
    '''Black Capture'''
    if WB == 'Black':
        left_capture_row = current_row + 1
        left_capture_col = current_col - 1

        right_capture_row = current_row + 1
        right_capture_col = current_col + 1
        right_cap = (right_capture_row, right_capture_col)
        left_cap = (left_capture_row, left_capture_col)
        if capture == left_cap or capture == right_cap:
            chess_board[current_row][current_col] = 0
            capture_row = capture[0]
            capture_col = capture[1]
            chess_board[capture_row][capture_col] = piece
        return chess_board

def bishop_move(move, chess_board, moves_board, WB):
    allowed_bishop_moves = allowable_bishop_moves(move, chess_board, moves_board, WB)
    to_pos = move[-2:]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    piece = move[:2]
    actual_move = find_position(to_pos, moves_board)
    if actual_move in allowed_bishop_moves:
        chess_board[actual_move[0]][actual_move[1]] = piece
        chess_board[from_row][from_col] = 0
    else:
        '''Invalid Move'''
        print('Invalid Move')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_bishop_moves(move, chess_board, moves_board, WB):
    #Returns an Array of Legal Bishop Moves
    piece = move[:2]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    to_pos = move[-2:]
    if WB == 'White' or WB == 'Black':
        cur_row = from_row -1
        cur_col = from_col -1
        allowable_moves = []
        '''Top Left Validation'''
        while cur_row >= 0 and cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row -= 1
            cur_col -= 1
        cur_row = from_row -1
        cur_col = from_col + 1
        '''Top Right Validation'''
        while cur_row >= 0 and cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row -= 1
            cur_col += 1
        '''Bottom Left Validation'''
        cur_row = from_row + 1
        cur_col = from_col - 1
        while cur_row <= 7 and cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row += 1
            cur_col -= 1
        '''Bottom Right Validation'''
        cur_row = from_row + 1
        cur_col = from_col + 1
        while cur_row <= 7 and cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row += 1
            cur_col += 1
        return allowable_moves

def rook_move(move, chess_board, moves_board, WB):
    allowed_rook_moves = allowable_rook_moves(move, chess_board, moves_board, WB)
    to_pos = move[-2:]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    piece = move[:2]
    actual_move = find_position(to_pos, moves_board)
    if actual_move in allowed_rook_moves:
        chess_board[actual_move[0]][actual_move[1]] = piece
        chess_board[from_row][from_col] = 0
    else:
        '''Invalid Move'''
        print('Invalid Move11')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_rook_moves(move, chess_board, moves_board, WB):
    #Returns An Array of Legal Rook Moves
    allowable_moves = []
    piece = move[:2]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    '''White Rook Logic'''
    if WB == 'White':
        '''Straight Up Validation'''
        cur_row = from_row -1
        cur_col = from_col
        while cur_row >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row -= 1
        '''Straight Down Validation'''
        cur_row = from_row + 1
        while cur_row <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row += 1
        '''Straight Left Validation'''
        cur_row = from_row
        cur_col = from_col - 1
        while cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col -= 1
        '''Straight Right Validation'''
        cur_col = from_col + 1
        while cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col += 1
        return allowable_moves
    else:
        '''Black Rook Logic'''
        '''Straight Up Validation'''
        cur_row = from_row + 1
        cur_col = from_col
        while cur_row <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row += 1
        '''Straight Down Validation'''
        cur_row = from_row - 1
        while cur_row >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row -= 1
        '''Straight Left Validation'''
        cur_row = from_row
        cur_col = from_col - 1
        while cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col -= 1
        '''Straight Right Validation'''
        cur_col = from_col + 1
        while cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col += 1
    return allowable_moves

def knight_move(move, chess_board, moves_board, WB):
    allowed_knight_moves = allowable_knight_moves(move, chess_board, moves_board, WB)
    to_pos = move[-2:]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    piece = move[:2]
    actual_move = find_position(to_pos, moves_board)
    if actual_move in allowed_knight_moves:
        chess_board[actual_move[0]][actual_move[1]] = piece
        chess_board[from_row][from_col] = 0
    else:
        '''Invalid Move'''
        print('Invalid Move12')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_knight_moves(move, chess_board, moves_board, WB):
    #Returns an Array of Legal Knight Moves
    allowed_knight_moves = []
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    '''For White'''
    '''Top Moves'''
    if WB == 'White':
        # Top Left 1
        new_row = from_row - 2
        new_col = from_col - 1
        if new_row >= 0 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Top Right 1
        new_row = from_row - 2
        new_col = from_col + 1
        if new_row >= 0 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Top Left 2
        new_row = from_row - 1
        new_col = from_col - 2
        if new_row >= 0 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        #Top Right 2
        new_row = from_row - 1
        new_col = from_col + 2
        if new_row >= 0 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        '''Bottom Moves'''
        #Bottom Left 1
        new_row = from_row + 2
        new_col = from_col - 1
        if new_row <= 7 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        #Bottom Right 1
        new_row = from_row + 2
        new_col = from_col + 1
        if new_row <= 7 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        #Bottom Left 2
        new_row = from_row + 1
        new_col = from_col  - 2
        if new_row <= 7 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        #Bottom Right 2
        new_row = from_row + 1
        new_col = from_col + 2
        if new_row <= 7 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
    if (from_row, from_col) in allowed_knight_moves:
        allowed_knight_moves.remove((from_row, from_col))
    else:
        '''For Black'''
        # Top Left 1
        new_row = from_row + 2
        new_col = from_col - 1
        if new_row <= 7 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Top Right 1
        new_row = from_row + 2
        new_col = from_col + 1
        if new_row <= 7 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Top Left 2
        new_row = from_row + 1
        new_col = from_col - 2
        if new_row <= 7 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Top Right 2
        new_row = from_row + 1
        new_col = from_col + 2
        if new_row <= 7 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        '''Bottom Moves'''
        # Bottom Left 1
        new_row = from_row - 2
        new_col = from_col - 1
        if new_row >= 0 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Bottom Right 1
        new_row = from_row - 2
        new_col = from_col + 1
        if new_row >= 0 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Bottom Left 2
        new_row = from_row - 1
        new_col = from_col - 2
        if new_row >= 0 and new_col >= 0:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
        # Bottom Right 2
        new_row = from_row - 1
        new_col = from_col + 2
        if new_row >= 0 and new_col <= 7:
            if chess_board[new_row][new_col] == 0:
                '''Valid Move'''
                allowed_knight_moves.append((new_row, new_col))
            else:
                if chess_board[new_row][new_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowed_knight_moves.append((new_row, new_col))
                else:
                    pass
    if (from_row, from_col) in allowed_knight_moves:
        allowed_knight_moves.remove((from_row, from_col))
    return allowed_knight_moves

def queen_move(move, chess_board, moves_bard, WB):
    allowed_queen_moves = allowable_queen_moves(move, chess_board, moves_board, WB)
    to_pos = move[-2:]
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    piece = move[:2]
    actual_move = find_position(to_pos, moves_board)
    if actual_move in allowed_queen_moves:
        chess_board[actual_move[0]][actual_move[1]] = piece
        chess_board[from_row][from_col] = 0
    else:
        '''Invalid Move'''
        print('Invalid Move13')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_queen_moves(move, chess_board, moves_board, WB):
    #Returns an Array of Legal Queen Moves
    #Queen - Bishop + Rook
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    '''Bishop Movement'''
    if WB == 'White' or WB == 'Black':
        cur_row = from_row - 1
        cur_col = from_col - 1
        allowable_moves = []
        '''Top Left Validation'''
        while cur_row >= 0 and cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row -= 1
            cur_col -= 1
        cur_row = from_row - 1
        cur_col = from_col + 1
        '''Top Right Validation'''
        while cur_row >= 0 and cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row -= 1
            cur_col += 1
        '''Bottom Left Validation'''
        cur_row = from_row + 1
        cur_col = from_col - 1
        while cur_row <= 7 and cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row += 1
            cur_col -= 1
        '''Bottom Right Validation'''
        cur_row = from_row + 1
        cur_col = from_col + 1
        while cur_row <= 7 and cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                '''Capture'''
                if WB == 'White':
                    if chess_board[cur_row][cur_col].startswith('W'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
                elif WB == 'Black':
                    if chess_board[cur_row][cur_col].startswith('B'):
                        break
                    else:
                        allowable_moves.append((cur_row, cur_col))
                        break
            cur_row += 1
            cur_col += 1
    '''Rook Movement'''
    if WB == 'White':
        '''Straight Up Validation'''
        cur_row = from_row -1
        cur_col = from_col
        while cur_row >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row -= 1
        '''Straight Down Validation'''
        cur_row = from_row + 1
        while cur_row <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row += 1
        '''Straight Left Validation'''
        cur_row = from_row
        cur_col = from_col - 1
        while cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col -= 1
        '''Straight Right Validation'''
        cur_col = from_col + 1
        while cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('B'):
                    '''Capturable Black Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col += 1
        return allowable_moves
    else:
        '''Black Rook Logic'''
        '''Straight Up Validation'''
        cur_row = from_row + 1
        cur_col = from_col
        while cur_row <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row += 1
        '''Straight Down Validation'''
        cur_row = from_row - 1
        while cur_row >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_row -= 1
        '''Straight Left Validation'''
        cur_row = from_row
        cur_col = from_col - 1
        while cur_col >= 0:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col -= 1
        '''Straight Right Validation'''
        cur_col = from_col + 1
        while cur_col <= 7:
            if chess_board[cur_row][cur_col] == 0:
                allowable_moves.append((cur_row, cur_col))
            else:
                if chess_board[cur_row][cur_col].startswith('W'):
                    '''Capturable White Piece'''
                    allowable_moves.append((cur_row, cur_col))
                    break
                else:
                    break
            cur_col += 1
    return allowable_moves

def check_black_king_check():
    #Handles Black King Checks
    check = False
    for row_index in range(len(chess_board)):
        for col_index in range(len(chess_board[row_index])):
            if chess_board[row_index][col_index] == 'BKI':
                row = row_index
                col = col_index
                white_capture = capturable_square('White')
                if (row, col) in white_capture:
                    print('Black King in Check!')
                    check = True
    if check:
        check_black_king_checkmate((row,col))
    if not check:
        check_black_king_stalemate((row,col))

def check_white_king_check():
    #Handles White King Checks
    check = False
    for row_index in range(len(chess_board)):
        for col_index in range(len(chess_board[row_index])):
            if chess_board[row_index][col_index] == 'WKI':
                row = row_index
                col = col_index
                '''If Black - Find All Capturable Pieces CURRENTLY by Black'''
                black_capture = capturable_square('Black')
                if (row, col) in black_capture:
                    print('White King in Check!')
                    check = True
    if check:
        check_white_king_checkmate((row,col))
    if not check:
        check_white_king_stalemate((row,col))

def check_black_king_stalemate(pos):
    #Handles Stalemates on the Black Side
    import sys
    all_legal_black_moves = capturable_square('Black')
    all_legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'Black')
    if len(all_legal_black_moves) > len(all_legal_king_moves):
        pass
    if all_legal_black_moves == all_legal_king_moves:
        '''Stalemate if All Potentuial king moves are dangeorus ()'''
        legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'Black')
        for move in legal_king_moves:
            board = copy.deepcopy(chess_board)
            board[move[0]][move[1]] = 'BKI'
            board[pos[0]][pos[1]] = 0
            new_capture = capturable_square('White', board)
            '''If Move in New_Capture - Non Legal Move'''
            if move in new_capture:
                legal_king_moves.remove(move)
        if legal_king_moves == []:
            print('Stalemate')
            sys.exit()

def check_white_king_stalemate(pos):
    #Handles Stalemates on the White Side
    import sys
    all_legal_white_moves = capturable_square('White')
    all_legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'White')
    if len(all_legal_white_moves) > len(all_legal_king_moves):
        pass
    if all_legal_white_moves == all_legal_king_moves:
        '''Stalemate if All Potentuial king moves are dangeorus ()'''
        legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'White')
        for move in legal_king_moves:
            board = copy.deepcopy(chess_board)
            board[move[0]][move[1]] = 'WKI'
            board[pos[0]][pos[1]] = 0
            new_capture = capturable_square('Black', board)
            '''If Move in New_Capture - Non Legal Move'''
            if move in new_capture:
                legal_king_moves.remove(move)
        if legal_king_moves == []:
            print('Stalemate')
            sys.exit()

def check_black_king_checkmate(pos):
    #Handles Checkmates on the Black Side
    import copy
    import sys

    protection_array = []
    legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'Black')

    filtered_king_moves = []
    for move in legal_king_moves:
        board = copy.deepcopy(chess_board)
        board[move[0]][move[1]] = 'BKI'
        board[pos[0]][pos[1]] = 0
        new_capture = capturable_square('White', board)
        if move not in new_capture:
            filtered_king_moves.append(move)
    legal_king_moves = filtered_king_moves

    if legal_king_moves == []:
        for r in range(8):
            for c in range(8):
                piece = chess_board[r][c]
                if isinstance(piece, str) and piece.startswith('B') and piece != 'BKI':
                    from_square = moves_board[r][c]
                    dummy_target = 'f6'
                    move_string = piece + from_square + dummy_target

                    if piece == 'BR':
                        moves = allowable_rook_moves(move_string, chess_board, moves_board, 'Black')
                    elif piece == 'BK':
                        moves = allowable_knight_moves(move_string, chess_board, moves_board, 'Black')
                    elif piece == 'BB':
                        moves = allowable_bishop_moves(move_string, chess_board, moves_board, 'Black')
                    elif piece == 'BP':
                        moves = allowable_pawn_moves(from_square, chess_board, moves_board, 'Black')
                    elif piece == 'WQ':
                        moves = allowable_queen_moves(move_string, chess_board, moves_board, 'Black')
                    else:
                        continue

                    for to_row, to_col in moves:
                        test_board = copy.deepcopy(chess_board)
                        test_board[to_row][to_col] = piece
                        test_board[r][c] = 0
                        white_threats = capturable_square('White', test_board)
                        if pos not in white_threats:
                            protection_array.append([piece, from_square, moves_board[to_row][to_col]])

    if legal_king_moves == [] and protection_array == []:
        print('Checkmate - Black Loses')
        sys.exit()

    while True:
        move = input("What is your move: ")

        if move.startswith("BKI"):
            piece = "BKI"
            from_square = move[3:5]
            to_square = move[5:7]
            from_row, from_col = find_position(from_square, moves_board)
            to_row, to_col = find_position(to_square, moves_board)

            if [to_row, to_col] not in legal_king_moves:
                print("Invalid Move")
                continue

            chess_board[from_row][from_col] = 0
            chess_board[to_row][to_col] = 'BKI'
            print_board(chess_board)
            white_move()
            return

        else:
            piece = move[:2]
            from_square = move[2:4]
            to_square = move[4:6]
            move_arr = [piece, from_square, to_square]

            if move_arr not in protection_array:
                print("Invalid Move")
                continue

            from_row, from_col = find_position(from_square, moves_board)
            to_row, to_col = find_position(to_square, moves_board)

            test_board = copy.deepcopy(chess_board)
            test_board[from_row][from_col] = 0
            test_board[to_row][to_col] = piece
            white_threats = capturable_square('White', test_board)

            if pos in white_threats:
                print("Invalid Move")
                continue

            chess_board[from_row][from_col] = 0
            chess_board[to_row][to_col] = piece
            print_board(chess_board)
            white_move()
            return

def check_white_king_checkmate(pos):
    #Handles Checkmates on the Black Side
    import copy
    import sys

    protection_array = []
    legal_king_moves = allowable_king_moves(pos, chess_board, moves_board, 'White')

    filtered_king_moves = []
    for move in legal_king_moves:
        board = copy.deepcopy(chess_board)
        board[move[0]][move[1]] = 'WKI'
        board[pos[0]][pos[1]] = 0
        new_capture = capturable_square('Black', board)
        if move not in new_capture:
            filtered_king_moves.append(move)
    legal_king_moves = filtered_king_moves

    if legal_king_moves == []:
        for r in range(8):
            for c in range(8):
                piece = chess_board[r][c]
                if isinstance(piece, str) and piece.startswith('W') and piece != 'WKI':
                    from_square = moves_board[r][c]
                    dummy_target = 'f6'
                    move_string = piece + from_square + dummy_target

                    if piece == 'WR':
                        moves = allowable_rook_moves(move_string, chess_board, moves_board, 'White')
                    elif piece == 'WK':
                        moves = allowable_knight_moves(move_string, chess_board, moves_board, 'White')
                    elif piece == 'WB':
                        moves = allowable_bishop_moves(move_string, chess_board, moves_board, 'White')
                    elif piece == 'WP':
                        moves = allowable_pawn_moves(from_square, chess_board, moves_board, 'White')
                    elif piece == 'BQ':
                        moves = allowable_queen_moves(move_string, chess_board, moves_board, 'White')
                    else:
                        continue

                    for to_row, to_col in moves:
                        test_board = copy.deepcopy(chess_board)
                        test_board[to_row][to_col] = piece
                        test_board[r][c] = 0
                        black_threats = capturable_square('Black', test_board)
                        if pos not in black_threats:
                            protection_array.append([piece, from_square, moves_board[to_row][to_col]])

    if legal_king_moves == [] and protection_array == []:
        print('Checkmate - White Loses')
        sys.exit()

    while True:
        move = input("What is your move: ")

        if move.startswith("WKI"):
            piece = "WKI"
            from_square = move[3:5]
            to_square = move[5:7]
            from_row, from_col = find_position(from_square, moves_board)
            to_row, to_col = find_position(to_square, moves_board)

            if [to_row, to_col] not in legal_king_moves:
                print("Invalid Move")
                continue

            chess_board[from_row][from_col] = 0
            chess_board[to_row][to_col] = 'WKI'
            print_board(chess_board)
            black_move()
            return

        else:
            piece = move[:2]
            from_square = move[2:4]
            to_square = move[4:6]
            move_arr = [piece, from_square, to_square]

            if move_arr not in protection_array:
                print("Invalid Move")
                continue

            from_row, from_col = find_position(from_square, moves_board)
            to_row, to_col = find_position(to_square, moves_board)

            test_board = copy.deepcopy(chess_board)
            test_board[from_row][from_col] = 0
            test_board[to_row][to_col] = piece
            black_threats = capturable_square('Black', test_board)

            if pos in black_threats:
                print("Invalid Move")
                continue

            chess_board[from_row][from_col] = 0
            chess_board[to_row][to_col] = piece
            print_board(chess_board)
            black_move()
            return

def king_move(move, chess_board, moves_board, WB):
    from_pos = move[-4:-2]
    from_row, from_col = find_position(from_pos, moves_board)
    start_pos = (from_row, from_col)
    allowed_king_moves = allowable_king_moves(start_pos, chess_board, moves_board, WB)
    to_pos = move[-2:]
    piece = move[:3]
    actual_move = find_position(to_pos, moves_board)
    if actual_move in allowed_king_moves:
        chess_board[actual_move[0]][actual_move[1]] = piece
        chess_board[from_row][from_col] = 0
    else:
        '''Invalid Move'''
        print('Invalid Move16')
        if WB == 'White':
            white_move()
            print()
            return
        else:
            black_move()
            print()
            return

def allowable_king_moves(start_pos, chess_board, moves_board, WB):
    #Returns an Array of Legal King Moves
    from_row = start_pos[0]
    from_col = start_pos[1]
    legal_moves = []
    if WB == 'White':
        capturable_squares = capturable_square('Black')
        # Up
        if from_row - 1 >= 0:
            if chess_board[from_row - 1][from_col] == 0 or chess_board[from_row - 1][from_col].startswith('B'):
                legal_moves.append((from_row - 1, from_col))
        # Down
        if from_row + 1 <= 7:
            if chess_board[from_row + 1][from_col] == 0 or chess_board[from_row + 1][from_col].startswith('B'):
                legal_moves.append((from_row + 1, from_col))
        # Left
        if from_col - 1 >= 0:
            if chess_board[from_row][from_col - 1] == 0 or chess_board[from_row][from_col - 1].startswith('B'):
                legal_moves.append((from_row, from_col - 1))
        # Right
        if from_col + 1 <= 7:
            if chess_board[from_row][from_col + 1] == 0 or chess_board[from_row][from_col + 1].startswith('B'):
                legal_moves.append((from_row, from_col + 1))
        # Diagonals
        if from_row - 1 >= 0 and from_col - 1 >= 0:
            if chess_board[from_row - 1][from_col - 1] == 0 or chess_board[from_row - 1][from_col - 1].startswith('B'):
                legal_moves.append((from_row - 1, from_col - 1))
        if from_row - 1 >= 0 and from_col + 1 <= 7:
            if chess_board[from_row - 1][from_col + 1] == 0 or chess_board[from_row - 1][from_col + 1].startswith('B'):
                legal_moves.append((from_row - 1, from_col + 1))
        if from_row + 1 <= 7 and from_col - 1 >= 0:
            if chess_board[from_row + 1][from_col - 1] == 0 or chess_board[from_row + 1][from_col - 1].startswith('B'):
                legal_moves.append((from_row + 1, from_col - 1))
        if from_row + 1 <= 7 and from_col + 1 <= 7:
            if chess_board[from_row + 1][from_col + 1] == 0 or chess_board[from_row + 1][from_col + 1].startswith('B'):
                legal_moves.append((from_row + 1, from_col + 1))

    else:  # Black
        capturable_squares = capturable_square('White')
        # Up
        if from_row - 1 >= 0:
            if chess_board[from_row - 1][from_col] == 0 or chess_board[from_row - 1][from_col].startswith('W'):
                legal_moves.append((from_row - 1, from_col))
        # Down
        if from_row + 1 <= 7:
            if chess_board[from_row + 1][from_col] == 0 or chess_board[from_row + 1][from_col].startswith('W'):
                legal_moves.append((from_row + 1, from_col))
        # Left
        if from_col - 1 >= 0:
            if chess_board[from_row][from_col - 1] == 0 or chess_board[from_row][from_col - 1].startswith('W'):
                legal_moves.append((from_row, from_col - 1))
        # Right
        if from_col + 1 <= 7:
            if chess_board[from_row][from_col + 1] == 0 or chess_board[from_row][from_col + 1].startswith('W'):
                legal_moves.append((from_row, from_col + 1))
        # Diagonals
        if from_row - 1 >= 0 and from_col - 1 >= 0:
            if chess_board[from_row - 1][from_col - 1] == 0 or chess_board[from_row - 1][from_col - 1].startswith('W'):
                legal_moves.append((from_row - 1, from_col - 1))
        if from_row - 1 >= 0 and from_col + 1 <= 7:
            if chess_board[from_row - 1][from_col + 1] == 0 or chess_board[from_row - 1][from_col + 1].startswith('W'):
                legal_moves.append((from_row - 1, from_col + 1))
        if from_row + 1 <= 7 and from_col - 1 >= 0:
            if chess_board[from_row + 1][from_col - 1] == 0 or chess_board[from_row + 1][from_col - 1].startswith('W'):
                legal_moves.append((from_row + 1, from_col - 1))
        if from_row + 1 <= 7 and from_col + 1 <= 7:
            if chess_board[from_row + 1][from_col + 1] == 0 or chess_board[from_row + 1][from_col + 1].startswith('W'):
                legal_moves.append((from_row + 1, from_col + 1))

    for move in capturable_squares:
        if move in legal_moves:
            legal_moves.remove(move)

    return legal_moves

def capturable_square(WB, board=None):
    #Returns An Array of All Capturable Pieces (White/Black)
    if board is None:
        board = chess_board

    template = 'f6'
    arr = []

    if WB == 'White':
        # Get all squares attacked by White pieces (White attacks Black)
        for row_index in range(len(board)):
            for col_index in range(len(board[row_index])):
                piece = board[row_index][col_index]
                if str(piece).startswith('W'):
                    from_square = moves_board[row_index][col_index]
                    if str(piece) == 'WR':
                        move = piece + from_square + template
                        moves = allowable_rook_moves(move, board, moves_board, 'White')
                    elif str(piece) == 'WK':
                        move = piece + from_square + template
                        moves = allowable_knight_moves(move, board, moves_board, 'White')
                    elif str(piece) == 'WB':
                        move = piece + from_square + template
                        moves = allowable_bishop_moves(move, board, moves_board, 'White')
                    elif str(piece) == 'WP':
                        moves = allowable_pawn_moves(from_square, board, moves_board, 'White')
                    elif str(piece) == 'WQ':
                        move = piece + from_square + template
                        moves = allowable_queen_moves(move, board, moves_board, 'White')
                    else:
                        moves = None
                    if moves is not None:
                        arr.extend(moves)

    elif WB == 'Black':
        # Get all squares attacked by Black pieces (Black attacks White)
        for row_index in range(len(board)):
            for col_index in range(len(board[row_index])):
                piece = board[row_index][col_index]
                if str(piece).startswith('B'):
                    from_square = moves_board[row_index][col_index]
                    if str(piece) == 'BR':
                        move = piece + from_square + template
                        moves = allowable_rook_moves(move, board, moves_board, 'Black')
                    elif str(piece) == 'BK':
                        move = piece + from_square + template
                        moves = allowable_knight_moves(move, board, moves_board, 'Black')
                    elif str(piece) == 'BB':
                        move = piece + from_square + template
                        moves = allowable_bishop_moves(move, board, moves_board, 'Black')
                    elif str(piece) == 'BP':
                        moves = allowable_pawn_moves(from_square, board, moves_board, 'Black')
                    elif str(piece) == 'BQ':
                        move = piece + from_square + template
                        moves = allowable_queen_moves(move, board, moves_board, 'Black')
                    else:
                        moves = None

                    if moves is not None:
                        arr.extend(moves)

    return arr

def main():
  print('The format of each move is Piece, From Square, To Square')
  print('E.g. WPe2e4 -> White Pawn Moves from e2 to e4')
  print_board(chess_board)
  while True:
      white_move()
      check_black_king_check()
      black_move()
      check_white_king_check()

if __name__ == '__main__':
    main()