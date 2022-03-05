import sys

from maze import Maze, path_from


def dfs(maze):
    start_node = maze.find_node('S')
    q = [start_node]
    start_node.visited = True
    while len(q) > 0:
        e = q.pop(0)  # FIFO
        e.visited = True
        if e.type == 'E':
            return path_from(e)
        children = maze.get_possible_movements(e)
        for child in children:
            if not child.visited:
                child.parent = e
                q.append(child)
    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = dfs(maze)
print()
maze.draw()
