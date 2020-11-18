def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    # dictionary holds key value
    array_dict = {}
    # We will loop through every list inside the array
    for i in arrays:
        # Loops through every item in each of the list
        for k in i:
            # If k is in the dictionary we will increase the key value
            if k in array_dict:
                array_dict[k] += 1
            else:
                array_dict[k] = 1  
    
        # ran the test between 6-7 seconds. Research more
        for key in array_dict.keys():
            if array_dict[key] == len(arrays):
                result.append(key)
        
        # this method took longer to run the tests in 8 seconds
        # result = [i[0] for i in array_dict.items() if i[1] == len(arrays)] 
    

    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
