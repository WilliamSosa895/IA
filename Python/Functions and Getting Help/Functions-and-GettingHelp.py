#1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)

pass
round_to_two_places(3.14159)

#2
print(round(123, -1))   # 120
print(round(123, -2))   # 100
print(round(9876, -3))  # 10000


#3
def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between a given number of friends.
    
    By default, assumes 3 friends.
    
    >>> to_smash(91)
    1
    >>> to_smash(91, 4)
    3
    """
    return total_candies % num_friends
to_smash(91)