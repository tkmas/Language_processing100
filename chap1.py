# a = "パタトクカシーー"
# print("".join([i for i in a[1::2]]))
#
# b = "パトカー"
# c = "タクシー"
# ans = "".join([i + j for i, j in zip(b, c)])
# print(ans)
#
# a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# b = a.replace(".", "").replace(",", "").split()
# c = [len(i) for i in b]
# print(c)
#
# a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# b = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# c = a.split()
# d = [j[0] if i + 1 in b else j[:2] for i, j in enumerate(c)]
# e = {key: value + 1 for value, key in enumerate(d)}
# print(d)
# print(e)
#
# a = "I am an NLPer"


def word_n_gram(seq, n):
    b = seq.split()
    if len(b) >= n:
        c = []
        for i in range(len(b) - n + 1):
            c.append(b[i: i+n])
        return c
    else:
        return None


# print(word_n_gram(a, 2))


def letter_n_gram(seq, n):
    b = seq.replace(" ", "")
    if len(b) >= n:
        c = []
        for i in range(len(b) - n + 1):
            c.append(b[i: i+n])
        return c
    else:
        return None


# print(letter_n_gram(a, 2))

# a = "paraparaparadise"
# b = "paragraph"
# a_bi = set(letter_n_gram(a, 2))
# b_bi = set(letter_n_gram(b, 2))
# print(a_bi, b_bi)
# print("和集合", a_bi | b_bi)
# print("積集合", a_bi & b_bi)
# print("差集合", a_bi - b_bi)


def time_and_info(x, y, z):
    return f"{x}時の{y}は{z}"


print(time_and_info(12, "気温", 22.4))


def cipher(line):
    a = list(line)
    b = []
    for i in a:
        if i.islower():
            b.append(chr(219 - ord(i)))
        else:
            b.append(i)
    return "".join(b)


print(cipher("Unityすき"))

