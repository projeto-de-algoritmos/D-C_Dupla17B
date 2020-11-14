def countInversions(array):
    if len(array) == 1:
        return array, 0
    else:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        left, left_inversions = countInversions(left)
        right, right_inversions = countInversions(right)
        sorted_array = []
        i = 0
        j = 0
        inversions = 0 + left_inversions + right_inversions
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            inversions += (len(left)-i)
    sorted_array += left[i:]
    sorted_array += right[j:]
    return sorted_array, inversions