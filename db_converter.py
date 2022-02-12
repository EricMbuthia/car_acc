'''
Convert .csv file to relevant .sql & add it to a .db
Each .csv would be considered as a single table in the .db to be updated.
'''

import sqlite3
import pandas as pd

#A00 Adding Primary & Secondary Keys