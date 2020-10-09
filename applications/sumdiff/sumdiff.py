"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


results = {}
totals = {}
sums = {}
differences = {}
qs = list(q)
for num in q:
    results[num] = f(num)
for i in qs:
    for j in qs:
        s = results[i] + results[j]
        d = results[i] - results[j]
        if s in sums:
            sums[s].append((i, j))
        else:
            sums[s] = [(i, j)]
        if d in differences:
            differences[d].append((i, j))
        else:
            differences[d] = [(i, j)]
    s = results[i] * 2
    if 0 in differences:
        differences[0].append((i, i))
    else:
        differences[0] = [(i, i)]
result = []
for s in sums:
    if s in differences:
        result.append((sums[s], differences[s]))
for t in result:
    for combo in t[0]:
        num_one = combo[0]
        num_two = combo[1]
        num_three = t[1][0][0]
        num_four = t[1][0][1]
        print(f"f({num_one}) + f({num_two}) = {results[num_one] + results[num_two]} = f({num_three}) - f({num_four})")
