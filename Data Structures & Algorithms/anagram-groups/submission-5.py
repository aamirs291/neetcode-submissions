class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_freq = [0]*26
        res = []
        res_map = {}

        for word in strs:
            word_freq = [0]*26
            for char in word:
                pos = ord(char) - ord('a')
                word_freq[pos]+=1
            
            key = tuple(word_freq)

            res_map[key] = res_map.get(key, [])
            res_map[key].append(word)


        return list(res_map.values())
        