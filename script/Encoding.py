import csv
import os
def hex_to_int(hash_string):
    hex_pairs = [hash_string[i:i+2] for i in range(0, len(hash_string), 2)]
    decimal_values = [int(pair, 16) for pair in hex_pairs]
    return decimal_values

def encoding(input_file, output_file, csv_file, hash_string, window_size=2000, step_size=100, first_execution=True):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            if parts:
                last_part = parts[-1] 
                if '/' in last_part:
                    last_part=last_part.replace('/','')
                if last_part and last_part[0]=='0' and last_part!="0" and len(last_part)>1 and last_part[1]=='x':
                    last_part=last_part[2:]
                    matches=['x',':','/']
                    if not any(x in last_part for x in matches):
                        if(len(last_part)%2!=0):
                            last_part=last_part+"0"
                        outfile.write(last_part)

    with open(output_file, 'r') as infile:
            line = infile.readline()
    max_start = len(line)-window_size

    opening_mode = ""
    if first_execution == True:
         os.makedirs(os.path.dirname(csv_file), exist_ok=True)
         opening_mode = 'w'
    else:
         opening_mode = 'a'
         
    with open(csv_file, opening_mode, newline='') as outfile:
            writer = csv.writer(outfile)
            if first_execution:
                field = ["mining(1=M 0=nM)"]
                for col1 in range(1, int(len(hash_string)/2)+1):
                        field.append(f"hash{col1}")
                for col in range(1,int(window_size/2)+1):
                    field.append(f"hex{col}")
                writer.writerow(field)
            hash_decimal_values=hex_to_int(hash_string)
            for start in range(0, max_start, step_size):
                window_stream = line[start:start + window_size]
                if "non-miners" in input_file:
                    sample=[0]
                else:
                    sample=[1]
                window_decimal_values=hex_to_int(window_stream)
                for value in hash_decimal_values:
                    sample.append(value)
                for values in window_decimal_values:
                    sample.append(values)
                writer.writerow(sample)
                sample=[]

if __name__ == "__main__":
    output_file = 'tmp.txt'
    input_file = '../processed_data/prova_processed.out'
    csv_file = '../encoded_data.csv'
    hash_string = 'ba184c40c8974ce60e6ec39355edaeef334b61fb614929b62e0561d789146553'
    window_size=2000
    step_size=100
    encoding(input_file, output_file, csv_file, hash_string)