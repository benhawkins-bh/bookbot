def main():
    user_chosen_book = input("Enter book name:")
    book_filepath = f"books/{user_chosen_book}.txt"
    text_output = get_book_text(book_filepath)
    word_count = get_word_count(text_output)
    character_count_dict = get_character_count(text_output)
    character_count_list = convert_dict_into_sorted_list(character_count_dict)
    character_count_report(book_filepath, word_count, character_count_list)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    lowered_text = text.lower()
    final_dict = {}
    
    for letter in lowered_text:
        if letter in final_dict:
            final_dict[letter] += 1
        else:
            final_dict[letter] = 1
    return final_dict

def sort_on(dict):
    return dict["num"]

def convert_dict_into_sorted_list(dict):
    # Creates a list from the dict with the format {"letter":item, "num":number}
    # Only takes in alphabetical letters
    final_list = []
    for item in dict:
        formatted_dict = {}
        if item.isalpha():
            formatted_dict["letter"] = item
            formatted_dict["num"] = dict[item]
            final_list.append(formatted_dict)
    final_list.sort(reverse=True, key=sort_on)
    return final_list

def character_count_report(filepath, number_of_words, character_list):
    print(f"--- Begin report of {filepath} ---")
    print(f"{number_of_words} words found in the document\n")
    for character in character_list:
        print(f"The '{character["letter"]}' character was found {character["num"]} times")

main()