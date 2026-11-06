class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = set()
        ip = []

        def backtrack(idx, currNum, dots):
            if idx == len(s):
                if ip[-1] == ".":
                    return
                if dots != 0:
                    return
                output.add("".join(ip))
                return 
            
            currNum = currNum*10 + int(s[idx])
            ip.append(s[idx])

            if currNum == 0:
                if dots > 0:
                    ip.append(".")
                    backtrack(idx+1, 0, dots-1)
                    ip.pop()  
                elif idx == len(s)-1:
                    backtrack(idx+1, currNum, dots)
            elif currNum <= 255:
                backtrack(idx+1, currNum, dots)
                if dots > 0:
                    ip.append(".")
                    backtrack(idx+1, 0, dots-1)
                    ip.pop()
            ip.pop()

        backtrack(0, 0, 3)
        return list(output)