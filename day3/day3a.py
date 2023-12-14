# open input.txt file
with open('input.txt') as input_file:
    schematic = []
    
    count = 0
    for line in input_file:
        schematic.append(line)
        
        print(line.split("."))
        
        #for elem in line.split("."):
            #if elem != "" or elem != "\n":
                #print(elem)
        
        if count == 3:        
            break
        else:
            count+=1
    