def tizbek(start, diff):
    kezen = start
    while True:
        yield kezen
        kezen += diff

seq = tizbek(3, 3)
for i in range(5):
    print(next(seq))
