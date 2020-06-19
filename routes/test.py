# cook your dish here
import operator


def op0(a, b):

    if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
        return True
    return False


def op1(x, y):
    tuple1 = [[x[0], x[1], x[2]], [x[0], x[2], x[1]], [x[1], x[0], x[2]], [
        x[1], x[2], x[0]], [x[2], x[0], x[1]], [x[2], x[1], x[0]]]
    tuple2 = [[y[0], y[1], y[2]], [y[0], y[2], y[1]], [y[1], y[0], y[2]], [
        y[1], y[2], y[0]], [y[2], y[0], y[1]], [y[2], y[1], y[0]]]
    for i in range(6):
        p = tuple1[i][0]
        q = tuple1[i][1]
        r = tuple1[i][2]
        a = tuple2[i][0]
        b = tuple2[i][1]
        c = tuple2[i][2]

        if p == a and q == b:
            return True
        if a == p and q-b == r-c:
            return True
        if q-b == r-c and r-c == p-a:
            return True
        if r == c and p != 0 and q != 0 and a % p == 0 and b % q == 0 and (a//p) == (b//q):
            return True
        if p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and (a//p) == (b//q) and (b//q) == (c//r):
            return True
    return False


def op2(x, y):
    tuple1 = [[x[0], x[1], x[2]], [x[0], x[2], x[1]], [x[1], x[0], x[2]], [
        x[1], x[2], x[0]], [x[2], x[0], x[1]], [x[2], x[1], x[0]]]
    tuple2 = [[y[0], y[1], y[2]], [y[0], y[2], y[1]], [y[1], y[0], y[2]], [
        y[1], y[2], y[0]], [y[2], y[0], y[1]], [y[2], y[1], y[0]]]
    for i in range(6):
        p = tuple1[i][0]
        q = tuple1[i][1]
        r = tuple1[i][2]
        a = tuple2[i][0]
        b = tuple2[i][1]
        c = tuple2[i][2]

        if a-p == b-q and (a-p) != (c-r):
            return True
        if (a-p+b-q) == (c-r):
            return True
        if a == p:
            return True
        if (p != 0 and q != 0 and a % p == 0 and b % q == 0 and a//p == b//q):
            return True
        if(p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and (a//p*b//q == c//r)):
            return True
        if((p+c-r) != 0 and (q+c-r) != 0 and a % (p+c-r) == 0 and b % (q+c-r) == 0 and (a//(p+c-r)) == (b//(q+c-r))):
            return True
        if(r != 0 and c % r == 0 and c != 0 and b % (c//r) == 0 and a % (c//r) == 0 and (b*(r//c)-a*r//c) == (q-p)):
            return True
        if q != 0 and b % q == 0 and (p+c-r)*(b//q) == a:
            return True
        if a != b and p != q and (p*b-q*a) % (a-b) == 0 and (r+(p*b-q*a)//(a-b)) == c:
            return True

        if p != 0 and q != 0 and r != 0 and (a+r-c) % p == 0 and (b+r-c) % q == 0 and (a+r-c)//p == (b+r-c)//q:
            return True

        if r != 0 and (p*(c//r)-q*(c//r)) == (a-b):
            return True
        if q != 0 and b % q == 0 and (p*(b//q)+c-r) == a:
            return True
        if p != q and (a-b) % (p-q) == 0 and (p*b-a*q) % (p-q) == 0 and (r*((a-b)//(p-q))+(p*b-a*q)//(p-q)) == c:
            return True
        return False


t = int(input())
while t:
    t = t-1
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if op0(a, b):
        print(0)
    elif op1(a, b):
        print(1)
    elif op2(a, b):
        print(2)
    else:
        print(3)
