import pandas
from reviewer import Reviewer

with open('reviewer_info.csv') as csv_file:
    csv_reader = csv_reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:            