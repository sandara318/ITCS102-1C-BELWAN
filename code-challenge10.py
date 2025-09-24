#creat a decreasing asterisk

for s in range(11, 0, -1):
    for x in range(1, s):
        print("*", end=" ")
    print()