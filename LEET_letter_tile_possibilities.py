from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = 0
        for i in range(1, len(tiles) + 1):
            answer += len(set(x for x in permutations(tiles, i)))
        return answer
