photo=open("G:\\Notepadd_python\\IMG-20180915-WA0014.jpg","w+b")
photo=open("G:\\Notepadd_python\\IMG-20180915-WA0014.jpg","r+b")
photo1=photo.readlines()
print(photo1)





def main(): 
    try: 
        #Relative Path 
        img = Image.open("G:\\Notepadd_python\\IMG-20180915-WA0014.jpg")  
          
        #In-place modification 
        img.thumbnail((200, 20))  
          
        img.save("thumb.jpg")
        print(thumb.jpg)
    except IOError: 
        pass
  
    if __name__ == "__main__": 
        main()

print(main)