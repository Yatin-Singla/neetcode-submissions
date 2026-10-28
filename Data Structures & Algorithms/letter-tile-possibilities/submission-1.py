class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        counter, unique = Counter(tiles), set()
        comb = []

        def combinations(n):
            if n == 0:
                unique.add("".join(comb))
                return
            
            for tile, freq in counter.items():
                if freq > 0:
                    comb.append(tile)
                    counter[tile] -= 1
                    combinations(n-1)
                    counter[tile] += 1
                    comb.pop()

        for n in range(1, len(tiles)+1):
            combinations(n)

        return len(unique)
            
