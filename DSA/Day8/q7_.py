def fun(n):

    if n == 0:
        return

    print("A", n)

    fun(n-1)

    print("B", n)

fun(3)