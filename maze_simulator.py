from maze_helper import *

maze = sample_maze() #Generate maze

def dfs(list_of_connected_points,current_point,explored,current_path):
    
    current_path.append(current_point)
    explored.append(current_point)
    adj_points = get_adjacent_positions(maze, current_point)
    if len(adj_points) > 2 and current_point not in list_of_connected_points:
        list_of_connected_points.append(current_point)
    for path in adj_points:
        if path not in explored:
            return(dfs(list_of_connected_points,path,explored,current_path))

    if symbol_at(maze, current_point) == "X":
        for path in current_path:
            if symbol_at(maze, path) != "O":
                add_walk_symbol(maze, path)
        print_maze(maze)
        return True

    else:
        last_intercect = list_of_connected_points[len(list_of_connected_points) - 1]

        check = all(elem in explored for elem in get_adjacent_positions(maze, last_intercect))
        if check:
            list_of_connected_points.remove(last_intercect)

        index = current_path.index(list_of_connected_points[len(list_of_connected_points)-1])
        current_path = current_path[0:index+1]

        return(dfs(list_of_connected_points, list_of_connected_points[len(list_of_connected_points)-1], explored,current_path))


dfs([],(5,0),explored=[],current_path=[])
