import sys

from maze import Maze, path_from


def djikstra(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = [start_node]
    while len(q) > 0:
        q.sort(key=lambda x: (x.cost))
        e = q.pop(0)  # FIFO
        e.visited = True

        if e.type == 'E':
            return path_from(e)

        children = maze.get_possible_movements(e)
        for d in children:
            if not d.visited:
                nowy_koszt = e.cost + maze.move_cost(e, d)
                if nowy_koszt < d.cost:
                    d.cost = nowy_koszt
                    d.parent = e
                    q.append(d)

    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = djikstra(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()