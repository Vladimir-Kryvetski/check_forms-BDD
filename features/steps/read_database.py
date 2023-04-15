def read_database(database):
    with open(database, 'r') as file:
        data = file.read()
    return data