# 2019_08_04 python practice
# python book p138
# inner_function pratice

#number 1
##############################3
#def outer(a, b):
#    def inner(c, d):
#        return c + d
#    return inner(a, b)
#
#outer(4, 7)
##############################


#number 2
###############################3
def kingihts(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

################################
