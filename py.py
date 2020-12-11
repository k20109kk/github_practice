class math:
    def __init__(self, operator):
        self.operator = operator

    def mul(self, x, y):
        if self.operator == "*":
            print(x * y)


answer = math("*")

answer.mul(5, 2)
