class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position , speed) , reverse = True)
        times=[]
        for p,s in cars:
            times.append((target-p)/s)

        fleets =0
        slow=0

        for time in times:
            if time>slow:
                fleets+=1
                slow=time

        return fleets
        