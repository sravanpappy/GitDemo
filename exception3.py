try:
    f=open("G:\\Notnepadd_pyth,,,on\\pmractenfile.mtxt","r")
    f.write("sravan kumar")
    print("not enterd")
except:
        #print("exception is found")
        # print(e)
        try:
            #d=("G:\\Notepadd_python\\practefile.txt","r+")
            d=("G:\\Notepadd_python\\practefile.txt","a")
            d.append("sravankumar")
            print("hi")
        except:
            print("this 1")
finally:
        print("finally")
# except Exception:
	# print("hi")
    # print(Exception)
    
    
# try:
    # s=open("G:\\Notepadd_python\\practefile.txt","a")
    # s.write("Trilochan")

    # s=open("G:\\Notepadd_python\\practefile.txt","r+")
    # print(s.readlines())
# except:
    # print("sivaram is not entered")    
    
    
try:
    linux_intraction()
except Exception:
        print("error")
        print(Exception)