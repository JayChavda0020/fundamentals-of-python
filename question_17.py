''' Write a Python program to get a single string from two given strings, separated by a space
and swap the first two characters of each string.'''

a = input("Enter a string A : ")
b = input("Enter a string B : ")

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

print(new_a + " " + new_b)

