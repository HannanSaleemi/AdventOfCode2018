id_list = [str(ids).rstrip() for ids in open("input.txt").readlines()]
print(id_list[0])

twice_appear_counter = 0
three_appear_counter = 0

for item in id_list:
    char_map = {}
    for char in item:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] = char_map[char] + 1
    
    twice = False
    three = False

    for value in char_map.values():
        if int(value) == 2 and twice == False:
            twice_appear_counter += 1
            twice = True
        elif int(value) == 3 and three == False:
            three_appear_counter += 1
            three = True
    
    print(char_map)

print(twice_appear_counter)
print(three_appear_counter)