class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid and asteroid < 0 and stack[-1] > 0:
                comet = stack.pop()
                if abs(asteroid) < abs(comet):
                    asteroid = comet
                elif abs(asteroid) == abs(comet):
                    asteroid = None

            if asteroid:
                stack.append(asteroid)

        return stack