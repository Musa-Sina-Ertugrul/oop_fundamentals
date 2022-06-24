class Car():
    #I initilized variables with conturactor and i added __ on beginnig of variables so,their named changed.
    #Therefore, these variables will not be reachable from objects with their name.
    #It is like fake private keyword.
    def __init__(self,make,model,color,year,price ):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__price = price
    #getter and setter mothods
    def get_make(self):
        return __make
    def get_model(self):
        return __model
    def get_color(self):
        return __color
    def get_year(self):
        return __year
    def get_price(self):
        return __price
    def set_make(self,make):
        self.__make = make
    def set_model(self,model):
        self.__model = model
    def set_color(self,color):
        self.__color = color
    def set_year(self,year):
        self.__year = year
    def set_price(self,price):
        self.__price = price
    #string representation of class
    def __str__(self):
        return "Car make: {}, model: {}, color: {}, year: {}, price: {}".format(get_make,get_model,get_color,get_year,get_price)
    #object representation of class
    def __repr__(self):
        return "Car({},{},{},{},{})".format(get_make,get_model,get_color,get_year,get_price)
