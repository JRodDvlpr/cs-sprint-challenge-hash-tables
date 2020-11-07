def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Sorting to Dictionaries
    # Storing each weight as a key, value will be that weights index
    
    w_dict = {}
    
    # Your code here
    
    # enumerate allows us to switch values 
    # swithcing the values and storing them in w_dict
    for i, k in enumerate(weights):
        # check to see if limit - weight is in w_dict
        if k in w_dict:
            w_dict[k].append(i)
        else:
            w_dict[k] = [i]

    for i, k in enumerate(w_dict):
        if limit-k in w_dict:
            if w_dict[limit-k] is w_dict[k]:
                if len(w_dict[k]) >= 2:
                    return (w_dict[limit-k][1], w_dict[k][0])
            else:
                return (w_dict[limit-k][0], w_dict[k][0])

    return None
