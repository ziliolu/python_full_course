# nested functions calls = function calls inside other fucntion calls 
# innermost function calls are resolved first 
# returned value is used as argument for the next outer function 

num = input("Enter a whole positive number: ")
num = float(num)


def hello(name):
    print("hello "+name)

hello("Mary")
