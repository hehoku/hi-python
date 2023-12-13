# from module3 import foo
import module3

print("hello")

# import module3 直接写成这样，被其他模块导入时，会执行module3中的代码,但无法调用module3中的函数

# main 不能为其他值
if __name__ == "__main__":
    print("call foo()")
    foo()
