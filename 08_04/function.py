
# 2019_08_04 python practice
# python book p137

# number 1
def add_args(arg1, arg2):
    print(arg1 + arg2)

def sum_args(*args):
    return sum(args)

#def run_something_with_args(func, arg1, arg2):
#    func(arg1, arg2)
def run_something_with_args(func, *args):
    return func(*args)

    
print(type(add_args)) 
#run_something_with_args(add_args, 1,2,3,4)
run_something_with_args(sum_args, 1,2,3,4)

