class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        path = path.split("/")
        for op in path:
            if op == "" or op == ".":
                continue
            elif op == "..":
                if output:
                    output.pop()
            else:
                output.append(op)

        return "/" + '/'.join(output)