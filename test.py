import signal
import time


class car():
     
    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# both objects have different self which
# contain their attributes
# audi = car("blue","audi a4")
# ferrari = car("ferrari 488", "green")
 
# audi.show()     # same output as car.show(audi)
# ferrari.show()  # same output as car.show(ferrari)


class test:
    def __init__(self) -> None:
        return None

test()