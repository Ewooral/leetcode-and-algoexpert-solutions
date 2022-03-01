# Print a square pattern
def squarePattern(size):
    
    for i in range(size):
        # this loop will print 7 vertical rows

        for j in range(0, size ):
            # this loop will print 7 horizontal columns
            print("#", end=" ")
        print(".")


squarePattern(7)


def star_heart_shape(size):
