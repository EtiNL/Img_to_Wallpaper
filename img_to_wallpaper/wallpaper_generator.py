import os
from PIL import Image
from hexagonal_wallpaper import hexagonal_grid, sample_color

class Wallpaper_generator:
    """Class that generates the final wallpaper
    """
    def __init__(input_img_path: str, output_img_path: str = 'output.svg', shape:str = 'Hexagon', shape_size:int):
        """Open the input image and assign all the required arguments for wallpaper generation as class attributes

        Args:
            input_img_path (str): path of the input image
            output_img_path (str): path of the output image. Defaults to 'output.svg'.
            output_res (int,int): two positive integers for the output image generation (must be > shape_size)
            shape_size (int): Sampling shape size
            shape (str, optional): sampling shape in 'Triangle', 'Hexagon'. Defaults to 'Hexagon'.
        """

        #check if input_img_path exists
        assert os.path.isfile(input_img_path)

        #read image
        with Image.open(input_img_path) as im:
            self.input_img = im

        self.output_img_path = output_img_path

        assert shape in ['Hexagon', 'Triangle'], 'shape must either be Hexagon or Triangle'
        self.shape = shape

        assert shape_size > 0, 'Shape must be > 0'
        self.shape_size = shape_size

    def generate_grid(self):
        if self.shape = 'Hexagon':
            self.grid = hexagonal_grid(self.input_img)

    def generate_grid_colors(self):
        self.grid_colors = np.array([sample_color(grid_point, self.size, self.input_img) for grid_point in self.grid])

    def generate_wallpaper(self):
        self.generate_grid()
        self.generate_grid_colors()

        return self.grid, self.grid_colors


if __name__ == '__main__':
    w =  Wallpaper_generator('../screenshot.jpg', output_img_path: str = 'output.svg', 10)
    grid, grid_colors = w.generate_wallpaper()
    print(grid.shape)
    print(grid_colors.shape)