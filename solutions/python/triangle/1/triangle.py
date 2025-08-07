def triangle_check(sides):
    for length in sides:
        if length <= 0:
            return False
    a, b, c = sides[0], sides[1], sides[2]
    return a + b >= c and a + c >= b and b + c >= a

def equilateral(sides):
    return len(set(sides)) == 1 and triangle_check(sides)


def isosceles(sides):
    return  len(set(sides)) <= 2 and triangle_check(sides)


def scalene(sides):
    return len(set(sides)) == 3 and triangle_check(sides)
