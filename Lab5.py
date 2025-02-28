# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 2:
        return "*" * n 
    
    square = []

    square.append("*" * n)
    
    for _ in range(n - 2):
        square.append("*" + " " * (n - 2) + "*")
    
    square.append("*" * n)
    
    return "\n".join(square)

# 1
# 12
# 123
# 1234
def number_pattern(n):
   lines = []

   for i in range (1, n + 1):
      line = ''.join(str(x) for x in range(1, i + 1 )) 
      lines.append(line)

   return '\n'.join(lines)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return n * (n + 1)/2

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    lines = []  
  
    for i in range(1, n + 1):
        spaces = " " * (n - i)        
        stars = "*" * (2 * i - 1)   
        lines.append(spaces + stars)       
    
    return "\n".join(lines)