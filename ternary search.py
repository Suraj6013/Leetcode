''' Write a python program to maintain club members, sort on roll numbers in
ascending order. Write function “Ternary Search” to search whether particular
student is member of club or not. Ternary search is modified binary search that
divides array into 3 halves instead of two. '''

def TernarySearch(): #Creating A Ternary Search Function.
   
    ListOfMembers = [] #Creating An Empty List.
   
    NumberOfMembers = int(input("Enter The Number Of Memebers In The Club: "))
    #Accepting The Total Number Of Members From The User.
   
    for i in range(NumberOfMembers):
        Members = input(f"Enter rollNo of member {i+1}: ")
        #Accepting The Names Of Members From The User.
       
        ListOfMembers.append(Members) #Adding Members To The Empty List.
       
    def BubbleSort(List):
       
        n = len(List)
        #Traverse Through All Array.
       
        for i in range (n-1):
            #Last i Elements Are Already In Place.
            for j in range(0, n - i -1):
                #Traverse The Array From 0 To n - i - 1.
                #Swap If The Element Is Greater Than The Next Element.
               
                if List[j] > List[j +1]:
                    List[j], List[j + 1] = List[j + 1], List[j]
                   
        print(f"The List Of Sorted Members Is: {List}")
       
    BubbleSort(ListOfMembers) #Sorting The List.
               
    MemberToBeFound = input("Enter The Member To Be Searched: ")
    #Taking Input Of Key From The User.
       
    print(f"Members In The Club: {ListOfMembers}") #Printing The Sorted List.
   
    Min = 0 #Declaring The Minimum as 0.
    Max = len(ListOfMembers) - 1 #Declaring The Maximum As The Last Index Of The List.
   
    for i in range(len(ListOfMembers)):
                   
        Mid1 = round(Min + ((Max - Min)/3))
        #Dividing The List In Three Parts Using Mid 1 And Mid 2.
        Mid2 = round(Max - ((Max - Min)/3))
               
        if MemberToBeFound == ListOfMembers[Mid1]: #If Key Is At Mid 1.
            print(f"{MemberToBeFound} Is In The Club And At Position {Mid1+1}")
            break
               
        elif MemberToBeFound == ListOfMembers[Mid2]: #If Key Is At Mid 2.
            print(f"{MemberToBeFound} Is In The Club And At Position {Mid2+1}")
            break
                       
        elif MemberToBeFound < ListOfMembers[Mid1]: #If Key Is Less Mid 1.
            Max = Mid1
       
        elif MemberToBeFound > ListOfMembers[Mid1] and MemberToBeFound < ListOfMembers[Mid2]:
            #If Key Is Between Mid 1 And Mid 2.
           
            Min = Mid1
            Max = Mid2
       
        elif MemberToBeFound > ListOfMembers[Mid2]: #If Key Is More Mid 2.
            Min = Mid2
           
    else: #Will Be Executed When The Condition Of For Loop Is Unsatisfied.
        print(f"Could Not Find {MemberToBeFound} In The Club.")

TernarySearch() #Calling The Function.