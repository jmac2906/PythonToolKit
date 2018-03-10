def searchtable_and_extractfrom_txtfile(table, deliminator, desired_column_name, file_to_be_searched, new_sequence_character, name_of_output_file):
    import extractBetween2Strings,search_table
    with open(name_of_output_file, "w") as new_file_with_seqs:
        for search_term in search_table.returnAllValuesInColumn(table, deliminator, desired_column_name):
            extractBetween2Strings.extract_string_between_two_strings(file_to_be_searched, search_term,
                                                                      new_sequence_character)
            new_file_with_seqs.write(
                extractBetween2Strings.extract_string_between_two_strings(file_to_be_searched, search_term,
                                                                          new_sequence_character))


searchtable_and_extractfrom_txtfile()