class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        shit = []
        answer = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            while shit and temperatures[i] > temperatures[shit[-1]]:
                answer[shit[-1]] = i-shit[-1]
                shit.pop()

            shit.append(i)

        return answer