class TimeMap:

    def __init__(self):
        self.keyStore = {} # key : [list of values,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

        #self.keyStore.get(key, []).append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])

        l = 0
        print(self.keyStore, key, values, timestamp)
        r = len(values)-1

        while l<=r:
            mid = l + (r-l)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid -1
        
        return res
        
