


def find_doubles(items):
    x = 0
    final = {}
    while x < len(items):
        if items[x] not in final:
            final[items[x]] = 1
        else:
            final[items[x]] += 1
        x += 1 
    for key in final:
        if final[key] == 2:
            print key 
    

    

test_one = ["a", "b", "c", "a", "d", "f", "l", "f", "g", "a", "g"]
    
test_two = [1, 5, 5, 7, -1, 12, 7, 7]


print("Testing: " + str(test_one))
find_doubles(test_one)
print("Testing: " + str(test_two))
find_doubles(test_two) 