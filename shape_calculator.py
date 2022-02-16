class Rectangle:


    def __init__(self, inputWidth, inputHeight):
        self.width = inputWidth
        self.height = inputHeight
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, inputWidth):
        self.width = inputWidth
    
    def set_height(self, inputHeight):
        self.height = inputHeight
    
    def get_area(self):
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50:
            return "Too big for picture."
        if self.height > 50:
            return "Too big for picture."
        else:
            pict = ''
            for i in range(0,self.height):
                pict += '*'*self.width + '\n'
            return pict
    
    # shape is a new polygon that wants to be fitted in the rectangle
    def get_amount_inside(self, shape):
        amount = self.get_area() / shape.get_area() 
        return int(amount)


class Square(Rectangle):


    def __init__(self, inputSide):
        self.width = inputSide
        self.height = inputSide

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, inputSide):
        self.set_width(inputSide)
        self.set_height(inputSide)