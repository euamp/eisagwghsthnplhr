def digSum(n): 
  
    if (n == 0): 
        return 0
    if (n % 9 == 0): 
        return 9 
    else: 
        return (n % 9)


def some_number(number):
    twice_plus = number*3 + 1
    return digSum(twice_plus)

'''
Example

print(some_number(9999))

'''
