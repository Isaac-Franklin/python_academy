def multiplyMethod():
    global mul

    def mul(a, b):
        return a * b


multiplyMethod()


answer = mul(2, 3)
print(answer)
