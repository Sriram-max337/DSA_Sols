class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        HM = {}

        for node in edges:
            if node[0] not in HM:
                HM[node[0]] = 1
            else:
                HM[node[0]] += 1

            if node[1] not in HM:
                HM[node[1]] = 1
            else:
                HM[node[1]] += 1

        return max(HM, key=HM.get)