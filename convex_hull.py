n = int(input())

def vec(a:'point',b:'point'):
    return (b[0]-a[0], b[1]-a[1])

def ccw(a:'vector', b:'vector'): # check counterclockwise using a crossproduct b
    return a[0]*b[1] - a[1]*b[0]

def buildhull(points, factor): #factor is used to find upper hull and lower hull
    hull = []
    for p in points:
        while len(hull) >= 2:
            a = vec(hull[-2], hull[-1])
            b = vec(hull[-1], p)

            if ccw(a,b) * factor > 0:
                break
            else:
                hull.pop()

        while len(hull) > 0 and p == hull[-1]:
            hull.pop()

        hull.append(p)
    return hull

while n:
    points = []
    for i in range(n):
        x, y = input().split()
        points.append((int(x),int(y)))

    points.sort()

    lower_hull = buildhull(points, 1)
    upper_hull = buildhull(points, -1)

    print(len(lower_hull) + max(0, len(upper_hull)-2))

    for p in lower_hull:
        print(p[0],p[1])
    for i in range(len(upper_hull)-2, 0, -1):
        print(upper_hull[i][0], upper_hull[i][1])
        
    
    n = int(input())
