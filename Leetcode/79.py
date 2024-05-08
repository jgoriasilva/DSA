class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # find beginnings
        
        def possible_moves(position: tuple[int], seen: set[tuple[int]]) -> list[tuple[int]]:
            return [(i, j) for i, j in [[position[0], position[1]-1], [position[0], position[1]+1], [position[0]-1, position[1]], [position[0]+1, position[1]]] if (i, j) not in seen and 0 <= i < len(board) and 0 <= j < len(board[0])]

        def backtrack(moves: list[tuple[int]], letter_i: int, seen: set[tuple[int]]) -> bool:
            if letter_i >= len(word): 
                return True
            new_moves = [(i, j) for i, j in moves if board[i][j] == word[letter_i]]
            for move in new_moves:
                seen.add(move)
                possibles = possible_moves(move, seen)
                # for possible in possibles:
                if backtrack(possibles, letter_i+1, seen):
                    return True
                else: seen.remove(move)
            return False

        beginnings = [(i, j) for i, row in enumerate(board) for j, letter in enumerate(row)]
        # print(beginnings)
        return backtrack(beginnings, 0, set())

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
solution = Solution().exist(board, word)
print(solution)