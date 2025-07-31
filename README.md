This repository contains the code and the presentation related to AICryptojacking trap project.
The project aims to developing a machine learning model to detect cryptojacking intrusions based on memory features.

- DataCleaning.py contains the program used to pre-process the memory read log files using regular expressions
- Encoding.py is the program used to encode the memory read log files into feasible values for the model. Every byte of memory read log files is encoded into an integer, this approach is combined with a sliding window algorithm.
- Normalization.py contains the program used to normalize the data inside the raw csv file.
- Training.py is where the neural network is created, trained and saved.
- Testing.py contains the program used to test the model on real world data.
The pdf file explains the work with a short presentation.
