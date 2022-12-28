'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01  (B)
OS Assignment # 3
Submitted to Mam Asia Aman & Mam Reeda Saeed

GitHub Repo URL: https://github.com/muhammad-mobeen/Merge-Sort-with-Multi-Threading
Merge Sort Reference: My own code

Note: In my code it is not a requirement that size of list must be greater than 4. Any size of array is acceptable.

Explanation of Task:-
The program gets lists of elements from user and than divedes the list into 4 parts to pass them individually
to 4 other threads. After the threads executes the sorted list are again combined in pairs of 2.
We use Multi-threading again to sort the individual pairs. Now we get 2 final pairs so merge sort is applied
again for the final time and we get the final sorted list of elements.
'''
import threading

def threads_distributor(lst):
    '''
    Distributes the list of elements among multiple threads untill all the lists are sorted and combined into one.
    Intially each list gets divided into 4 parts and merge sort is carried out on individual lists.
    '''
    # Divide the list in 4 parts
    thread_divider = len(lst)//4
    lst1 = lst[:thread_divider]
    lst2 = lst[thread_divider:thread_divider*2]
    lst3 = lst[thread_divider*2:thread_divider*3]
    lst4 = lst[thread_divider*3:]

    # Create 4 threads for each list
    t1 = threading.Thread(target=mergeSort, args=[lst1])
    t2 = threading.Thread(target=mergeSort, args=[lst2])
    t3 = threading.Thread(target=mergeSort, args=[lst3])
    t4 = threading.Thread(target=mergeSort, args=[lst4])
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # Now combine the 4 individual lists into 2 lists
    lst5 = lst1 + lst2
    lst6 = lst3 + lst4

    # Create 2 threads for newly accuired lists
    t5 = threading.Thread(target=mergeSort, args=[lst5])
    t6 = threading.Thread(target=mergeSort, args=[lst6])
    t5.start()
    t6.start()
    t5.join()
    t6.join()

    # Combine the final 2 lists into one and again final sort it.
    lst7 = lst5 + lst6
    mergeSort(lst7)
    return lst7


def mergeSort(myList):
    '''Sorts the given list according to the merge sort algorithm'''
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

def get_data_from_user():
    '''Inputs data from user'''
    myList = []
    print("Enter the number of elements you want to enter: ",end="")
    no_elem = int(input())
    for i in range(no_elem):
        print("Enter Element [{}/{}]: ".format(i+1,no_elem),end="")
        myList.append(int(input()))
    return myList


if __name__ == '__main__':
    myList = get_data_from_user()
    print("Unsorted List: {}".format(myList))
    print("Sorted List:   {}".format(threads_distributor(myList)))
