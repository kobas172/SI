import sys

from maze import Maze, path_from


def gbfs(maze):
    start_node = maze.find_node('S')
    end_node = maze.find_node('E')
    q = [start_node]
    start_node.cost = 0
    while len(q) > 0:
        q.sort(key=lambda x: x.cost)
        e = q.pop(0)  # FIFO
        e.visited = True
        if e.type == 'E':
            return path_from(e)

        children = maze.get_possible_movements(e)
        for child in children:
            if not child.visited:
                nowy_koszt = abs(child.x - end_node.x) + abs(child.y - end_node.y)
                child.cost = nowy_koszt
                child.parent = e
                q.append(child)


    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = gbfs(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()