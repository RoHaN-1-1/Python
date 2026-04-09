class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = list(range(1,len(score)+1))
        z = list(zip(score,a))
        top_three = ["Gold Medal","Silver Medal","Bronze Medal"]
        remain = list(range(4,len(score)+1))
        medal = top_three + remain
        z.sort(reverse = True)
        score1, a1 = zip(*z)
        ans = list(zip(a1,medal))
        ans.sort()
        a2, medal2 = zip(*ans)
        return list(map(str,medal2))