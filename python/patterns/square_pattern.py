# Print a square pattern
def squarePattern(size):
    
    for i in range(size):
        # this loop will print 7 vertical rows

        for j in range(0, size ):
            # this loop will print 7 horizontal columns
            print("#", end=" ")
        print("")


squarePattern(7)


def star():
    for row in range(6):
        for col in range(7):
            if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                print("*", end="")
            else:
                print("",end=" ")
        print()

star()