from sys import stdin

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

d_to_n = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5', 
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}


def func(maps, in_, comb):
    for l in letters - set(comb):
        maps[l] -= set(in_)
    for l in comb:
        maps[l] = maps[l].intersection(set(in_))


c = 0

for line in stdin:
    maps = {l: letters.copy() for l in letters}
    in_, out = line.split(' | ')
    outs = out.split()
    ins = in_.split()
    togo5 = {"bf", "ce", "be"}
    togo6 = {"c", "e", "d"}
    for i in sorted(ins, key=lambda x:  (2, 3, 4, 7, 6, 5).index(len(x))):
        if len(i) == 2:
            func(maps, i, "cf")
            continue
        if len(i) == 3:
            func(maps, i, "acf")
            continue
        if len(i) == 4:
            func(maps, i, "bcdf")
            continue
        if len(i) == 7: # useless
            func(maps, i, "abcdefg")
            continue
        if len(i) == 6:
            last = (letters - set(i))
            for l in "abfg":
                maps[l] -= last
                if len(maps[l]) == 1:
                    for j in letters - {l}:
                        maps[j] -= maps[l]
            continue
    revmap = {max(v): k for k, v in maps.items()}
    c += int(''.join(d_to_n[''.join(sorted(revmap[i] for i in o))] for o in outs))

print(c)