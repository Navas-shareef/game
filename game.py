def display(array):
	for i in array:
		for j in i:
			print(j,end=" ")
		print("\n")	



def rule1(livecell,deadcell):
	if deadcell>=3:
		if livecell==2 or livecell==3:
			return 1	
		else: 
				
			return 0
	else:
		return 0		
	




def main():
	arr=[[0,1,0,1,0],[0,1,0,0,1],[0,1,0,1,0]]
	rows=3
	cols=5
	display(arr)
	

	for i in range(rows):
		for j in range(cols):
			livecell=0
			deadcell=0

			str2=arr[i][j]
			
			
			if j-1 >= 0 :
				if arr[i][j]==arr[i][j-1]:
					if str2==1:
						livecell +=1
					else:
						deadcell=livecell	
			if j+1 < len(arr[i]):
				if arr[i][j]==arr[i][j+1]:
					if str2==1:
						livecell +=1
					else:
						deadcell=livecell
				arr[i][j]=rule1(livecell,deadcell)
				



			if i-1 >= 0:
				str1=arr[i-1][j]
				
				if arr[i][j]==str1:
					if str2==1:
						livecell +=1
					else:
						deadcell=livecell
				arr[i][j]=rule1(livecell,deadcell)
				
				if j-1 >= 0 :

					if str2==arr[i-1][j-1]:
						if str2==1:
							livecell +=1
						else:
							deadcell=livecell
					arr[i][j]=rule1(livecell,deadcell)
					
				if j+1 < len(arr[i-1]):
					if str2==arr[i-1][j+1]:
						if str2==1:
							livecell +=1
						else:
							deadcell=livecell
					arr[i][j]=rule1(livecell,deadcell)
					


			if i+1 < len(arr):
				if str2<len(arr):
					str3=arr[i+1][j]
					if str2==str3:
						if str2==1:
							livecell +=1
						else:
							deadcell=livecell
					
					arr[i][j]=rule1(livecell,deadcell)
					
					if j-1 >= 0 :
						if str2==arr[i+1][j-1]:
							if str2==1:
								livecell +=1
							else:
								deadcell=livecell
						arr[i][j]=rule1(livecell,deadcell)
						
					if j+1 < len(arr[i+1]) :
						#print(i)
						if str2==arr[i+1][j+1]:
							if str2==1:
								livecell +=1
							else:
								deadcell=livecell
						arr[i][j]=rule1(livecell,deadcell)
											
		display(arr)
					


if __name__=="__main__":
	main()	