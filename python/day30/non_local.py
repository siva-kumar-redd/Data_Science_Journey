def outer():
    x=100
    def inner():
        nonlocal x
        x += 50
    inner()
    print(x)
outer()