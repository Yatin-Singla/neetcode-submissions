class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars based on starting positions, no need for tie breaker since pos is unique
        # key = lambda x,y: y (where x = idx, and y = pos)
        orderSet = list(sorted([(i, v) for (i,v) in enumerate(position)],\
         key= lambda x: x[1], reverse= True))
        t_stack = [] # time for fleet to reach target starting from car with min dist to cover
        n = len(position)
        for idx, pos in orderSet:
            if not t_stack:
                t_stack.append((target-pos)/speed[idx])
            else:
                t_curr_fleet = (target-pos)/speed[idx]
                t_fleet_ahead = t_stack[-1]
                if t_curr_fleet > t_fleet_ahead:
                    t_stack.append(t_curr_fleet)

        return len(t_stack)