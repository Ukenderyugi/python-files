def remove_vowels(string):
    vowels = "aeiouAEIOU"
    without_vowels = ""

    for char in string:
        if char not in vowels:
            without_vowels += char

    return without_vowels
my_string = "Hello, World!"
result = remove_vowels(my_string)
print(result) # Output: Hll, Wrld!