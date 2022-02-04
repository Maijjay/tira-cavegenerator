"""
adad
"""
import graphs as g

def app():
    """Starts the program"""
    row = 5
    col = 5
    percent = 60
    graph = g.make_graph(row, col, percent)
    g.print_graph(row, col, graph)

    for _ in range(1):
        g.modify_graph(row, col, graph)
        print("----------")
    g.search(row, col, graph)
    g.print_graph(row, col, graph)


def main():
    """Statts app()"""
    app()
    print("   ")

if __name__ == "__main__":
    main()
