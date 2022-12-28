import threading

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

def merge_sort_with_threading(lst):
    # Create 4 threads
    threads = []
    chunk_size = len(lst) // 4
    for i in range(4):
        if i == 3:
            # For the last thread, we will include the remaining elements
            # to ensure that all elements are covered
            threads.append(threading.Thread(target=merge_sort, args=(lst[i * chunk_size:],)))
        else:
            threads.append(threading.Thread(target=merge_sort, args=(lst[i * chunk_size:(i + 1) * chunk_size],)))
    
    # Start the threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Merge the sorted chunks
    result = merge(threads[0], threads[1])
    result = merge(result, threads[2])
    result = merge(result, threads[3])
    return result


if __name__ == '__main__':
    lst = [5, 2, 7, 1, 3, 9, 8, 4, 6]
    sorted_lst = merge_sort_with_threading(lst)
    print(sorted_lst)  # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
