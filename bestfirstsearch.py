from collections import defaultdict
hurestic = {"A": 40,
            "B": 32,
            "C": 25,
            "D": 35,
            "E": 19,
            "F": 17,
            "H": 10,
            "G": 0}
cost = {"AB": 11,
        "AC": 14,
        "AD": 7,
        "BE": 15,
        "DE": 25,
        "CE": 8,
        "CF": 10,
        "EH": 9,
        "HG": 10,
        "FG": 20
        }
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
# function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def cost(self, path):
        c = 0
        count = 0
        al = ""
        for i in path:
            count = count + 1
        for i in range(count - 1):
            al = path[i] + path[i + 1]
            c = c + cost.get(al)

        print("Best First Path Cost is :", c)

    def minNode(self, queue):
        hl = []
        counter = 1
        mnode = ""
        for i in queue:
            hl.append(hurestic.get(i))
        m = max(hl)
        for i in hl:
            if i < m:
                m = i
                counter = counter + 1
        for x in range(counter):
            mnode = queue[x]

        return hl, m, mnode

    # Function to print a BFS of graph
    def BFS(self, s, f):
        Queue = []
        Visited = []
        path = []
        print("Your searching node is  ", f, "")
        print()
        print("Breadth First Traversal starting from vertex: ", s, "")

        Queue.append(s)
        Visited.append(s)

        while Queue:
            hl, mn, mv = self.minNode(Queue)

            bool = 0

            # print ("   ",hl, "   ",mn, "   min node:",mv)
            path.append(mv)

            if mv == f:
                bool = 1

                print(mv, " is Found")
                print()
                print("Path is: ")
                for i in path:
                    print(i, end="   ")
                print()
                self.cost(path)

                break
            Queue.remove(mv)

            for j in self.graph[mv]:
                if j not in Visited:
                    Queue.append(j)
                    Visited.append(j)

        if bool == 0:
            print(f, " Not Found!")


def main():
    g = Graph()
    g.addEdge("A", "B")
    g.addEdge("A", "D")
    g.addEdge("A", "C")
    g.addEdge("B", "E")
    g.addEdge("C", "E")
    g.addEdge("C", "F")
    g.addEdge("D", "F")
    g.addEdge("E", "H")
    g.addEdge("H", "G")
    g.addEdge("F", "G")

    print()
    g.BFS("A", "G")


main()
