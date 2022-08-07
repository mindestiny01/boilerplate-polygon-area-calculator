
# All the similar habits will coded inside Rectangle class
class Rectangle:
    # Constructor, take width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Default
    def __str__(self): 
        return f'Rectangle(width={self.width}, height={self.height})'

    # Setter
    def set_width(self, width): 
        self.width = width
    
    def set_height(self, height): 
        self.height = height

    # Area Calculation
    def get_area(self):
        return self.width * self.height 

    # Perimeter Calculation
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    # Diagonal Calculation
    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    # Polygon Drawer
    def get_picture(self):
        polygon_picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        polygon_picture = ('*' * self.width  + '\n') * self.height

        return polygon_picture
        
    # Testing
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()
    


# This Square just contain set_height
class Square(Rectangle):
    def __init__(self, side):
        # Inherit the constructor
        super().__init__(side, side)

    # Default
    def __str__(self):
        return f'Square(side={self.width})'

    # Setter
    def set_side(self, side):
        self.height = side
        self.width = side
