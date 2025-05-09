# Str = "Automation"
# for ch in list(Str):
#     print(ch)




# str="Automation"
# v=0
# c=0
# for ch in list(str.lower()):
#     if ch in "aeiou":
#         v+=1
#     else:
#         c+=1


# print(c)
# print(v)

def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for ch in s:
        if ch.isalpha():  # Check if the character is a letter
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

# Example usage
my_str = "Automation"
count_vowels_and_consonants(my_str)

