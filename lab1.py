def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a
    return a

def readArray(n):
    a = []
    while n:
        a.append(int(input()))
        n -= 1
    return a

def printFactors(arr, variant):
    for val in arr:
        g = gcd(val, arr[variant])
        if g > 1 and g != arr[variant]:
            print (arr[variant], ":\n1 -> ", g, "\n2 -> ", arr[variant] // g)
            break

n, variant = map(int, input().split())
variant %= n
arr = readArray(n * 2)
printFactors(arr, variant)
printFactors(arr, variant + n)
print()