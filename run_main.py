import all_function


def main():
    word_to_unscramble = input("Enter word to unscramble: ").upper()

    word_in_dic = []

    first_letter_align = []

    two_letter_words = []
    three_letter_words = []
    four_letter_words = []
    five_letter_words = []
    six_letter_words = []

    with open("wor.txt", "r") as file:
        word_file = file.readlines()

    all_function.put_word_in_list(word_file, word_in_dic)

    all_function.get_the_word(word_to_unscramble, first_letter_align, word_in_dic, two_letter_words, three_letter_words, four_letter_words, five_letter_words, six_letter_words)

    string_two_letter = str(two_letter_words).replace("[", "").replace("]", "")
    string_three_letter = str(three_letter_words).replace("[", "").replace("]", "")
    string_four_letter = str(four_letter_words).replace("[", "").replace("]", "")
    string_five_letter = str(five_letter_words).replace("[", "").replace("]", "")
    string_six_letter = str(six_letter_words).replace("[", "").replace("]", "")

    print(f"Two letter words include: {string_two_letter}")
    print(f"Three letter words include: {string_three_letter}")
    print(f"Four letter words include: {string_four_letter}")
    print(f"Five letter words include: {string_five_letter}")
    print(f"Six letter words include: {string_six_letter}")