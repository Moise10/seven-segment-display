
patterns = [[[' ','#',' '],
             [' ','#',' '],
             [' ','#',' '],
             [' ','#',' '],
             [' ','#',' ']],
             
             [['#','#','# '],
              [' ',' ','# '],
              ['#','#','# '],
              ['#',' ','  '],
              ['#','#','# ']],
             
             [['#','#','# '],
              [' ',' ','# '],
              [' ','#','# '],
              [' ',' ','# '],
              ['#','#','# ']],
             
             [['#',' ','# '],
              ['#',' ','# '],
              ['#','#','# '],
              [' ',' ','# '],
              [' ',' ','# ']],
             
             [['#','#','# '],
              ['#',' ','  '],
              ['#','#','# '],
              [' ',' ','# '],
              ['#','#','# ']],
             
             [['#','#','# '],
              ['#',' ','  '],
              ['#','#','# '],
              ['#',' ','# '],
              ['#','#','# ']],
             
             [['#','#','# '],
              [' ',' ','# '],
              [' ',' ','# '],
              [' ',' ','# '],
              [' ',' ','# ']],
             
             [['#','#','# '],
              ['#',' ','# '],
              ['#','#','# '],
              ['#',' ','# '],
              ['#','#','# ']],
             
             [['#','#','# '],
              ['#',' ','# '],
              ['#','#','# '],
              [' ',' ','# '],
              [' ',' ','# ']]]
             


def displaynum():
    num = -1
    
    while num < 0:
        try:
            num = int(input("Enter a any positive number:  "))
        except:
            print("Invalid number")
    for x in range(5):
        for digit in str(num):
            for y in range(3):
                if digit == '1':
                    print(patterns[0][x][y], end =" ")
                elif digit == '2':
                    print(patterns[1][x][y], end =" ")
                elif digit == '3':
                    print(patterns[2][x][y], end = " ")
                elif digit == '4':
                    print(patterns[3][x][y], end = " ")
                elif digit == '5':
                    print(patterns[4][x][y], end = " ")
                elif digit == '6':
                    print(patterns[5][x][y], end = " ")
                elif digit == '7':
                    print(patterns[6][x][y], end = " ")
                elif digit == '8':
                    print(patterns[7][x][y], end = " ")
                elif digit == '9':
                    print(patterns[8][x][y], end = " ")
                else:
                    print(patterns[0][x][y], end = " ")
            
        
        print()


displaynum()    
            