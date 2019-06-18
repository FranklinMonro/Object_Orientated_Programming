def load_file():
    try:
        f = open('input.txt', 'r+')#open file
    except NoSuchFile:
        return "No Such File"

    for lines in f.readlines():#for loop to read through txt file
        data = lines[0:4]#splice txt file from 0 to 3
        data2 = lines[4:]#splice txt file index 4 to end
        data3 = data2.split(',')#split at ,
        data4 = [int(i) for i in data3] #cast string to integer
        if data == "min:":#if statement when data is equal to min
            print("The min of [" + data2 + "] is: " + str(min(data4)))
        elif data == "max:":#if statement when data is equal to max
            print("The max of [" + data2 + "] is: " + str(max(data4)))
        elif data == "avg:":
            print("The avg of [" + data2 + "] is: " + str(sum(data4)/len(data4)))
        else:
            print("No Such operation")
                
        
    f.close()#close file
    
            
  
        
    

