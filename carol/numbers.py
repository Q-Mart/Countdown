import itertools
import astar
import collections
import operator

State = collections.namedtuple('State', ['currentVal', 'numbersLeft', 'lastOperation'])

def solveNumbersRound(goal, numbers):

    goalFunc = lambda x: x.currentVal == goal
    hFunc = lambda x: goal - x.currentVal
    gFunc = hFunc

    def children(s):
        operators = [('+', operator.add),
                     ('-', operator.sub),
                     ('*', operator.mul),
                     ('/', operator.truediv)]
        kids = []
        for n in s.numbersLeft:
            for ch, op in operators:
                i = s.numbersLeft.index(n)
                newNumbersLeft = s.numbersLeft[i+1:] + s.numbersLeft[:i]
                newCurrentVal = op(s.currentVal, n)

                kids.append(State(newCurrentVal, newNumbersLeft, ch))

        return kids

    searcher = astar.Astar(State(0, numbers, None), goalFunc, children, hFunc, gFunc)
    return searcher.executeSearch()

def allResultsFrom(a,b):
    yield '+', a + b
    yield 'x', a * b

    c = b-a
    if c > 0:
        yield '-', c
    if b % a == 0:
        yield '/', b / a

def pairsAndRejects(numbers):
    for pair in itertools.combinations(numbers, 2):
        # We don't want to modify the original list
        rejects = list(numbers[:])
        del rejects[rejects.index(pair[0])]
        del rejects[rejects.index(pair[1])]

        yield pair, tuple(rejects)

def findAllPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def solve(numbers, target):
    numbers = tuple(sorted(numbers))
    graph = {}

    def r(numbers):
        if len(numbers) == 2:
            a, b = numbers[0], numbers[1]
            if b / a > target or a * b < target:
                return
        for pair, rejects in pairsAndRejects(numbers):
            a, b = pair[0], pair[1]
            for op, c in allResultsFrom(a, b):
                node = tuple(sorted(list(rejects) + [c]))

                if node in graph:
                    graph[node][numbers].add(((a,b), op, c))
                    if c == target: return
                else:
                    graph[node] = collections.defaultdict(set)
                    graph[node][numbers].add(((a,b), op, c))
                    if c == target: return
                    r(node)

    for i in range(len(numbers)):
        for comb in itertools.combinations(numbers, i+1):
            r(comb)

    return graph

def prettyPrint(path, graph):
    for node in path:
        if node in graph:
            print(node, graph[node])


# r = solveNumbersRound(386.0, (25, 75, 50, 1, 9, 3))
# print(r)

# numbers = (25, 75, 50, 1, 9, 31)
numbers = (25, 75)
operators = ('+', '-', '*', '-')

#     for c in itertools.combinations(numbers, i):
#         for p in itertools.permutations(c):
#             print(p)

nums = [5, 100, 25]
g = solve(nums, 125)

paths = findAllPaths(g, (125,), tuple(sorted(nums)))
print (paths)

for k1,v1 in g.items():
    print (k1, '\n')

    for k2,v2 in v1.items():
        print ('\t', k2, v2)

for path in paths:
    prettyPrint(path, g)
    print('-------------------------------------------------------\n')

