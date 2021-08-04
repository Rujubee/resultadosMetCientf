# Python program for implementation of Bubble Sort
# Provided by GeeksForGeeks

import time
import os
import psutil

def file_read(fname):
        with open(fname) as fd:
                for line in fd:
                        content_array = [int(elt.strip()) for elt in line.split(',')]

                return content_array
            
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
'''arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),'''
    
if __name__ == "__main__":
    
    #sys.setrecursionlimit(1000000000)
    #threading.stack_size(104857600)
    
    filename = input('Digite o nome do arquivo:')

    array = file_read(filename)
    print('Conjunto de entrada: ')
    #print(array)
    
    n = len(array)
    
    inicio = time.time()
    # Function Call
    bubbleSort(array)
    fim = time.time()
    
    print("Conjunto ordenado: ")
    #print(array)
    
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)  # in bytes
    print(f'Memory Report: {psutil.virtual_memory()}')  # physical memory usage
    print(f'\nMemory percent used: {psutil.virtual_memory().percent}%')
    
    print(f'Elapsed time (Bubble): {fim - inicio}')