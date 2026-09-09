import math
from datetime import datetime

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def clean(in_series):
    # Days with no reading arrive from read_csv as None.
    # Build a new list holding only the real readings.
    result = []
    for value in in_series:
        if value is not None:
            result.append(value)
    return result

def mean(in_series):
    #takes input and returns mean
    in_series = clean(in_series)
    return sum(in_series) / len(in_series)

def variance(in_series):
    in_series = clean(in_series)
    m = mean(in_series)
    variance = sum((x - m) ** 2 for x in in_series) / len(in_series)
    return variance

def standard_deviation(in_series):
    v = variance(in_series)
    return math.sqrt(v)

def data_range(in_series):
    # Feature 4: the largest value minus the smallest value.
    # Called data_range so it does not hide Python's built-in range().
    series = clean(in_series)
    if len(series) == 0:
        return None
    return max(series) - min(series)

def median(in_series):
    # The middle value once the series is sorted.
    # With an even number of values, take the average of the middle two.
    series = clean(in_series)
    if len(series) == 0:
        return None
    series.sort()
    middle = int(len(series) / 2)
    if len(series) % 2 == 1:
        return series[middle]
    return (series[middle - 1] + series[middle]) / 2

def interquartile_range(in_series):
    # Feature 5: IQR = Q3 - Q1, the range of the middle 50% of the values.
    # Q1 is the median of the lower half, Q3 is the median of the upper half.
    series = clean(in_series)
    if len(series) < 4:
        return None
    series.sort()
    half = int(len(series) / 2)
    lower_half = series[:half]
    upper_half = series[len(series) - half:]
    return median(upper_half) - median(lower_half)

def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(1,len(lines[0])):
        conversion = datetime.fromisoformat if (lines[0][i]=='Date') else float
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
    print(f"Variance: {variance(data_table[choice])}")
    print(f'Standard Deviation: {standard_deviation(data_table[choice])}')
    print(f'Range: {data_range(data_table[choice])}')
    print(f'Interquartile range: {interquartile_range(data_table[choice])}')
    

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)