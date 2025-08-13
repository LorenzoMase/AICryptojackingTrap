# AICryptojacking Trap Project

This repository contains the code and presentation for the **AICryptojacking Trap** project.  
The goal of the project is to develop a **machine learning model** to detect cryptojacking intrusions based on **memory features**.

---

## 📂 Project Structure

### 1. **Data Cleaning**
- The `DataCleaning` function processes all files with the `.out` extension located in the `data` folder.

### 2. **Encoding**
- The encoding function requires the user to enter the correct **hash string** for the specific memory read log file.

### 3. **Normalization**
- Once the `.csv` file is generated, the `Normalization` function is applied to it.

---

## ⚙️ Workflow

1. **CSV Generation**  
   - After cleaning and encoding, the `.csv` file is created and normalized.

2. **User Choice**
   - The user can choose to:
     - **Train the model** with the generated dataset.
     - **Create a test CSV** to evaluate the model.

3. **Testing Option**
   - When generating a test dataset, the process is identical, except the data is taken from the `testing_data` directory.

---

## ▶️ How to Run the Project

1. Place your data files in the `data` directory.
2. Run the `main.py` script.
3. Follow the prompts to:
   - Train the model, or
   - Generate a test CSV.
   
---

## 📊 Dataset
A complete dataset with real data is available here:  
[https://github.com/CryptojackingTrap/dataset](https://github.com/CryptojackingTrap/dataset)
