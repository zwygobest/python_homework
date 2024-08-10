def is_all_letters(s):
    return s.isalpha()

your_variable_name = \
["abcdefghijklm",
 "nopqrstuvwxyz"]

str = input("Enter a string to type: The robot must perform the following operations:")
position = 0
line = 0
if str.isalpha():
    for char in str:
        # 在第0行
        if char in your_variable_name[0]:
            level = 0
            # get char position
            index = your_variable_name[0].index(char)
            # 上一个字符在第0行
            if level == line:
                if index > position:
                    print('r'*(index-position) + 'p',end='')
                    position = index
                elif index < position:
                    print('l'*(position-index) +'p',end='')
                    position = index
                else:
                    print('p',end='')

            # 上一个字符在第一行
            elif level < line:
                # print("u",end='')
                if index > position:
                    print('r'*(index-position) + 'up',end='')
                    position = index
                    line = level
                elif index < position:
                    print('l'*(position-index) +'up',end='')
                    position = index
                    line = level
                else:
                    print('up',end='')
                    line = level
        else:
            # 在第1行
            level =1
            index = your_variable_name[1].index(char)
            # 上一个字符在第1行
            if level == line:
                if index > position:
                    print('r'*(index - position) + 'p',end='')
                    position = index
                elif index < position:
                    print('l'*(position-index) + 'p',end='')
                    position = index
                    line = level
                else:
                    print('p',end='')
            # 上一个字符在0行
            elif level > line:
                print("d",end='')
                if index > position:
                    print('r'*(index - position) + 'p',end='')
                    position = index
                    line = level
                elif index < position:
                    print('l'*(position-index) +'p',end='')
                    position = index
                    line = level
                else:
                    print('p',end='')
                    line = level
else:
    print("The string cannot be typed out.")