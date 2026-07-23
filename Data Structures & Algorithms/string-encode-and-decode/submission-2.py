class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            length = len(word)
            output.append(f"{length}#{word}")

        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            output.append(word)
            i = j+1+length
        return output