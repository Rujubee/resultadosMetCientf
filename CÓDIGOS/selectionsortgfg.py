# Python program for implementation of Selection
# Sort
import time
import os
import psutil

def file_read(fname):
        with open(fname) as fd:
                for line in fd:
                        content_array = [int(elt.strip()) for elt in line.split(',')]

                return content_array
            
 
# Traverse through all array elements
def selectionSort(arr):
    for i in range(len(arr)):
         
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                 
        # Swap the found minimum element with
        # the first element       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
# Driver code to test above

if __name__ == "__main__":
    
    filename = input('Digite o nome do arquivo:')

    array = file_read(filename)
    print('Conjunto de entrada: ')

    #print(array)
    
    inicio = time.time()
    # Function Call
    selectionSort(array)
    fim = time.time()
    
    print("Conjunto ordenado!")
    
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)  # in bytes
    print(f'Memory Report: {psutil.virtual_memory()}')  # physical memory usage
    print(f'\nMemory percent used: {psutil.virtual_memory().percent}%')
    
    print(f'Elapsed time (Selection): {(fim - inicio):.5f}')