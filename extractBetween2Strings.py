def extract_string_between_two_strings(file_to_be_searched,
                                       input_sequence,
                                       new_sequence_character):
    with open(file_to_be_searched) as text_file_name:
        text_file = text_file_name.read()
        return (text_file[
                text_file.index(input_sequence):text_file.find(new_sequence_character,
                                                               text_file.index(input_sequence))])
