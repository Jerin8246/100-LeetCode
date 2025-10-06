# # Here's the plan:

# # First, it is possible to complete the circuit if and only if the total amount of gas on the circuit is sufficient to drive the circuit. More formally: sum(gas) >= sum(cost).

# # The starting station can be determined by starting at some stationa(say, a = 0) and noting whether a station b on the circuit is unreachable due to lack of gas. If all are reachable, then a is our answer. If not, our answer is not a, nor is any station between a andb.

# # We reset the tank to zero and repeat on the remainder of the string s.

# # The last station that is unreachable in this process, say stationz, is our answer.

# # Why does this work? Recall there's enough gas to complete the circuit. If it were possible to "borrow" gas to get to the next station, the station requiring the most borrowed gas overall is stationz. Thus, starting at stationz is the answer.


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         if sum(gas) < sum(cost):
#             return -1
                
#         curernt_gas = 0
#         start = 0
#         for i in range(len(gas)):
#             curernt_gas += gas[i] - cost[i]
#             if curernt_gas < 0:
#                 curernt_gas = 0
#                 start = i + 1

#         return start

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        currentGas = 0
        start = 0
        for i in range(len(gas)):
            currentGas = currentGas + gas[i] - cost[i]
            if currentGas < 0:
                currentGas = 0
                start = i + 1
        
        return start
