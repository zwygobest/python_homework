import keyboard
keyboards = [
        ["abcdefghijklm", "nopqrstuvwxyz"],
        ["789", "456", "123", "0.-"],
        ["chunk", "vibex", "gymps", "fjord", "waltz"],
        ["bemix", "vozhd", "grypt", "clunk", "waqfs"]
    ]

def find_position(keyborad,char):
#     find the index of char
    for r,row in enumerate(keyborad):
        if char in row:
            return (r,row.index(char))
    return None

def generate_actions(keyboard,str):
    action = ""
    pos = (0,0)
    for element in str:
        tar_pos = find_position(keyboard,element)
        if tar_pos is  None:
            return None
        r1 , c1 = pos
        r2 , c2 = tar_pos
#         turn right
        action += 'r' * max(0, c2 - c1)
#         move left
        action += 'l' * max(0, c1 - c2)
#         move down
        action += 'd' * max(0, r2 - r1)
#         move up
        action += 'u' * max(0, r1 - r2)
        action += 'p'
        pos = tar_pos
    #     计算出 一个字符串的总路径
    return action

def count_moves(actions):
    return len(actions.replace("p",""))

def best_keyboard(string):
    """选择最优的键盘配置"""

    best_config = None
    best_actions = None
    min_move = float('inf')
    for i,kb in enumerate(keyboards):
        actions = generate_actions(kb,string)
        if actions is not None:
            moves = count_moves(actions)
            if moves < min_move:
                min_move = moves
                best_actions = actions
                best_config = i
    return best_actions,best_config


def print_keyboard(keyboard):
    print("---------")
    for row in keyboard:
        print("| {} |".format(row))
    print("---------")


# 用户输入
userinput = input("Enter a string to type: ")
action,config_index = best_keyboard(userinput)
if config_index is not None:
    print("Configuration used:")
    print_keyboard(keyboards[config_index])
    print("The robot must perform the following operations:")
    print(action)
else:
    print("The string cannot be typed out.")






