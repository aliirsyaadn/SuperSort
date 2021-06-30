def merge (M,N):
    merged_list = []

    m, n = len(M), len(N)
    i, j = 0, 0

    while (i + j < m + n):
        if i == m:
            merged_list.append(N[j])
            j += 1
        elif j == n:
            merged_list.append(M[i])
            i += 1
        elif M[i] <= N[j]:
            merged_list.append(M[i])
            i += 1
        elif M[i] > N[j]:
            merged_list.append(N[j])
            j += 1

    return merged_list

def selection(L, left, right):
    forward_sorted = []
    backward_sorted = []

    # Forward Selection
    current_highest = L.pop(left)
    forward_sorted.append(current_highest)
    right -= 1

    pointer = left
    while (pointer < right):
        if L[pointer] >= current_highest:
            current_highest = L.pop(pointer)
            forward_sorted.append(current_highest)
            right -= 1
        pointer += 1
    
    # Backward Selection
    if right > 1:
        current_highest = L.pop(right-1)
        backward_sorted.append(current_highest)
        right -= 1
        pointer = right-1
        while (pointer >= left):
            if L[pointer] >= current_highest:
                current_highest = L.pop(pointer)
                backward_sorted.append(current_highest)
                right -= 1
            pointer -= 1

    return L, merge(forward_sorted, backward_sorted)

def supersort(L):
    l = len(L)
    if l <= 1:
        return L

    # Partition
    middle = l // 2
    unsorted_left, parent_sorted_left = selection(L[0:middle], 0, middle)
    child_sorted_left = supersort(unsorted_left)
    sorted_left = merge(parent_sorted_left, child_sorted_left)
    
    unsorted_right, parent_sorted_right = selection(L[middle:l], 0, l-middle)
    child_sorted_right = supersort(unsorted_right)
    sorted_right = merge(parent_sorted_right, child_sorted_right)
    
    return merge(sorted_left, sorted_right)

L = [2,7,4,19,45,16,9,13,8,69,55,11,23,98,14,5,1,3]	
print(f"Unsorted list {L}")

result = supersort(L)
print(f"Sorted list   {result}")