import os, string
os.chdir("C:\\Users\\james\\Desktop\\febessentials\\hmmsearch")

def returnAllValuesInColumn(input_file,deliminator,desired_column_name):
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

csv = "UJBLAST.csv"
deliminator = ","
desired_column_name= "Sequence"
