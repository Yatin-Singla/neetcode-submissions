class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = []
        operators = {'+': lambda x,y : x+y,\
                     '-': lambda x,y : x-y,\
                     '*': lambda x,y : x*y,\
                     '/': lambda x,y : int(x/y)
                     }
        for i in range(len(tokens)):
            op = tokens[i]
            if op in operators:
                num2 = output.pop()
                num1 = output.pop()
                ans = operators[op](num1, num2)
                output.append(ans)
            else:
                output.append(int(op))

        return output.pop()