for r in range(1,6):
    for c in range(1,6):
        if r == 1 or r == 5 or c == 1 or c == 5:
            print("*", end = "")
        
        else:
            print(" ", end = "")
        
    print()

