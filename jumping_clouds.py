def jumpingOnClouds(c):
    current_position = 0
    steps = 0
    done = False
    while (current_position < (len(c)-1)) and not done:
        print('======',current_position, (len(c)-1), steps)
        if c[current_position+2] == 0:
            current_position += 2
            steps += 1
        elif c[current_position+1] == 0:
            current_position += 1
            steps += 1
        else:
            done = True
    return steps
        

p = [0,1,0,0,0,1,0]
print(jumpingOnClouds(p))