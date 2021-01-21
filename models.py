import random
import numpy as np

class company:
    def __init__(self,price):
        self.share_price = price
        self.ret = 0
    def buy(self,qty):
        self.share_price += 0.00005*self.share_price
    def sell(self,qty):
        self.share_price -= 0.00005*self.share_price
    def trade(self,cost,misc,sell):
        self.ret = sell - (cost + misc)
        if(ret<0):
            self.sell(10)
        elif(ret>0):
            self.sell(10)
        return ret

class regression:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.m = [0]*len(x.T)
        self.c = 2
        self.line_mag = self.m*self.x + self.c
        self.y_p = self.line_mag
        self.error_mag = self.line_mag - self.y_p
    def error(self):
        return np.mean((self.line_mag-self.y_a))**2
    def gradient_m(self):
        return 2*np.mean(self.error_mag)*x
    def gradient_c(self):
        return 2*np.mean(self.error_mag)
    def fit(self,iters):
        for i in range(iters):
            self.m -= self.gradient_m()
            self.c -= self.gradient_c() 
    def predict(self,test_x):
        return (self.m * test_x) + self.c