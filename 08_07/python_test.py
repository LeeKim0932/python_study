


# number1 exception

'''
short_list = [ 1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])

    except IndexError as err:
        print('Bad index:', position)

    except Exception as other:
        print('Something else broke:', other)
'''

# number2 deque
'''
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print(palindrome('apple'))
'''


# number3 reverse_palindrome
'''
word = input()
def another_palindrome(word):
    return word == word[::-1]
print(another_palindrome(word))
'''


# number4 reverse_word

word = input()
def another_palindrome(word):
    return  word[::-1]
print(another_palindrome(word))
