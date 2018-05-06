import extractBetween2Strings, search_table

def return_all_values_in_column(input_file, deliminator, desired_column_name):
    values_in_column_array = []
    with open(input_file, "rt") as opentable:
        table = opentable.read()
        rows = table.splitlines()
        headers= rows[0]
        del rows[0]
        for lines in rows:
            cells = lines.split(deliminator)
            search_column = str(headers).split(deliminator).index(desired_column_name)
            values_in_column_array.append(cells[search_column])
    return values_in_column_array

def search_table_and_extract_from_txt_file(table, deliminator, desired_column_name, file_to_be_searched,
                                           new_sequence_character, name_of_output_file):
    with open(name_of_output_file, "w") as new_file_with_seqs:
        for search_term in search_table.return_all_values_in_column(table, deliminator, desired_column_name):
            extractBetween2Strings.extract_string_between_two_strings(file_to_be_searched, search_term,
                                                                      new_sequence_character)
            new_file_with_seqs.write(
                extractBetween2Strings.extract_string_between_two_strings(file_to_be_searched, search_term,
                                                                          new_sequence_character))
