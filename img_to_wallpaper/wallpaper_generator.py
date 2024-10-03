
class Wallpaper_generator:
    """Class that generates the final wallpaper
    """
    def __init__(input_img_path: str, output_img_path: str, output_res:(int,int), shape:str = 'Hexagon', shape_size:int):
        """Contains all the required arguments for wallpaper generation and open the input image

        Args:
            input_img_path (str): path of the input image
            output_img_path (str): path of the output image
            output_res (int,int): two positive integers for the output image generation
            shape_size (int): Sampling shape size
            shape (str, optional): sampling shape in 'Triangle', 'Hexagon'. Defaults to 'Hexagon'.
        """