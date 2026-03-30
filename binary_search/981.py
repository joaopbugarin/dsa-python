from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #use binary search to find adequate timestamp
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = l + (r-l) // 2
            curr_timestamp = self.store[key][m][0]
            if curr_timestamp == timestamp:
                return self.store[key][m][1]
            if curr_timestamp < timestamp:
                l = m + 1
            elif curr_timestamp > timestamp:
                r = m - 1
        if r <= 0:
            return ""
        return self.store[key][r][1]



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set(1,2,3)
print(obj.store)
print(obj.get(1,1))