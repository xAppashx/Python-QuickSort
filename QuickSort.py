
#Setting up parameters
def QuickSort(ArrayToSort): 
      
      Array = ArrayToSort.copy()
      SortedArray = QuickSortRecursion(Array, 0, len(Array)-1)
      return (SortedArray)
#Def QuickSort


# Will do the recursion part
def QuickSortRecursion(Array, Low, High):
      
      if (Low < High):
            
            Pi = Particiones(Array, Low, High)
            QuickSortRecursion(Array, Low, Pi - 1)
            QuickSortRecursion(Array, Pi+1, High)
      # if
      
      return(Array)
      
#def QuickSortRecursion


# Sorts the array
def Particiones(Array, Low, High):
      
      Lengh = len(Array) 
      Pivot = Array[High]
      Small = Low - 1 
      
      for Loop in range(Low, High):
               
               #Sets up all nums inferior to the pivot to the left of the array
               if (Array[Loop] < Pivot): 
                     Small = Small + 1
                     Temp = Array[Small]
                     Array[Small] = Array[Loop]
                     Array[Loop] = Temp
               #if (Array[Loop] < Pivot)
               
      #For Loop in range
      
      
      #Sets the pivot in its respective spot
      Temp = Array[Small + 1]
      Array[Small + 1] = Array[High]
      Array[High] = Temp
      
      return (Small + 1)
      
# def Particiones




# Test of the use // Feel free to delete the following lines to use the funtions only
Array = [3, 2, 1, 4, 5, 14, 22, 63, 6, 53, 22, 12, 45, 213, 53, 233, 41, 98]

#Call the QuickSort function and send only the array to sort as parameter
SortedArray = QuickSort(Array) 

print("Original array: ", Array)
print("Sorted array: ", SortedArray)

