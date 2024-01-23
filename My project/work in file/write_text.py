import csv
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

rows = [('AA', '39.48', '23/01/2024', '9:36am', '-0.18', '181800'),
        ('AIG', '71.38', '23/01/2024', '9:36am', '-0,15', '195500'),
        ('AXP', '62.58', '23/01/2024', '9:36am', '-0.46', '935000')]

with open(r"My project\work in file\stocks.csv", "w") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)