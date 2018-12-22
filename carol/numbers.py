import itertools
import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.children = collections.defaultdict(list)


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

        yield pair, rejects

def generateTree(numbers, target, t=None):
    if t==None: t=Node(tuple(sorted(numbers)))
    # base case
    if len(numbers) == 1: return t
    if target in numbers: return t

    for pair, rejects in pairsAndRejects(numbers):
        a, b = pair[0], pair[1]
        for op, c in allResultsFrom(a,b):
            newNumbers = sorted(tuple(rejects + [c]))
            newNode = Node(newNumbers)
            t.children[newNode].append(str(a) + op + str(b))

        for child in t.children.keys():
            generateTree(newNumbers, target, child)

    return t

def findPath(target, root):
    visited = set()
    stack = [(root, [])]

    while stack:
        (node, path) = stack.pop()
        if node.value == [15, 50]:
            for c, op in node.children.items():
                print(node.value, c.value, op)

        if node not in visited:
            if target in node.value:
                return path
            visited.add(node)

            for child, operations in node.children.items():
                stack.append((child, path + [operations[0]]))


def prettyPrint(root):
    print (root.value)
    for child in root.children.keys():
        print ('\t', prettyPrint(child))

# nums = [5, 100, 25]
# t = 125
# g = generateTree(nums, t)
# print (findPath(t, g))

nums = [25, 5, 3, 2]
t = 750
g = generateTree(nums, t)
# for k,v in g.children.items():
#     print (v)
print (findPath(t, g))
