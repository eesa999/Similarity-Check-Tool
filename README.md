# Similarity Check Tool

This project is a Python-based tool that utilizes the Ollama AI model to analyze geographical and semantic similarity between textual entries. It is designed to help determine whether two given texts refer to the same entity, name, or location, despite minor differences in wording.

---

## 📌 Features

- Uses **AI-powered text similarity analysis** to detect equivalent place names.
- Processes data from **Excel files**.
- **Filters** and **matches** similar entries.
- Exports results in an Excel file for easy review.

---

## 🚀 Prerequisites

Ensure you have the following installed:

1. **Python** (>=3.7 recommended)

2. Required Python libraries:

   ```sh
   pip install pandas ollama openpyxl
   ```

3. **Install Ollama** (if not already installed):

   - For macOS and Linux:
     ```sh
     curl -fsSL https://ollama.com/install.sh | sh
     ```
   - For Windows:
     - Download the installer from [Ollama's official website](https://ollama.com) and follow the installation instructions.

4. **Verify Ollama installation**:

   ```sh
   ollama --version
   ```

   If this command returns a version number, Ollama is installed correctly.

5. **Download the required model**:

   ```sh
   ollama run command-r7b-arabic
   ```

   This will download and prepare the model for use.

6. **Excel files** (`trusted_file.xlsx` & `similarity_file.xlsx`)

   - Ensure the files contain the columns **`ID`** and **`NAME`**

---

## 🛠️ Installation & Usage

1. Clone this repository:

   ```sh
   git https://github.com/eesa999/Similarity-Check-Tool.git
   cd similarity-check-tool
   ```

2. Place your input Excel files (`trusted_file.xlsx` & `similarity_file.xlsx`) in the same directory.

3. Run the script:

   ```sh
   python similarity_check.py
   ```

4. The processed results will be saved in:

   ```sh
   final_result.xlsx
   ```

---

## 🔹 How It Works

1. **Loads** two Excel files (`trusted_file.xlsx` and `similarity_file.xlsx`).
2. **Creates a cross join** between them to compare all possible pairs.
3. **Applies AI-based text similarity** using the `check_similarity` function.
4. **Filters** the results to keep only the rows where similarity was confirmed.
5. **Saves** the final matched data into `final_result.xlsx`.

---

## 🔹 Important Note

The `system_message` in the script has been updated to be more **generic**. Users must customize it to fit their **specific use case**, such as judicial institutions, geographical locations, or product names. Modify the `system_message` content in the script as needed to align with your domain-specific requirements.

