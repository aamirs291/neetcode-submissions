class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        total_fuel = 0

        for i in range(n):
            total_fuel += gas[i]-cost[i]

        if total_fuel<0:
            return -1
        
        curr_fuel = 0
        start_idx = 0
        for i in range(n):
            curr_fuel += gas[i]-cost[i]

            if curr_fuel<0:
                curr_fuel=0
                start_idx = i+1
        
        return start_idx
            

        