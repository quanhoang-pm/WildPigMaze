import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.image as mpimg


# Find some path in the graph.
def findPathInGraph(G, source_node, target_node):
    return nx.shortest_path(G, source_node, target_node)

# Draw the maze path to the output image
def drawMazePath(input_image, output_image, graph_path):
    verts = [(206, 30),]
    codes = [Path.MOVETO]
    del graph_path[0] # Delete the first node in the path, which is the source
    image = mpimg.imread(input_image) # Read the image, change it to list of 'numpy' codes
    fig,ax = plt.subplots(1) # Create figure and axes
    
    # The next 'for' loop is to create list of vertices and list of codes using to draw the path on the images
    for node in graph_path:
        # Convert node of the graph to some point on the image
        point = ()
        point = point + (24 + node[1] * 12, 28 + node[0] * 12,)
        verts.append(point)
        codes.append(Path.LINETO)
    
    path = Path(verts, codes) # Create path with vertices and line
    patch = patches.PathPatch(path, edgecolor = 'red', facecolor = 'none') # Create patch covered by the path
    ax.add_patch(patch) # Add the patch to the axes
    ax.imshow(image) # Display the image
    plt.savefig(output_image)
    plt.show() 
    
def drawExampleMazePath(input_image):
    image = mpimg.imread(input_image)
    fig,ax = plt.subplots(1) # Create figure and axes

    verts = [
        (206., 30.),  
        (206., 90.),  
        (277., 90.),  
        (278., 43.), 
        (254., 43.),
        (254., 138.),
        (230., 138.),
        (230., 234.),
        (182., 234.),
        (182., 186.),
        (86., 186.),
        (86., 258.),
        (38., 258.),
        (38., 139.),
        (134., 139.),
        (134., 91),
        (180., 91),
        (180., 65.),
        (157., 65.),
        (157., 161.),
        (206., 161.),
        (206., 270.)
        ]

    codes = [Path.MOVETO,] + [Path.LINETO] * 21
        
    path = Path(verts, codes) # Create path with vertices and line
    patch = patches.PathPatch(path, edgecolor = 'red', facecolor = 'none') # Create patch covered by the path
    ax.add_patch(patch) # Add the patch to the axes
    ax.imshow(image) # Display the image
    plt.savefig("output_image.jpg")
    plt.show()
    
if __name__ == '__main__':    
    #drawExampleMazePath('images/input_image2.jpg')
    
    path = [(0, 15,'down'), (1, 15, 'down'), (2, 15, 'down'), (3, 15, 'down'),
        (4, 15, 'down'), (5, 15, 'down'), (5, 15, 'right'), (5, 16, 'right'),
        (5, 17, 'right'), (5, 18, 'right'), (5, 19, 'right'), (5, 20, 'right'),
        (5, 21, 'right'), (5, 21, 'up'), (4, 21, 'up'), (3, 21, 'up'), 
        (2, 21, 'up'), (1, 21, 'up'), (1, 21, 'left'), (1, 20, 'left'), 
        (1, 19, 'left'), (1, 19, 'down'), (2, 19, 'down'), (3, 19, 'down'), 
        (4, 19, 'down'), (5, 19, 'down'), (6, 19, 'down'), (7, 19, 'down'), 
        (8, 19, 'down'), (9, 19, 'down'), (9, 19, 'left'), (9, 18, 'left'), 
        (9, 17, 'left'), (9, 17, 'down'), (10, 17, 'down'), (11, 17, 'down'), 
        (12, 17, 'down'), (13, 17, 'down'), (14, 17, 'down'), (15, 17, 'down'), 
        (16, 17, 'down'), (17, 17, 'down'), (17, 17, 'left'), (17, 16, 'left'), 
        (17, 15, 'left'), (17, 14, 'left'), (17, 13, 'left'), (17, 13, 'up'), 
        (16, 13, 'up'), (15, 13, 'up'), (14, 13, 'up'), (13, 13, 'up'), 
        (13, 13, 'left'), (13, 12, 'left'), (13, 11, 'left'), (13, 10, 'left'), 
        (13, 9, 'left'), (13, 8, 'left'), (13, 7, 'left'), (13, 6, 'left'), 
        (13, 5, 'left'), (13, 5, 'down'), (14, 5, 'down'), (15, 5, 'down'), 
        (16, 5, 'down'), (17, 5, 'down'), (18, 5, 'down'), (19, 5, 'down'), 
        (19, 5, 'left'), (19, 4, 'left'), (19, 3, 'left'), (19, 2, 'left'), 
        (19, 1, 'left'), (19, 1, 'up'), (18, 1, 'up'), (17, 1, 'up'), 
        (16, 1, 'up'), (15, 1, 'up'), (14, 1, 'up'), (13, 1, 'up'), 
        (12, 1, 'up'), (11, 1, 'up'), (10, 1, 'up'), (9, 1, 'up'), (9, 1, 'right'), 
        (9, 2, 'right'), (9, 3, 'right'), (9, 4, 'right'), (9, 5, 'right'), 
        (9, 6, 'right'), (9, 7, 'right'), (9, 8, 'right'), (9, 9, 'right'), 
        (9, 9, 'up'), (8, 9, 'up'), (7, 9, 'up'), (6, 9, 'up'), (5, 9, 'up'), 
        (5, 9, 'right'), (5, 10, 'right'), (5, 11, 'right'), (5, 12, 'right'), (5, 13, 'right'), 
        (5, 13, 'up'), (4, 13, 'up'), (3, 13, 'up'), 
        (3, 13, 'left'),  (3, 12, 'left'), (3, 11, 'left'), 
        (3, 11, 'down'), (4, 11, 'down'), (5, 11, 'down'), (6, 11, 'down'), (7, 11, 'down'), 
        (8, 11, 'down'), (9, 11, 'down'), (10, 11, 'down'), (11, 11, 'down'), 
        (11, 11, 'right'), (11, 12, 'right'), (11, 13, 'right'), (11, 14, 'right'), (11, 15, 'right'), 
        (11, 15, 'down'), (12, 15, 'down'), (13, 15, 'down'), (14, 15, 'down'), (15, 15, 'down'), 
        (16, 15, 'down'), (17, 15, 'down'), (18, 15, 'down'), (19, 15, 'down'), (20, 15, 'down'), 
    ]
    
    drawMazePath('images/input_image2.jpg', 'images/output_image.jpg', path)
