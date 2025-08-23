#1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. 
    A lucky list contains at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    # Si terminamos el for y no encontramos ningún número divisible por 7
    return False
        
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. 
    A lucky list contains at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    # Si ningún número es divisible por 7
    return False

    
#2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [x > thresh for x in L]
pass

#3
def menu_is_boring(meals):
    """Return True if the same meal has ever been served two days in a row."""
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False
pass

#4
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run."""
    total_profit = 0
    for _ in range(n_runs):
        payout = play_slot_machine()  # Ganancia de esta tirada
        net_profit = payout - 1       # Restamos el costo de la jugada
        total_profit += net_profit
    return total_profit / n_runs
    pass
print(estimate_average_slot_payout(100000000))