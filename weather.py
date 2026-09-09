import math
from datetime import datetime

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def is_nonnull(x):
    return x is not None

def mean(in_series):
    in_series = list(filter(is_nonnull, in_series))
    return sum(in_series) / len(in_series)

def variance(in_series):
    '''
    function takes in_series list and returns variance list
    

    Parameters
    ----------
    in_series : list

    Returns
    -------
    variance : list

    '''
    
    variance = [
        ((in_series[x] - mean.(in_series[x])) ** 2)
        for x in in_series
        ]
    
    return variance


def standard_deviation(variance):
    return math.sqrt(variance)

def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        conversion = datetime.fromisoformat if (lines[0][i] == 'Date') else float
        data_table[lines[0][i]] = \
            [default_value if (len(line[i]) == 0) else conversion(line[i]) for line in lines[1:]]
    return data_table

def get_user_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == 'exit':
        return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        print("Invalid choice. Please try again.")
        return get_user_choice(options)
    choice = int(choice) - 1
    return options[choice]

def menu(data_table):
    print("Select a data series:")
    choice = get_user_choice(series_titles)
    series = data_table[choice]
    print(f"Mean: {mean(data_table[choice])}")

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)