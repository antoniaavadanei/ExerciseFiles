snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

move = input("move:L/R/U/D: ")
x = True
while x:
    if move == 'R':
        old_head = snake[-1]
        new_head = [old_head[0] + 20, old_head[1]]
        snake.append(new_head)
        snake.pop(0)
        print(snake)
        direction = 'R'
    elif move == 'L':
        old_head = snake[-1]
        new_head = [old_head[0] - 20, old_head[1]]
        snake.append(new_head)
        snake.pop(0)
        print(snake)
        direction = 'L'
    elif move == 'U':
        old_head = snake[-1]
        new_head = [old_head[0], old_head[1]+20]
        snake.append(new_head)
        snake.pop(0)
        print(snake)
    elif move == 'D':
        old_head = snake[-1]
        new_head = [old_head[0], old_head[1]-20]
        snake.append(new_head)
        snake.pop(0)
        print(snake)
    else:
        print('wrong move')
        x = False
    move = input("move:L/R/U/D: ")
