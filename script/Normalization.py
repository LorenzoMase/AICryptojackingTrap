import numpy as np
import csv
import pandas as pd
from sklearn import preprocessing


def normalization(csv_file, standardized_csv_file, hash_len_byte=32, window_size_byte=1000):
    data = pd.read_csv(csv_file, low_memory=False)
    data = np.asarray(data).astype('float64')

    scaler = preprocessing.StandardScaler().fit(data)
    standardized_data = scaler.transform(data)

    with open(standardized_csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        field = ["mining(1=M 0=nM)"]
        for n in range(1, hash_len_byte+1):
            field.append(f"hash{n}")
        for m in range(1, window_size_byte+1):
            field.append(f"hex{m}")
        writer.writerow(field)    
        writer.writerows(standardized_data)

if __name__ == "__main__":
    csv_file='Path_Of_CSV'
    hash_len_byte=32
    window_size_byte=1000
    standardized_csv_file='Path_Of_new_CSV'
    normalization(csv_file, standardized_csv_file)