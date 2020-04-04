## Q47
##

def divisions(n):
    a = 2
    c = set()
    while n != 1:
        if n % a == 0:
            n = n // a
            c.add(a)
        else:
            a += 1

    return (c)


d = [0] * 4
i = 122500
while True:
    if len(divisions(i)) == 4:
        d.pop(0)
        d.append(len(divisions(i)))
    else:
        d.pop(0)
        d.append(0)

    if all(d):
        break
    else:
        i += 1

e = []
for i in range(2, int(1e6)):
    e.append(len(divisions(i)))