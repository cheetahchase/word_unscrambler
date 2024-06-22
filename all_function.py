def put_word_in_list(list_to_get: list, list_to_append: list):
    for word in list_to_get:
        list_to_append.append(word.replace("\n", ""))


def get_the_word(word_to_unscramble: str, first_letter_align: list, word_in_dic: list, two_letter: list, three_letter: list, four_letter: list, five_letter: list, six_letter: list):
    for word in word_in_dic:
        if len(word) > len(word_to_unscramble):
            pass
        else:
            if word[0] in word_to_unscramble:
                first_letter_align.append(word)
                for word_that_first_letter_align in first_letter_align:
                    pass
                if len(word_that_first_letter_align) == 2 and (word_that_first_letter_align[1] in word_to_unscramble):
                    two_letter.append(word_that_first_letter_align)

                else:
                    if len(word_that_first_letter_align) == 3 and (word_that_first_letter_align[1] in word_to_unscramble) and (word_that_first_letter_align[2] in word_to_unscramble):
                        three_letter.append(word_that_first_letter_align)
                    else:
                        if (len(word_that_first_letter_align) == 4) and (
                                word_that_first_letter_align[1] in word_to_unscramble) and (
                                word_that_first_letter_align[2] in word_to_unscramble) and (
                                word_that_first_letter_align[3] in word_to_unscramble):
                            four_letter.append(word_that_first_letter_align)
                        else:
                            if len(word_that_first_letter_align) == 5 and (
                                    word_that_first_letter_align[1] in word_to_unscramble) and (
                                    word_that_first_letter_align[2] in word_to_unscramble) and (
                                    word_that_first_letter_align[3] in word_to_unscramble) and (
                                    word_that_first_letter_align[4] in word_to_unscramble):
                                five_letter.append(word_that_first_letter_align)
                            else:
                                if len(word_that_first_letter_align) == 6 and (
                                        word_that_first_letter_align[1] in word_to_unscramble) and (
                                        word_that_first_letter_align[2] in word_to_unscramble) and (
                                        word_that_first_letter_align[3] in word_to_unscramble) and (
                                        word_that_first_letter_align[4] in word_to_unscramble) and (
                                        word_that_first_letter_align[5] in word_to_unscramble):
                                    six_letter.append(word_that_first_letter_align)
