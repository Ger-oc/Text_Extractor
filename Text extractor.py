import re
import pandas as pd


def extract_metrics(log_file):
    with open(log_file, 'r', encoding='utf-8') as file:
        logs = file.read().split("\n\n")  # Splitting using double newlines

    data = []

    for block in logs:
        lines = block.strip().split("\n")  # Split each block into lines

        # Match epoch number
        epoch_match = re.search(r"Epoch (\d+)/\d+", block)
        precision_match = re.search(r"Precision:\s*([\d.]+)", block)
        recall_match = re.search(r"Recall:\s*([\d.]+)", block)
        f1_match = re.search(r"F1 Score:\s*([\d.]+)", block)

        if epoch_match and precision_match and recall_match and f1_match:
            epoch = int(epoch_match.group(1))
            precision = float(precision_match.group(1))
            recall = float(recall_match.group(1))
            f1_score = float(f1_match.group(1))

            print(f"Extracted: Epoch={epoch}, Precision={precision}, Recall={recall}, F1={f1_score}")  # Debugging print
            data.append([epoch, precision, recall, f1_score])

    df = pd.DataFrame(data, columns=['Epoch', 'Precision', 'Recall', 'F1 Score'])

    if df.empty:
        print("No valid data found. Check the log file format.")
    else:
        print("Data successfully extracted!")

    return df


# Run the function and display results
log_file = r'C:\.....\.......\.......\Epoch 140txt.txt' 
df = extract_metrics(log_file)

# Save to CSV and print
df.to_csv("training_metrics.csv", index=False)
print("Extracted data saved to training_metrics.csv")
print(df)


log_file = 'C:\\Users\\.....\\.....\\Epoch 140txt.txt'

df = extract_metrics(log_file)

# Display the extracted data
print(df)
