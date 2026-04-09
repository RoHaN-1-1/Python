class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        d_score = {}
        d_count = {}

        for i in range(0, len(letters), 1):
            num = ord(letters[i])
            d_score[letters[i]] = score[num - 97]


        for i in range(0, len(letters), 1):
            d_count[letters[i]] = letters.count(letters[i])


        max_score = 0
    

       
        for i in range(0, 2 ** len(words), 1): 
            current_score = 0
            temp_count = d_count.copy()
            valid_set = True

            for j in range(0, len(words), 1):
                
                power_of_two = 1
                for k in range(0, j, 1):
                    power_of_two *= 2
                
                if i & power_of_two:  
                    word = words[j]

                    
                    for char in word:
                        if temp_count.get(char, 0) > 0:
                            temp_count[char] -= 1
                            current_score += d_score[char]
                        else:
                            valid_set = False
                            break

                    if not valid_set:
                        break

            if valid_set:
                max_score = max(max_score, current_score)

        return max_score