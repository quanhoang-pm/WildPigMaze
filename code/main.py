from step_1_create_01matrix_from_image_input import finalMatrix2
from step_2_convert_matrix_to_graph_and_io_node import createGraphAndIoNodes
from step_3_find_and_draw_maze_path import findPathInGraph, drawMazePath

input_image_path = '../images/input_image2.jpg'
output_image_path = '../images/output_image.jpg'

black_white_array = finalMatrix2(input_image_path)
G, input_node, output_node = createGraphAndIoNodes(black_white_array)
maze_path = findPathInGraph(G, input_node, output_node)
drawMazePath(input_image_path, output_image_path, maze_path)
# print(black_white_array)
# print(maze_path)
