class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_char_freq = {}
        for char in s1:
            s1_char_freq[char] = s1_char_freq.get(char, 0) + 1
        
        window_size = len(s1)
        s2_char_freq = {}
        
        # Initialize s2_char_freq for the first window in s2
        for i in range(window_size):
            s2_char_freq[s2[i]] = s2_char_freq.get(s2[i], 0) + 1
        
        # Compare initial window
        if s1_char_freq == s2_char_freq:
            return True
        
        # Slide the window across s2
        for r in range(1, len(s2) - window_size + 1):
            # Add the new character on the right
            s2_char_freq[s2[r + window_size - 1]] = s2_char_freq.get(s2[r + window_size - 1], 0) + 1
            
            # Remove the character that is sliding out from the left
            left_char = s2[r - 1]
            s2_char_freq[left_char] -= 1
            if s2_char_freq[left_char] == 0:
                del s2_char_freq[left_char]
            
            # Compare current window
            if s1_char_freq == s2_char_freq:
                return True
        
        return False