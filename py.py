class math:
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2

    def mul(self):
        print(self.num1 * self.num2)
    def add(self):
        print(self.num1 + self.num2)
    def sub(self):
        print(self.num1 - self.num2)
answer = math(5,2)
answer.mul()
answer.add()
answer.sub()
