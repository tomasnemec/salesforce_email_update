#!/usr/bin/python

import os
import glob
import pandas as pd
os.chdir("./csvtomerge")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

print('Based on number of csv files to merge it can take up to few minutes to finish, please be patient :) ')

print(pd.read_csv('combined_csv.csv'))