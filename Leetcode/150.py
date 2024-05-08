class Solution:
    def evalRPN(self, tokens: list[str]) -> int | None:

        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b,
        }
        
        stack = []
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))
        
        return stack.pop()            

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

triplets = Solution().evalRPN(tokens)

print(triplets)
