from icecream import ic


def solve(inp):
    dial = 50
    res = 0
    for ins in inp.strip().split():
        dirn, cnt = ins[:1], int(ins[1:])
        if dirn == 'L':
            dial = (dial - cnt) % 100
        else:
            dial = (dial + cnt) % 100
        if dial == 0:
            res += 1
    return res


def solve2(inp):
    dial = 50
    res = 0
    for ins in inp.strip().split():
        dirn, cnt = ins[:1], int(ins[1:])
        if dirn == 'L':
            res += abs((dial - cnt) // 100)
            dial = (dial - cnt) % 100

        else:
            res += (dial + cnt) // 100
            dial = (dial + cnt) % 100
            
        ic(ins, dial, res)
    return res


inp1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

ic.enable()
assert solve(inp1) == 3
assert solve2(inp1) == 6

ic.disable()

with open("d1.txt") as f:
    txt = f.read()
    print(solve(txt))
    print(solve2(txt))
