print("Hello world") #practice print

nameexample="a1a"
numberexample=1
print(nameexample) #practice value and print

inputexample=input(nameexample)
inputexample2=input("write a number here")

print("here's the first sentence,"+nameexample)
print(f"here's the second sentence, and this will be a number: {numberexample}.")
print("here's the third sentence. There would be a number: "+str(numberexample))

def example1():
    print("这个def只能用来重复说你好。你好！\n")

def example2(myfavorites):
    print("这个def有一个变量，可以告诉你我喜欢什么。我喜欢"+myfavorites+"！\n")

def example3(thoughts1,thoughts2):
    print("这个def就厉害了，有两个变量，可以告诉你两件我正在想的事。我来告诉你第一件："+thoughts1+"，然后是第二件："+thoughts2+"。\n")

example1()

example2("叶子酱")

example3("我的第二个想法是正确的","我的第一个想法是错误的")