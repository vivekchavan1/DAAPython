import heapq

class Node:
    def __init__(self, freq, sym, left=None, right=None):
        self.freq, self.sym, self.left, self.right = freq, sym, left, right
    def __lt__(self, other): return self.freq < other.freq

def print_codes(node, code=''):
    if node.left:  print_codes(node.left, code + '0')
    if node.right: print_codes(node.right, code + '1')
    if not node.left and not node.right: print(f"{node.sym} -> {code}")

n = int(input("Enter number of characters: "))
items = [(input(f"Char {i+1}: "), int(input("Frequency: "))) for i in range(n)]
heap = [Node(f, c) for c, f in items]
heapq.heapify(heap)

while len(heap) > 1:
    l, r = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, Node(l.freq + r.freq, None, l, r))

print("\nHuffman Codes:")
print_codes(heap[0])
