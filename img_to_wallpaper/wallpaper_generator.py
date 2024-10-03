import os
from PIL import Image

class Wallpaper_generator:
    """Class that generates the final wallpaper
    """
    def __init__(input_img_path: str, output_img_path: str, output_res:(int,int), shape:str = 'Hexagon', shape_size:int):
        """Contains all the required arguments for wallpaper generation and open the input image

        Args:
            input_img_path (str): path of the input image
            output_img_path (str): path of the output image
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

        assert output_res[0] > shape_size and output_res[1] > shape_size 
        self.output_res = output_res

        assert shape in ['Hexagon', 'Triangle'], 'shape must either be Hexagon or Triangle'
        self.shape = shape

        assert shape_size > 0, 'Shape must be > 0'
        self.shape_size = shape_size