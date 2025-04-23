# Author: Mubashir
# Date: 13-04-25

# 30. Convert Snake case to Pascal case ?

def Snake_to_Pascal(snake_str) :
    words = snake_str.split('_')
    Pascal_Case = ''.join(word.capitalize() for word in words)
    return Pascal_Case

# An Example 
str = "code_with_maviya"
Pascal_case = Snake_to_Pascal(str)
print(Pascal_case)
