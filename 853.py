class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = []
        pos = [target-position[n] for n in range(len(position))]
        print(sol)
        for i in range(len(pos)):
            time = pos[i]/speed[i]
            cars.append((pos[i],time))
        cars.sort(key=lambda x: x[0])
        print('cars:',cars)
        for car in cars:
            print("car:",car,"cars:",cars)
            if fleets and car[1]<=fleets[-1]:
                continue
            else:
                fleets.append(car[1])
        print(fleets)
        return len(fleets)

sol = Solution()
print(sol.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))