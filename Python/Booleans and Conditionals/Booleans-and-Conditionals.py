#1
# Your code goes here. Define a function called 'sign'
def sign(n):
    if(n>0):
        return 1
    elif(n<0):
        return -1
    else:return 0
    
sign(0)

#2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3
to_smash(91)

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if(total_candies>1):
        print("Splitting", total_candies, "candies")
        return total_candies % 3
    else:
        print("Splitting", total_candies, "candy")
        return total_candies % 3
to_smash(91)
to_smash(1)

#3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    """
    Return True if we're prepared for the weather according to the rules:
    - I'm safe if I have an umbrella
    - Or if the rain isn't too heavy (<5) and I have a hood
    - Otherwise, I'm fine unless it's raining (>0) and it's a workday
    """
    # Corregimos la precedencia usando paréntesis
    return have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)

# Este es el caso que falla en la función original
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Verificamos el resultado
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)  # Debe imprimir True, porque no llueve y no es día laboral

#4
def concise_is_negative(number):
    return number < 0


#5a
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
pass

#5b
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion
pass

#5c
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (not ketchup and mustard)

pass

#6
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return int(ketchup) + int(mustard) + int(onion) == 1
pass

#return (int(ketchup) + int(mustard) + int(onion)) == 1
#return (ketchup + mustard + onion) == 1
