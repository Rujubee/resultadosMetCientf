# Python program for implementation of MergeSort
# Provided by GeeksForGeeks

import time
import os
import psutil

def file_read(fname):
        with open(fname) as fd:
                for line in fd:
                        content_array = [int(elt.strip()) for elt in line.split(',')]

                return content_array
            
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
'''if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)'''
    
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
    mergeSort(array)
    fim = time.time()
    
    print("Conjunto ordenado: ")
    #print(array)
    
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)  # in bytes
    print(f'Memory Report: {psutil.virtual_memory()}')  # physical memory usage
    print(f'\nMemory percent used: {psutil.virtual_memory().percent}%')
    
    print(f'Elapsed time (Merge): {fim - inicio}')

# This code is contributed by Mayank Khanna
