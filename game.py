#function to display content
def display(list):
    for i in list:
        for j in i:
            print(j,end=" ")
        print("\n")

#funtion to find present line neighbour cell values 
def present_cells(list,row,column,neigbours):
    if column-1 >= 0 :
        neigbours.append(list[row][column-1])               
    if column+1 < len(list[row]):
        neigbours.append(list[row][column+1])
    return neigbours 


#function to find upper niebourcell values
def upper_cells(list,row,column,neigbours):
    if row-1 >= 0:
        neigbours.append(list[row-1][column])
        if column-1 >= 0 :
            neigbours.append(list[row-1][column-1])
        if column+1 < len(list[row-1]):
            neigbours.append(list[row-1][column+1])
    return neigbours


#function to find down nigbour cell values
def down_cells(list,row,column,neigbours):
    if row+1 < len(list):
        neigbours.append(list[row+1][column])
        if column-1 >= 0 :
            neigbours.append(list[row+1][column-1])
        if column+1 < len(list[row+1]):
            neigbours.append(list[row+1][column+1])
    return neigbours             
                  
 
# live cell value will change depends on its neigbours value                
def livecell_rule(list,row,column,neigbours):
    if neigbours.count('*') in [2,3]:
        list[row][column]='*' #Any live cell with two or three live neighbours lives on to the next generation.
    else:
        list[row][column]='-' #Any live cell with fewer than two live neighbours dies, as if by underpopulation ,Any live cell with more than three live neighbours dies, as if by overpopulation.
    return list 

# dead cell value will change depends on its neigbours value
def deadcell_rule(list,row,column,neigbours):
    if neigbours.count('*') == 3: #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        list[row][column]='*'
    else:
        list[row][column]='-'
    return list    

        

def main():
    list=[['*','-','*','*','-'],['*','*','-','-','*'],['-','*','-','*','-']] # '*' indicates livecell, '-' indicates dead cell
    rows=len(list)
    print("----1st Generation---")
    display(list)
    for i in range(rows):
        for j in range(len(list[i])):
            neigbours=[]
            present_cell=list[i][j]
            
            present_cells(list,i,j,neigbours)
            upper_cells(list,i,j,neigbours)
            down_cells(list,i,j,neigbours)
            if present_cell == '*':
                livecell_rule(list,i,j,neigbours)
            else:
                deadcell_rule(list,i,j,neigbours)    
                  
            #print(neigbours)
    print("----2nd Generation---")                                       
    display(list)
                    


if __name__=="__main__":
    main()  