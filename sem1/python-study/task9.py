keyboards = [
        ["abcdefghijklm", "nopqrstuvwxyz"],
        ["789", "456", "123", "0.-"],
        ["chunk", "vibex", "gymps", "fjord", "waltz"],
        ["bemix", "vozhd", "grypt", "clunk", "waqfs"]
    ]

def find_position(keyboard,char):
    for i,row in enumerate(keyboard):
        if char in row:
            return i,row.index(char)
    return None

def generate_actions(keyboard,string):
    action = ""
    pos = (0,0)
    for char in string:
        target_pos = find_position(keyboard,char)
        if target_pos is None:
            return None
        r1,c1 = pos
        r2,c2 = target_pos
        if c2 > c1:
            if (c2 -c1) >= len(keyboard[0]) / 2:
                action += 'lw'
            else:
                action += (c2 -c1) * 'r'

        elif c2 < c1:
            if (c1 - c2) >= len(keyboard[0]) / 2:
                action += 'rw'
            else:
                action += (c1 - c2) * 'l'

        if r2 > r1:
            if (r2 -r1) >= len(keyboard) / 2:
                action += 'uw'
            else:
                action += (r2 -r1) * 'd'
        elif r2 < r1:
            if (r1 -r2) >= len(keyboard) / 2:
                action += 'dw'
            else:
                action += (r1 -r2) * 'u'

        action += 'p'
        pos = target_pos
    return action


def count_step(action):
    return len(action.replace('p',''))


def best_keyboard(string):
    best_config = None
    best_action = None
    min_step = float('inf')
    for i,keyboard in enumerate(keyboards):
        actions = generate_actions(keyboard,string)
        if actions is not None:
            count = count_step(actions)
            if count < min_step:
                min_step = count
                best_action = actions
                best_config = i
    return best_action, best_config

def print_keyboard(keyboard):
    print("---------")
    for row in keyboard:
        print("| {} |".format(row))
    print("---------")

print()


userinput = input("Enter a string to type: ")
action , config = best_keyboard(userinput)
if config is not None:
    print("Configuration used:")
    print_keyboard(keyboards[config])
    print("The robot must perform the following operations:")
    print(action)
else:
    print("The string cannot be typed out.")
