"""
DataCleanining functions runs over all the files with .out extension in the data folder.
Encoding function requires the user to insert the correct hash string for the specific memory read log file.
Then Normalization function is executed over the CSV file generated.
Once the csv file is generated and normalised the user is asked if they want to train the model with that specific dataset.
Another possibility is to generate a csv file that can be used to test the model, this options follows the same path for the creation of the csv file but the repository from where the data is taken is the "testing_data" repository.
"""
import DataCleaning
import Encoding
import Normalization
import Training
import Testing
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

data_choice = input("Do you want to do testing? (y/n): ")

if data_choice == "y":
    input_dir = os.path.join(base_dir, "../testing_data")
else:
    input_dir = os.path.join(base_dir, "../data")

#DataCleaning
output_dir = os.path.join(base_dir, "../processed_data")

os.makedirs(output_dir, exist_ok=True)


for filename in os.listdir(input_dir):
    if filename.endswith(".out"):
        input_path = os.path.join(input_dir, filename)
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}_processed.out"
        output_path = os.path.join(output_dir, output_filename)

        print(f"Processing {filename} -> {output_filename}")
        DataCleaning.process_file(input_path, output_path)

#Encoding
input_dir = os.path.join(base_dir, "../processed_data")
output_dir = os.path.join(base_dir,"../csv")
output_filename = "encoded_data.csv"
output_path = os.path.join(output_dir, output_filename)
tmp_dir = os.path.join(base_dir,"../")
tmp_filename = "tmp.txt"
tmp_path = os.path.join(tmp_dir, tmp_filename)
first_execution = True
for filename in os.listdir(input_dir):
    if data_choice == "n":
        if filename.endswith(".out") and "testing" not in filename:
            input_path = os.path.join(input_dir, filename)
            hash_string = input(f"Insert the hash string for the {filename}: ")
            Encoding.encoding(input_path, tmp_path, output_path, hash_string, first_execution=first_execution)
            first_execution = False
            os.remove(tmp_path)
    else:
        if filename.endswith(".out") and "testing" in filename:
            input_path = os.path.join(input_dir, filename)
            hash_string = input(f"Insert the hash string for the {filename}: ")
            Encoding.encoding(input_path, tmp_path, output_path, hash_string, first_execution=first_execution)
            first_execution = False
            os.remove(tmp_path)
print(f"csv file created in {output_path}")

#Normalization
count = 1
input_path = output_path
output_dir = os.path.join(base_dir,"../csv")
output_filename = "normalized_data.csv"
output_path = os.path.join(output_dir, output_filename)
if data_choice == "y":
    output_filename = "normalized_data_testing.csv"
    output_path = os.path.join(output_dir, output_filename)
while os.path.isfile(output_path):
    if data_choice == "y":
        output_filename= f"normalized_data_testing_{count}.csv"
    else:
        output_filename= f"normalized_data_{count}.csv"
    count += 1
    output_path = os.path.join(output_dir, output_filename)
Normalization.normalization(input_path, output_path)

training_choice = "n"
if data_choice == "n":
    training_choice = input(f"Do you want to start the training of the model? (y/n): ")

#Training
input_path = output_path
output_dir = os.path.join(base_dir,"../models")
output_filename = "AICryptojackingTrapModel.keras"
output_path = os.path.join(output_dir, output_filename)
if training_choice == "y":
    Training.training(input_path, output_path)


#Testing
if data_choice == "y":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(base_dir,"../models")
    model_filename = "AICryptojackingTrapModel.keras"
    model_path = os.path.join(model_dir, model_filename)

    testing_dir = os.path.join(base_dir,"../csv")
    testing_filename = "normalized_data_testing.csv"
    testing_path = os.path.join(testing_dir, testing_filename)
    print(f"Testing over {testing_filename} (remember to set the specific testing file if there are multiple in the directory)")
    Testing.testing(model_path, testing_path)

