import sys


n = int(sys.argv[1])
b = int(sys.argv[2])
s = ''
while n % b < b:
    tmp = n // b
    if b > 10:
        s += '0x'
    s += str(tmp)
    if 10 <= n % b < 16:
        if n % b == 10:
            s += 'a'
        if n % b == 11:
            s += 'b'
        if n % b == 12:
            s += 'c'
        if n % b == 13:
            s += 'd'
        if n % b == 14:
            s += 'e'
        if n % b == 15:
            s += 'f'
    else:
        s += str(n % b)
        break
else:
    tmp = n // b
    s += '0x'+str(tmp)
print s





# while v <= n//2:
#     v *= 2
#
# # Cast out powers of 2 in decreasing order.
# while v > 0:
#     if n < v:
#         s += str(0)
#     else:
#         s += str(1)
#         n -= v
#     v //= 2

# print s


