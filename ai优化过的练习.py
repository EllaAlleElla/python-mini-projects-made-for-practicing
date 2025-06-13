# 打印欢迎信息
print("Hello world")  # 输出一段文本，作为程序的开始

# 定义一个整数变量
example_number = 1
print(f"The value of example_number is: {example_number}")  # 使用格式化输出变量内容

# 让用户输入一些东西（input 返回的是字符串类型）
input_example = input("Please write something here: ")
input_number = input("Write a number here: ")

# 输出的时候，记得要把数字转成字符串，或者用格式化方式
print(f"Here's the first sentence, and this is the number you saw earlier: {example_number}")

# 定义第一个函数：不带参数，只重复一句话
def example1():
    print("这个函数只能用来重复说你好：你好！\n")

# 定义第二个函数：带一个参数
def example2(my_favorites):
    print(f"这个函数有一个变量，可以告诉你我喜欢什么。我喜欢 {my_favorites}！\n")

# 定义第三个函数：带两个参数
def example3(thoughts1, thoughts2):
    print(f"这个函数就厉害了，有两个变量。")
    print(f"我来告诉你第一件：{thoughts1}，然后是第二件：{thoughts2}。\n")

# 调用上面这些函数
example1()

# 使用中文变量会有兼容问题，建议实际开发中尽量使用英文
example2("叶子酱")

example3("我的第二个想法是正确的", "我的第一个想法是错误的")
