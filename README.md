This repository contains the code and the presentation related to AICryptojacking trap project.
The project aims to developing a machine learning model to detect cryptojacking intrusions based on memory features.

DataCleanining functions runs over all the files with .out extension in the data folder.
Encoding function requires the user to insert the correct hash string for the specific memory read log file.
Then Normalization function is executed over the CSV file generated.
Once the csv file is generated and normalised the user is asked if they want to train the model with that specific dataset.
Another possibility is to generate a csv file that can be used to test the model, this options follows the same path for the creation of the csv file but the repository from where the data is taken is the "testing_data" repository.


The main.py script needs to be run after inserting the data required in the data repository, after that the script can be executed and by following the inputs it is possible to train the model. 
A complete dataset with real data can be found at https://github.com/CryptojackingTrap/dataset.
