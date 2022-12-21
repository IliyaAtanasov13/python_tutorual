
class Fruit(object):

    def __init__(self):
        print('Fruits are good for you!!')

    def nutrition(self):
        print('The nutritionс that the fruits give are vital to a healthy life')

    def fruit_shape(self):
        print('The shape of the fruits can be...')


class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print('As well as the apples!')

    def nutrition(self):
        super(Apple, self).__init__()
        print('It gives you the vitamin C and many more...')

    def color(self):
        print('The color of the apple is green.')


a = Fruit()
a.nutrition()
a.fruit_shape()
print()
b = Apple()
b.nutrition()
b.color()
