def is_all_letters(s):
    return s.isalpha()

your_variable_name = \
["abcdefghijklm",
 "nopqrstuvwxyz"]

str = input("Enter a string to type: ")
position = 0
line = 0
action = ""
if str.isalpha():
    print("The robot must perform the following operations:")
    for char in str:
        # 在第0行
        if char in your_variable_name[0]:
            level = 0
            # get char position
            index = your_variable_name[0].index(char)
            # 上一个字符在第0行
            if level == line:
                if index > position:
                    # print('r'*(index-position) + 'p',end='')
                    action += 'r'*(index-position) + 'p'
                    position = index
                elif index < position:
                    # print('l'*(position-index) +'p',end='')
                    action += 'l'*(position-index) +'p'
                    position = index
                else:
                    # print('p',end='')
                    action += 'p'
            # 上一个字符在第一行
            elif level < line:
                # print("u",end='')
                if index > position:
                    # print('r'*(index-position) + 'up',end='')
                    action += 'r'*(index-position) + 'up'
                    position = index
                    line = level
                elif index < position:
                    # print('l'*(position-index) +'up',end='')
                    action += 'l'*(position-index) +'up'
                    position = index
                    line = level
                else:
                    # print('up',end='')
                    action += 'up'
                    line = level
        else:
            # 在第1行
            level =1
            index = your_variable_name[1].index(char)
            # 上一个字符在第1行
            if level == line:
                if index > position:
                    # print('r'*(index - position) + 'p',end='')
                    action += 'r'*(index - position) + 'p'
                    position = index
                elif index < position:
                    # print('l'*(position-index) + 'p',end='')
                    action += 'l'*(position-index) + 'p'
                    position = index
                    line = level
                else:
                    # print('p',end='')
                    action += 'p'
            # 上一个字符在0行
            elif level > line:
                # print("d",end='')
                if index > position:
                    # print('r'*(index - position) + 'dp',end='')
                    action += 'r'*(index - position) + 'dp'
                    position = index
                    line = level
                elif index < position:
                    # print('l'*(position-index) +'dp',end='')
                    action += 'l'*(position-index) + 'dp'
                    position = index
                    line = level
                else:
                    # print('dp',end='')
                    action += 'dp'
                    line = level
    # print()
    print(action +' ')
else:
    print("The string cannot be typed out.")


