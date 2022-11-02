in_text = "banana"

vowels = ["a", "i", "u", "e", "o"]

my_dict = {}
checked_words = {}




def minion_game(in_text):
    start_index = None
    # start_index_cons = None
    for index in range(len(in_text)):
        if in_text[index] in vowels:
            start_index = index

            break

        elif  in_text[index] not in vowels:
            start_index = index

            break
    vowel_in_text = in_text[start_index: len(in_text) + 1]
    cons_in_text = in_text[start_index: len(in_text) + 1]
    return cons_in_text

print(minion_game(in_text))