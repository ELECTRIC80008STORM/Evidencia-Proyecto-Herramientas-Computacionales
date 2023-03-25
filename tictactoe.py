"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import color
from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import onscreenclick
from turtle import done


from freegames import line


def check(x, y, box):
    "To check if the box is taken"
    newX = int(x)
    newY = int(y)
    # Box 0
    if ((newX == -200) & (newY == 66)):
        if box[0] == 1:
            return True
        else:
            box[0] = 1
            return False

    # Box 1
    if ((newX == -67) & (newY == 66)):
        if (box[1] == 1):
            return True
        else:
            box[1] = 1
            return False

    # Box 2
    if ((newX == 66) & (newY == 66)):
        if (box[2] == 1):
            return True
        else:
            box[2] = 1
            return False

    # Box 3
    if ((newX == -200) & (newY == -67)):
        if (box[3] == 1):
            return True
        else:
            box[3] = 1
            return False

    # Box 4
    if ((newX == -67) & (newY == -67)):
        if (box[4] == 1):
            return True
        else:
            box[4] = 1
            return False

    # Box 5
    if ((newX == 66) & (newY == -67)):
        if (box[5] == 1):
            return True
        else:
            box[5] = 1
            return False

    # Box 6
    if ((newX == -200) & (newY == -200)):
        if (box[6] == 1):
            return True
        else:
            box[6] = 1
            return False

    # Box 7
    if ((newX == -67) & (newY == -200)):
        if (box[7] == 1):
            return True
        else:
            box[7] = 1
            return False

    # Box 8
    if ((newX == 66) & (newY == -200)):
        if (box[8] == 1):
            return True
        else:
            box[8] = 1
            return False


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player red."""
    color("red")
    line(x - 17, y - 17, x + 150, y + 150)
    line(x - 17, y + 150, x + 150, y - 17)


def drawo(x, y):
    """Draw O player blue."""
    color("blue")
    up()
    goto(x + 67, y - 3)
    down()
    circle(70)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def tap(x, y):
    # Draw X or O in tapped square.
    x = floor(x)
    y = floor(y)

    if check(x, y, boxes) is False:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
