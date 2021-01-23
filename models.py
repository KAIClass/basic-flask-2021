import random
import numpy as np

'''
class company:
    def __init__(self,price):
        self.share_price = price
        self.ret = 0
        self.share_percentage=100
    def buy(self,qty,price):
        self.share_price += 0.00005*self.share_price
    def sell(self,qty,price):
        self.share_price -= 0.00005*self.share_price
    def LoSs(self):
        while
    def trade(self,cost,misc,sell):
        self.ret = sell - (cost + misc)
        if(self.ret<0):
            Loss()
        elif(ret>0):
            self.sell(10)
        return ret

    Sorry For Commenting Your codes Out I just coulnt understand your codes so I developed mines :)
'''

# And Mujhe abhi parent class and child class ka concept nhi clear hai so maine comments mein likh diya hai ki kha kya call hona chahiye...
# Mujhe class in python ka knowledge ka idea nhi hai.... so if any mistake pls tell me

class person: #A class of person i.e, investor ki kitna paisa hai uske paas and future value calculate karne ke liye
    def Commits(self,i): #this will contain all the logs of an investor related to his money....... abhi ke liye pass kar de rha cuz cant write the codes for a file
        pass
    def __init__(self,amount):
        self.amount = amount #how much amount he has to invest
        self.amountrelated = 0
         

    def Remove(self,amount): #if he buys any share then amount left with him or he pulls out some amount for various reasons
        self.amount -= amount
        self.amountrelated += 1
        Commits(self.amountrelated) 
    def Add(self,amount): #if he sells any share then he will get some money back which could be used for future investments or if he wants to add some more money for investments
        self.amount += amount
        self.amountrelated += 1
        Commits(self.amountrelated)
    def can_invest(self, amount): # check karne ke liye ki kitna paisa he can spend or not
        if amount>self.amount:
            return False
        else:
            return True
    def check_amount(self): #return the amount he has to invest in something
        return self.amount
    def seeCommits(self): #if an investor wants to see his log he can see it using this function.... again file handling ka code thode time baad likhenge
        pass
    def CompanyInvested(self): #will show us all the companies invested in aur kitna share hai unme
        pass
    
    

class investedcompany: #this class is for invested companies ki humne agar kisi company mein invest kiya then uska records
    def Commits(self): #kuch bhi paisa related kaam karne par logs will be updated..... Abhi no idea on structure so left blank
        pass
    def __init__(self,price,share):
        self.share = share #how much share of the company I have
        self.share_price = price #for how much I bought the share
        self.mprice = share/price #this variable stores the market price of each 
    
    def update(self,mprice): #will be called anytime market mein company ka share price badha hai ki dooba hai
        self.mprice = mprice
        self.share_price = self.share * self.mprice

    
    def share_value(self,mprice): # will give you your current share price
        update(mprice)
        return self.share_price

    def buy(self,share_qty,mprice): #share buy krne par this will be called
        update(mprice)
        self.share += share_qty
        self.share_price += qty*mprice
        # NOw it should call Remove class to sub money from investor
    
    def sell(self,share_qty,mprice): #share buy krne par this will be called
        update(mprice)
        self.share -= share_qty
        self.share_price -= qty*mprice
        # NOw it should call Add class to add money to investor
        # agar share price zero ho jaaye toh yeh comany ka object bhi delete ho jaana chahiye cuz mera kuch bhi share nhi hai and add to list on investor ke wish pe ki to invest list mein add karu ki nhi
    
class toinvestCompany(): #this class is for companies jisme hamari nazar hai future investments ke liye
    def __init__(self,mprice,share): #initializing the object
        self.share= share
        self.mprice = mprice
    def updown(self, mprice,share): #check and tell ki market value down hai ki up to know ki invest kare ki nhi .. isme baad mein hum kitna invest kare and all ka definition daal sakte hai
        if mprice>self.mprice:
            return False
        else:
            return True

    def update(self,mprice,share): #will be called anytime to know ki kya market price kya hai company ka share ka and kitna share hai
        updown(mprice,share)
        self.mprice = mprice
        self.share = share
    
    #Iss class mein agar koi company mein share kharid liye ho fir bhi honi chahiye cuz kya pta future mein investments karle 

    


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
        return np.mean((self.line_mag-self.y))**2 #return np.mean((self.line_mag-self.y_a))**2 was the original code and replaced self.y_a with self.y as actual values are stored in it
    def gradient_m(self):
        return 2*np.mean(self.error_mag)*self.x #return 2*np.mean(self.error_mag)*x was the original code and replaced x with self.x
    def gradient_c(self):
        return 2*np.mean(self.error_mag)
    def fit(self,iters):
        for i in range(iters):
            self.m -= self.gradient_m()
            self.c -= self.gradient_c() 
    def predict(self,test_x):
        return (self.m * test_x) + self.c