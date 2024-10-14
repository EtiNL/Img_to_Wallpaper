import numpy as np
# create the grid of points in the center of the hexagons the same size as the image
# uses flat hexagons
def hexagonal_grid(img: np.array, size: int) -> np.array:
    #first point is 0,0
    hexagonal_grid = []
    img_width = img.shape[1]
    img_heigth = img.shape[0]

    #horiz = 3/2 * size
    #vert = sqrt(3) * size

    width = 0
    height = 0
    even_row = True

    while height < img_heigth:

        if even_row:
            width = 0
        else:
            width = 3/2 * size / 2

        while width < img_width:
            hexagonal_grid.append((width, height))
            width += 3/2 * size
        
        even_row = not(even_row)
        height += np.sqrt(3) * size

    return np.array(hexagonal_grid)

def sample_color(center_point, size, img):
    #medium color in the inner square of the hexagone of center: center_point and size: size
    color_samples = []
    img_width = img.shape[1]
    img_heigth = img.shape[0]
    for i in range(-size//2, size//2):
        for j in range(-size//2, size//2):
            sample_x = center_point[0] + i
            sample_y = center_point[1] + j

            if sample_x>=0 and sample_x<img_heigth and sample_y>=0 and sample_y<img_width:
                color_samples.append(img[sample_x, sample_y])
    
    mean_color_hexagon = np.mean(np.array(color_samples), axis = 0)

    return mean_color_hexagon

