class MedianFinder:
    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)

    def findMedian(self) -> float:
        n = len(self.lst)
        self.lst.sort()
        if n % 2 == 1:
            median = self.lst[n // 2]
        else:
            median = (self.lst[(n // 2) - 1] + self.lst[n // 2]) / 2
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()