def fair_sharer(values, num_iterations, share=0.1):
    """
    In each iteration the highest value in values gives a fraction (share) to both the left and right neighbor. 
    The leftmost field is considered the neightbor of the rightmost field.

    Args:
        values (list/array): 1D array of values (list or numpy array)
        num_iterations (int): Integer to set the number of iterations
        share (float): Fraction to be shared with each neighbor

    Returns:
        values (list/array): Values after all iterations of redistribution

    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    """
    for _ in range(num_iterations):
        highest_value_index = values.index(max(values))
        # modulo to treat array as circular
        left_index = (highest_value_index - 1) % len(values)
        right_index = (highest_value_index + 1) % len(values)
        
        amount_to_share = values[highest_value_index] * share
        
        # increase neighbors by spec. fraction
        values[left_index] += amount_to_share
        values[right_index] += amount_to_share
        
        # reduce highest value by total amount shared
        values[highest_value_index] -= 2 * amount_to_share

    return values
