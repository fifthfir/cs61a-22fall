from operator import mul
def square(square):
    return mul(square,square)
print(square(square(-2)))
# 这里的两个square相当于一个local一个global？
# 所以里面local square的取值不影响外面的global square
# 反正就是不同的嵌套,每个产生调用的上下文对于那个被调用的上下文都是所谓的全局
# 不同frame/作用域/帧不相互影响

# A name evaluates to the value bound to that name in earliest frame 
# of the current environment in which that name is found