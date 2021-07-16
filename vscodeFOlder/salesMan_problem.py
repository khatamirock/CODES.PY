from random import randint
import turtle
from math import isinf, sqrt, degrees, acos
def generate_subsets(n):
    l = []
    for i in range(2**n):
        l.append(i)
    return sorted(l, key = lambda x : size(x) )



def in_subset(i, s):
    while i > 0 and s > 0:
        s = s >> 1
        i -= 1
    cond = s & 1
    return cond

def length(int_type):
    length = 0
    count = 0
    while (int_type):
        count += (int_type & 1)
        length += 1
        int_type >>= 1
    return length

def remove(i, s):
    x = 1
    x = x << i
    l = length(s)
    l = 2 ** l - 1
    x = x ^ l
    return x & s

def get_path(p):
    n = len(p[0])
    number = 2 ** n - 2
    prev = p[number][0]
    path = []
    while prev != -1:
        path.append(prev)
        number = remove(prev, number)
        prev = p[number][prev]
    reversepath = [str(path[len(path)-i-1]+1) for i in range(len(path))]
    reversepath.append("1")
    reversepath.insert(0, "1")
    return reversepath

def make_graph(n):
    a = [ [-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rand = randint(0, n)
            if a[i][j] < 0:
                a[i][j] = rand
                a[j][i] = rand
            if i == j:
                a[i][i] = 0
    return a

def size(int_type):
    length = 0
    count = 0
    while (int_type):
        count += (int_type & 1)
        length += 1
        int_type >>= 1
    return count

def tsp(a):
    n = len(a)
    l = generate_subsets(n)
    cost = [[-1 for city in range(n)] for subset in l]
    p = [[-1 for city in range(n)] for subset in l]

    count = 1
    total = len(l)
    for subset in l:
        for dest in range(n):
            if not size(subset):
                cost[subset][dest] = a[0][dest]
                print(dest, subset)
            elif (not in_subset(0, subset)) and (not in_subset(dest, subset)):
                mini = float("inf")
                for i in range(n):
                    if in_subset(i, subset):
                        modifiedSubset = remove(i, subset)
                        val = a[i][dest] + cost[modifiedSubset][i]

                        if val < mini:
                            mini = val
                            p[subset][dest] = i

                if not isinf(mini):
                    cost[subset][dest] = mini
        count += 1
    path = get_path(p)

    Cost = cost[2 ** n - 2][0]
    print("Total cost for travelling with minimum route is :", Cost)
    return path

points = [(randint(-150,150), randint(-150,150)) for i in range(5)]
travel_cost_matrix = [[1, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
print(travel_cost_matrix)
path = tsp(travel_cost_matrix)


ang=0
travel_path = turtle.Turtle()
travel_path.hideturtle()
travel_path.screen.bgcolor("yellow")
travel_path.color("blue")

def distance(x, y):
    return sqrt((x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1]))

def angle(x, y):
    try:
        result = degrees(acos((y[0] - x[0]) / distance(x, y)))
    except:
        result = 0
    if x[1] > y[1]:
        result = 360 - result
    return result;

for i in range(len(points)):
    travel_path.left(-ang)
    d = distance(points[i-1], points[i])
    ang = angle(points[i-1], points[i])
    travel_path.left(ang)
    travel_path.forward(d)
    travel_path.circle(2)
travel_path.screen.exitonclick()

