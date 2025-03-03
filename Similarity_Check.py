import pandas as pd
import ollama

# ============================
# 🔹 CONFIGURATION & SETUP 🔹
# ============================

# Define the model name used for text similarity checking
MODEL_NAME = "command-r7b-arabic:latest"

# Define the system message for the AI model
# NOTE: Modify the system message to fit your specific use case
system_message = {
    "role": "system",
    "content": (
        "You are an assistant specializing in analyzing the similarity of texts based on the user's specific needs. "
        "Your goal is to determine whether the two given texts refer to the **same entity**, even if the wording is slightly different. "
        "Common variations in word order, synonyms, and abbreviations should be **considered equivalent** if the meaning remains unchanged. "
        "Only respond with 'Yes' if both texts represent the same concept, regardless of minor differences in phrasing. "
        "If the texts refer to different entities, respond with 'No'. "
        "Answer only with 'Yes' or 'No' without any further explanation. "
        "Modify this message according to your domain-specific requirements (e.g., judicial institutions, geographic locations, product names, etc.)."
    )
}

# ============================
# 🔹 SIMILARITY CHECK FUNCTION 🔹
# ============================

def check_similarity(text1, text2):
    """
    Checks the similarity between two texts using the Ollama AI model.
    Returns either 'Yes' if they are the same or 'No' if they are different.
    """
    user_message = {
        "role": "user",
        "content": f"First text: {text1}\nSecond text: {text2}"
    }

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[system_message, user_message]
        )

        # Extract the response content and clean up any extra whitespace
        similarity_result = response["message"]["content"].strip()

        # Print comparison details for debugging/logging
        print(f"Comparison:\n - {text1}\n - {text2}\n Result: {similarity_result}\n")

        return similarity_result
    except Exception as e:
        print(f"Error while calling the API: {e}")
        return "Error"

# ============================
# 🔹 DATA PROCESSING 🔹
# ============================

# Load the input Excel files (Ensure columns are named 'ID' and 'NAME')
trusted_file = pd.read_excel("trusted_file.xlsx")
similarity_file = pd.read_excel("similarity_file.xlsx")

# Create a cross join between the two datasets
trusted_file["key"] = 1
similarity_file["key"] = 1
cross_joined = trusted_file.merge(similarity_file, on="key").drop(columns=["key"])

# Remove duplicate entries (if any)
cross_joined = cross_joined.drop_duplicates()

# Apply the similarity check function to each row
df_filtered = cross_joined.copy()
df_filtered["Similarity_Result"] = df_filtered.apply(
    lambda row: check_similarity(row["NAME_x"], row["NAME_y"]), axis=1
)

# Keep only the rows where similarity was confirmed as "Yes"
df_filtered = df_filtered[df_filtered["Similarity_Result"] == "Yes"]

# Perform a left join to associate filtered results with the original trusted file
final_result = trusted_file.merge(df_filtered, left_on="ID", right_on="ID_x", how="left")

# Save the final result to an Excel file
final_result.to_excel("final_result.xlsx", index=False)

print("Processing complete. Filtered results saved to final_result.xlsx")
