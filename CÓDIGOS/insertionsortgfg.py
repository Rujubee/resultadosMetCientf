# Python program for implementation of Insertion Sort
# Function to do insertion sort

import time
import os
import psutil

def file_read(fname):
        with open(fname) as fd:
                for line in fd:
                        content_array = [int(elt.strip()) for elt in line.split(',')]

                return content_array
            
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
'''arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])'''
    
if __name__ == "__main__":
    
    filename = input('Digite o nome do arquivo:')

    array = file_read(filename)
    print('Conjunto de entrada: ')

    #print(array)
    
    inicio = time.time()
    # Function Call
    insertionSort(array)
    fim = time.time()
    
    print("Conjunto ordenado!")
    
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)  # in bytes
    print(f'Memory Report: {psutil.virtual_memory()}')  # physical memory usage
    print(f'\nMemory percent used: {psutil.virtual_memory().percent}%')
    
    print(f'Elapsed time (Insertion): {(fim - inicio):.5f}')
    
# This code is contributed by Mohit Kumra