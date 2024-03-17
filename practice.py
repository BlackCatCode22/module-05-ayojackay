# colors = dict()
# colors['red'] = '#FF0000'
# colors['blue'] = '#0000FF'
# colors['lime'] = '#00FF00'
# print(colors)

# fname = input('Enter file: ')
# handle = open(fname)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)

d = {'a': 10, 'c': 22, 'b': 1}
# t = sorted(d.items())
# print(t)
# tmp = list()
# for k, v in d.items():
#     tmp.append((v, k))
#
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

fhand = open('lorem.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
#
# lst = sorted(lst, reverse=True)
#
# for val, key in lst[:10]:
#     print(key, val)


print(sorted([(b, a) for a, b in counts.items()], reverse=True))