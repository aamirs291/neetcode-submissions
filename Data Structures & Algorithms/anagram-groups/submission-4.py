class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        word_map = {}

        for word in strs:
            freq_arr = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                freq_arr[idx]+=1
            key = tuple(freq_arr)
            word_map[key] = word_map.get(key, [])
            word_map[key].append(word)
        
        print(word_map.values())
        return list(word_map.values())