#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    
    # dictionary to hold key value 
    tickets_dict = {}
    route = []
    
    for t in tickets:
        tickets_dict[t.source] = t.destination
        
    current_ticket = tickets_dict['NONE']
    
    while current_ticket != 'NONE':
        route.append(current_ticket)
        current_ticket = tickets_dict[current_ticket]
        
    route.append(current_ticket)

    return route
