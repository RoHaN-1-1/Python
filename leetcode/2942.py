class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        letter = []
        for i in range(len(words)):
            if x in words[i]:
                letter.append(i)
        return letter   