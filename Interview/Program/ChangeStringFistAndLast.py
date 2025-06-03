def change_first_and_last(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > 1:
            new_word = word[-1] + word[1:-1] + word[0]
        else:
            new_word = word
        result.append(new_word)
    return ' '.join(result)

input_str = "Good Morning Shyamjeet"
output_str = change_first_and_last(input_str)
print(output_str)