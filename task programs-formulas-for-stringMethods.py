# Accessing characters in strings
# len(): length of string
# lower(): convert all the character of a string to lower case method
# upper(): convert all the character of a string to upper case method
# str(): convert non string value to string representation
# Replace some character in sting


# index starts from zero
first = "Pune"[0]
print(first)
new_str = "Access to the all users"
print(len(new_str))
print(new_str.upper())
print(new_str.lower())
print(new_str.replace('s', 'S'))
print(new_str + str(2))


# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = new_str[1:6]
step = new_str[1:6:2]
print(sub)
print(step)