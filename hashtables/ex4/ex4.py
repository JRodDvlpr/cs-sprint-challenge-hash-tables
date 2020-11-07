def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # hash table
    hash_tbl = {}
    # array for result
    result = []
 
    for num in a:
        hash_tbl[num] = num
        if num != 0 and -num in hash_tbl:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
