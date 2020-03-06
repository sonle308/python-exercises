# Letter Counter App
# Write a console programme that
# (1) Allows users to enter a string
# (2) Then allows users to enter a character or a string
# (3) Prints the number of occurrences of the character or string in (2) in the string in (1)

print('Input a string:')
string = input()
print('Input a character:')
character = input()
print('The number of occurrences of character (%s) is/are' % character, string.count(character))
