class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]

        pairs = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        
        pairs.sort(reverse=True)

        fleet = 1
        prev_time = (target-pairs[0][0])/pairs[0][1]

        for pos, speed in pairs:
            curr_time = (target-pos)/speed
            
            if curr_time>prev_time:
                fleet+=1
                prev_time = curr_time
        
        return fleet


