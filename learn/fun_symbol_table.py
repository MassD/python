x = 1

def fun1(y):
    x = y
    print x
    y = 9

def fun2(z):
    zz = z
    fun1(zz)
    print zz

fun2(10)

print x

def fun3(l):
    l.append(4)

l = [1,2,3]
fun3(l)
print l
