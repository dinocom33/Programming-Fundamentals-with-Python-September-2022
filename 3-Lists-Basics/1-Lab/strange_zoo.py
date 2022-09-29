head = input()
body = input()
tail = input()

meerkat = [head, body, tail]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
