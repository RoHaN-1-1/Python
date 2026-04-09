class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]

        ans = []
        i = set(words[0])

        for char in i:
            common = min([j.count(char) for j in words])
            ans += common * [char]

        return ans