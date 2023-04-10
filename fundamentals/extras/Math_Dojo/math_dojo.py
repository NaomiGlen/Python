class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for num in nums:
            self.result += num
        return self
    def subtract(self, num, *nums):
        for num in nums:
            self.result -= num
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(2,3).result
print(x)
