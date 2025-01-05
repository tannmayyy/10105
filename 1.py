import pandas as pd
from tabulate import tabulate

# Load the CSV files into DataFrames
table1 = pd.read_csv('table1.csv')
table2 = pd.read_csv('table2.csv')
table3 = pd.read_csv('table3.csv')

# Prepare a list to hold the results
result = []

# Iterate over each entry in table2
for _, t2 in table2.iterrows():
    usi_id = t2['USI_ID']
    insight_number = t2['Insight_Numbers']

    # Get the corresponding entry from table1
    t1_entry = table1[table1['Insight_Numbers'] == insight_number]

    # Initialize the result row with None for all columns in table3
    result_row = {col: None for col in table3.columns}
    result_row['USI_ID'] = usi_id
    result_row['Insight_Numbers'] = insight_number

    if not t1_entry.empty:
        uni_combination = t1_entry['Uni_Combination'].values[0]
        columns_to_match = [col.strip() for col in uni_combination.split('+')]

        # Check if the columns exist in table3
        if all(col in table3.columns for col in columns_to_match):
            # Iterate over rows in table3 to find matches
            for _, t3_row in table3.iterrows():
                # Build the merged value based on Uni_Combination
                merged_value = ''.join(str(t3_row[col]) for col in columns_to_match)

                # Compare the merged value with USI_ID
                if merged_value == usi_id:
                    # Fill in the result row with data from table3
                    for col in table3.columns:
                        result_row[col] = t3_row[col]
                    break  # Stop after the first match

    # Append the result row to the results list
    result.append(result_row)

# Convert the result list to a DataFrame
result_df = pd.DataFrame(result)

# Print the result in a pretty format
print(tabulate(result_df, headers='keys', tablefmt='pretty', showindex=False))
