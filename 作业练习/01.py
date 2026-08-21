def outer(num):
    def inner():
        return num + 10

    return inner


func = outer(5)
print(func())