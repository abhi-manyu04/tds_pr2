# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "chardet>=5.2.0",
#     "matplotlib>=3.10.0",
#     "numpy>=2.2.0",
#     "pandas>=2.2.3",
#     "python-dotenv>=1.0.1",
#     "requests>=2.32.3",
#     "seaborn>=0.13.2",
# ]
# ///

import os 
import sys
import chardet
import pandas as pd
import numpy as np 
import requests
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

load_dotenv()

def encoding(file_path: str) -> str:#+
    """
    Determine the encoding of a given CSV file using the chardet library.
    """
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def savefig(plot, filename):
    """
    Save a Matplotlib figure to a file.
    """
    plot_filename = os.path.join(directory_name, filename)
    plot.tight_layout()
    plot.savefig(plot_filename, format='png')
    plot.clf()

def req_llm(prompt):
    TOKEN = os.getenv("AIPROXY_TOKEN")
    URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    model = "gpt-4o-mini"
    headers = {
        "Content-Type": "application/json",
        "Authorization":f'Bearer {TOKEN}'
    }
    data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }

    response = requests.post(URL, headers=headers, json=data)
    response_json = response.json()
    print("LLM Response code: ", response.status_code)
    if response.status_code == 200:
        return response_json
    else:
        exit(1)

def detect_outliers(df):
    outliers = {}
    for column in df.columns:  # Only consider numeric columns and use iqr on them
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers[column] = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        outlier_raw_text = outlier_raw(outliers)
    return outlier_raw_text, plot_outliers(df, outliers)

def outlier_raw(outliers):
    text = ""
    for column in outliers.keys():
        if len(outliers[column]) > 0:
            text += f'{column} has {len(outliers[column])} outliers. '
    return text

def plot_outliers(df, outliers):
    num_columns = len(df.columns)
    num_rows = (num_columns // 4) + 1 
    
    fig, axes = plt.subplots(num_rows, 4, figsize=(16, 4 * num_rows))
    axes = axes.flatten()
    
    for idx, column in enumerate(df.select_dtypes(include=[np.number]).columns):
        sns.boxplot(x=df[column], ax=axes[idx])
        axes[idx].set_title(f'Outliers in {column}')
        if not outliers[column].empty:
            axes[idx].scatter(outliers[column][column], np.ones(len(outliers[column])), color='red', label='Outliers')
            axes[idx].legend()
    
    # Remove any unused axes
    for i in range(idx + 1, len(axes)):
        fig.delaxes(axes[i])
    
    savefig(plt, "outlier.png")

def plot_correlation_heatmap(df):
    correlation_matrix = df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    savefig(plt, "correlation_heatmap.png")

def plot_quick_histogram(df):
    num_columns = len(df.columns)
    num_rows = (num_columns // 4) + 1 
    
    fig, axes = plt.subplots(num_rows, 4, figsize=(16, 4 * num_rows))
    axes = axes.flatten()

    for i, column in enumerate(df.columns):
        sns.histplot(df[column], bins=15, kde=True, color="salmon", ax=axes[i])
        axes[i].set_title(f'Histogram of {column}')

    for i in range(num_columns, len(axes)):
        axes[i].axis('off')
    savefig(plt, 'histogram.png')


def static_plot(numeric_columns):
    
    outlier_text = detect_outliers(numeric_columns)
    cor = plot_correlation_heatmap(numeric_columns)
    plot_quick_histogram(numeric_columns)

    return outlier_text, cor

def column_summary(df):
    # Initialize a dictionary to store results
    summary = {
        'Column': [],
        'Data Type': [],
        'Unique Values': [],
        'Missing Values': [],
        'Value Counts': []
    }

    # Loop through each column in the DataFrame
    for column in df.columns:
        summary['Column'].append(column)
        summary['Data Type'].append(df[column].dtype)
        summary['Unique Values'].append(df[column].nunique())  # Count of unique values
        summary['Missing Values'].append(df[column].isnull().sum())  # Count of missing values
        summary['Value Counts'].append(df[column].value_counts(dropna=False))  # Value counts, including NaN
        
    # Create a summary DataFrame from the dictionary
    summary_df = pd.DataFrame(summary)
    
    return summary_df

def write_to_readme(content):
    try:
        markdown_content = content['choices'][0]['message']['content']
        readme_path = os.path.join(directory_name, 'README.md')
        # Add image to README.md
        markdown_content = markdown_content.replace("```markdown","")
        markdown_content = markdown_content.replace("```", "")
        file_path = os.path.join(directory_name, "histogram.png")
        with open(file_path, "rb") as image_file:
          encoded_string = base64.b64encode(image_file.read()).decode()
          markdown_content = markdown_content.replace("histogram.png", f"data:image/png;base64,{encoded_string}")
        file_path = os.path.join(directory_name, "outlier.png")
        with open(file_path, "rb") as image_file:
          encoded_string = base64.b64encode(image_file.read()).decode()
          markdown_content = markdown_content.replace("outlier.png", f"data:image/png;base64,{encoded_string}")
        file_path = os.path.join(directory_name, "correlation_heatmap.png")
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            markdown_content = markdown_content.replace("correlation_heatmap.png", f"data:image/png;base64,{encoded_string}")

        with open(readme_path, 'w') as f:
            f.write(markdown_content)
    except Exception as e:
        print(f"An error occurred: {e}")



def main(file_path):

    df = pd.read_csv(file_path, encoding=encoding(file_path))

    numeric_columns = df.select_dtypes(include=[np.number])
    outlier_text, cor = static_plot(numeric_columns)

    summary = df.describe(include='all')
    missing_values = df.isnull().sum()


    prompt = f"""
    Genrate a README.md file with heading {file_name}.
    1st sub-header should be about the dataset, {df.columns}, describing the columns and recommending some analysis that would be good on the data.
    2nd sub-header should be the number of samples, features. use {df.info()}, {summary}, {missing_values}
    3rd sub header should be the about each column, use this {column_summary(df)}, dont write too much detail. 
    4th sub-header should be 'Key Insights and Next Steps'.
    here are some more information about the dataset use them libraly and make the readme file stand out {outlier_text}, {cor}, only use these if you see anything intresting.
    make the file extra intresting and exciting. Do not break the markdown format.
    """
    response = req_llm(prompt)

    write_to_readme(response)



    
file_path = sys.argv[1]
file_name = os.path.basename(file_path)
directory_name = os.path.splitext(file_name)[0]

if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
else:
    print(f"Directory '{directory_name}' already exists.")



main(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide csv file name.")
        sys.exit(1)