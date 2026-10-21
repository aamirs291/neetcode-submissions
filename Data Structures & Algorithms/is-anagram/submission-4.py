class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        first_map = {}
        second_map = {}

        for char in s:
            first_map[char] = first_map.get(char, 0) + 1
        
        for char in t:
            second_map[char] = second_map.get(char, 0) + 1
        

        if first_map == second_map:
            return True
        
        return False

        