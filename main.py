def main():
    file_path = "books/frankenstein.txt"
    print(f"--- Begin report of {file_path} ---")
    file_contents = read_file(file_path)
    num_words = count_words(file_contents)
    print(f"{num_words} words found in the document")
    print("\n")
    chars_dict = count_characters(file_contents)
    sorted_dictionary = sort_dict(chars_dict)

    for key in sorted_dictionary:
        print(f"The '{key}' character was found {sorted_dictionary[key]} times")

    print("--- End report ---")

def read_file(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    count_chars = {}

    for c in lowered_text:
        if (c>='a'and c<='z'):
            if c in count_chars:
                count_chars[c] += 1
            else:
                count_chars[c] = 1
    
    return count_chars


def sort_dict(chars_dict):
    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_chars_dict)
    

main()

