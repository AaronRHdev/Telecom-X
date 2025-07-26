import pandas as pd 

def load_data(path = '', type_file = 'csv'):
    """This function allows load data from a specific path\n
    Key arguments:  
    path - this argument recieves the path of our data to read. (default: '')\n
    type of "path": String\n
    type_file - this argument recieves the type of file that wants read. (default: 'csv')\n
    type of "type_file": String """

    if type_file.lower() == 'csv':
        return pd.read_csv(path)
    elif type_file.lower() == 'json':
        return pd.read_json(path)
    elif type_file.lower() == 'excel':
        return pd.read_excel(path)
    elif type_file.lower() == 'html':
        return pd.read_html(path)
    else:
        print(f'The {type_file} type is not compatible with this function.')

load_data()
