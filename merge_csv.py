import os
import glob
import pandas as pd

nmin = 1
TICKER ='SPY'

data_path = os.path.join('data', TICKER, TICKER +'_equidistant_log_returns')
os.chdir(data_path)

extension = 'csv'
csv_file_list = [i for i in glob.glob('*.{}'.format(extension))]
##################### not working, hitting memory limit(probably)
#combine all files in the list
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

###########################################

CHUNK_SIZE = 100000


output_file = os.path.join(os.path.pardir,TICKER+'_preprocessed_data.csv')

for csv_file_name in csv_file_list:
    chunk_container = pd.read_csv(csv_file_name, chunksize=CHUNK_SIZE)
    for chunk in chunk_container:
        chunk.to_csv(output_file, mode="a", index=False)
