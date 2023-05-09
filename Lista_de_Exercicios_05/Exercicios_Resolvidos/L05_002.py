s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "
i = 14
p1 = s[i+13] + s[i+4] + s[i-2] + s[10] + s[-12] + s[i-1] + s[-15] + s[-1]
p2 = s[i+6] + s[i+7] + s[14] + s[i-3] + s[i] + s[i+13]
print(p1 + p2)
