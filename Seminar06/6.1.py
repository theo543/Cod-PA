'''
1. Rezolvați problema programării spectacolelor într-o singură sală utilizând o coadă cu 
priorități.
'''
import queue
def solve(intervals):
    q = queue.PriorityQueue()
    for interval in intervals:
        q.put(interval)
    selected = [q.get()]
    while not q.empty():
        current = q.get()
        if current[0] >= selected[-1][1]:
            selected.append(current)
    return selected

def main():
    test = [(1, 3), (2, 4), (5, 7), (6, 8), (5, 6), (3, 4), (50, 100), (99, 102), (101, 150)]
    print(solve(test))

if __name__ == '__main__':
    main()
