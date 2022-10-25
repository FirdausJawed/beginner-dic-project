# def rev(L,n):
#     L=(reversed(sorted(L)))
#     for i in L:
#         if i<n:
#          print(i)

# x=[2,5,6,1,0,9]

# rev(x,4)

# L =[1,2,3,4,5,66,88,9,8,77,9,5,55,7]

# l=[]

# for i in L:
#     if i%2!=0:
#         l.append(i)

# print(len(l))


# import turtle
# tur=turtle.Turtle()

# for i in range(5):
#     tur.forward(50)
#     tur.right(75)
# turtle.done()

import turtle
turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7

dot_distance = 25

seurat.setpos(-250, 250)


def spiral(n, m):
    l = 0
    k = 0
    f = 0
    seurat.color("white")

    while (k < m and l < n):

        if (f == 1):
            seurat.right(90)

        for i in range(l, n):
            seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        k += 1
        f = 1

        seurat.right(90)

        for i in range(k, m):
            seurat.forward(dot_distance)

            # print(a[i][n-1],end=" ")
        n -= 1
        seurat.right(90)

        if k < m:
            for i in range(n-1, l-1, -1):
                seurat.forward(dot_distance)
                # print(a[m-1][i], end=" ")
            m -= 1
            seurat.right(90)
            if l < n:
                for i in range(m-1, k-1, -1):
                    seurat.forward(dot_distance)
                    # print(a[i][l], end=" ")
                l += 1
spiral(20,20)