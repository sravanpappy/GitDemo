
#### Senario - 1
def gst(OP,NP):
    
    OP = int(input("Enter Original price:-"))
    NP = int(input("enter Net Price:-"))
    GST_amount = NP - OP

    GP = ((GST_amount * 100) / OP)
    print("GST = ",end='') 
      
    print(round(GP),end='') 
    print("%")
gst(100,120)   

# @gst
# def new_gst(OP,NP):
    # return new_gst
# price(new_gst())    


       
    #### Senario - 2

    # Original_price = 100
    # Net_price = 120
    # GST_amount = Net_price - Original_price

    # GST_percent = ((GST_amount * 100) / Original_price)
    # print("GST = ",end='') 
      
    # print(GST_percent,end='') 
    # print("%")



### Senario - 3


# Original_price=float(input("Enter original Price:-"))

# Net_price = float(input("Enter Net Price:-"))

# GST_amount = Net_price - Original_price

# GST_percent = ((GST_amount * 100) / Original_price)

# print("GST = ",end='')  

 

# print(GST_percent,end='')  

# print("%")


