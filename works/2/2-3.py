x = 12
z = 3

def f(y):
    x = 3
    print(x,y,z) 
    # anything not defined can still be accessed(but not changeable)
z += 6
f(7)
print(x)

# 3 - in the function1 (local)
# 12 - global frame
# 相当于f可以调用global的数据(go up one frame)；可以把f里的x换成a，即可理解两个x并不一样
# 所以z += 6只能在global里面进行，因为f中没有定义z；虽然能print出来，但
# print时调用的z已经是global的了，而在其走出f进入global调用z之前，对z的任何
# 操作都是无效且不关联的。所以应在global中改变z从而改变f中z的结果。