# current_instance: the current state
# neighbor_fn: the neighborhood function which creates a list of instances
# obj_fn: the objective function which rates each state
# it: number of iterations

def local_search(start_instance, neighbor_fn, obj_fn, it):
    current_instance = start_instance
    history = [current_instance]
    for i in range(0, it):
        neighbors = neighbor_fn(current_instance)
        minimum_val = obj_fn(current_instance)
        minimum_neighbor = current_instance
        for n in neighbors:
            if obj_fn(n) < minimum_val:
                minimum_neighbor = n
                minimum_val = obj_fn(n)
        if current_instance == minimum_neighbor:
            print("Iteration until minimum: " + str(i))
            break
        else:
            current_instance = minimum_neighbor
            history.append(current_instance)
    return current_instance, history



