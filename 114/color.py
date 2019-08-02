import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())
    
    @classmethod
    def hex2rgb(self,color):
        """Class method that converts a hex value into an rgb one"""
        if type(color)!=str or len(color)!=7:
            raise ValueError
            
        value = color.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



    @classmethod
    def rgb2hex(self,color):
        """Class method that converts an rgb value into a hex one"""

        if type(color)!=tuple  or any(rgb not in range(0,256) for rgb in color) :
            raise ValueError
        else:
            return '#%02x%02x%02x' % color

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        value  = COLOR_NAMES.get(self.color.upper())
        # if value:
        #     return str(value)
        # else:
        #     return "Unknown"
        return str(value) if value else "Unknown"
        




   #Pybites solution 



# import os
# from string import hexdigits
# import sys
# import urllib.request

# # PREWORK (don't modify): import colors, save to temp file and import
# color_values_module = os.path.join('/tmp', 'color_values.py')
# urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
#                            color_values_module)
# sys.path.append('/tmp')

# # should be importable now
# from color_values import COLOR_NAMES  # noqa E402


# class Color:
#     """Color class.

#     Takes the string of a color name and returns its RGB value.
#     """

#     def __init__(self, color):
#         self.color = color
#         self.rgb = COLOR_NAMES.get(self.color.upper(), None)

#     @classmethod
#     def hex2rgb(cls, hex_value):
#         """Converts a hex value into an rgb one"""
#         error_message = f"{hex_value} is not a valid hex value!"

#         for char in hex_value:
#             if char not in hexdigits:
#                 raise ValueError(error_message)

#         if not len(hex_value) == 7 or not hex_value.startswith("#"):
#             raise ValueError(error_message)

#         return tuple(int(hex_value[i:i + 2], 16) for i in (1, 2, 4))

#     @classmethod
#     def rgb2hex(cls, rgb_value):
#         """Converts an rgb value into a hex one"""
#         error_message = f"{rgb_value} is not a valid RGB value!"

#         if not isinstance(rgb_value, tuple):
#             raise ValueError(error_message)

#         valid = [1 for n in rgb_value if not (0 <= n <= 255)]
#         if sum(valid) > 0:
#             raise ValueError(error_message)

#         return f"#{rgb_value[0]:02x}{rgb_value[1]:02x}{rgb_value[2]:02x}"

#     def __repr__(self):
#         """Returns the repl of the object"""
#         return f"Color('{self.color}')"

#     def __str__(self):
#         """Returns the string value of the color object"""
#         return f"{self.rgb}" if self.rgb else "Unknown"

