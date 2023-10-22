import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the nominal credits dataset from the CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Restructure the dataset to include credit class distribution
def restructure_dataset(df, status_column):
    pivot_table = df.pivot_table(index=status_column, columns='Credit Status', aggfunc='size', fill_value=0)
    pivot_table.columns = ['Bad Credit', 'Good Credit']
    pivot_table['Total Credits'] = pivot_table['Bad Credit'] + pivot_table['Good Credit']
    return pivot_table.sort_values(by='Total Credits', ascending=False)

# Modified function to display percentage values on the bars
def plot_credit_distribution_percentage(df, title, xlabel, ax):
    sns.set_style("whitegrid")
    
    # Calculate percentages
    df_percentage = df[['Bad Credit', 'Good Credit']].div(df['Total Credits'], axis=0) * 100
    
    # Create bar plot
    df_percentage.plot(kind='bar', ax=ax, color=['#d9534f', '#5cb85c'], stacked=True)
    
    # Annotate bars with percentage values
    for i, (index, row) in enumerate(df_percentage.iterrows()):
        total_percentage = 0
        for j, value in enumerate(row):
            if value > 0:
                ax.text(i, total_percentage + value / 2, f'{value:.1f}%', ha='center', va='center', color='white', fontsize=10)
            total_percentage += value
    
    # Set plot properties
    ax.set_title(title, fontsize=15)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Percentage of Credits', fontsize=12)
    ax.legend(["Bad Credit", "Good Credit"], loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_ylim(0, 100)
    ax.set_xticklabels(df.index, rotation=45, ha='right')

# Main function to run the analysis
def main():
    file_path = './cleaned-nominal-credits.csv'
    df = load_data(file_path)
    
    # Combine "Marital Status" and "Gender" into a single category
    df['Marital Status & Gender'] = df['Marital Status'] + ' & ' + df['Gender']
    
    # Create subplots for standardized visual representations
    fig, axs = plt.subplots(2, 1, figsize=(12, 12))
    
    # Personal Status: Marital Status & Gender
    combined_personal_status_df = restructure_dataset(df, 'Marital Status & Gender')
    plot_credit_distribution_percentage(combined_personal_status_df, 'Credit Class Distribution by Marital Status & Gender', 'Marital Status & Gender', axs[0])
    
    # Job Status: Employment Term
    employment_term_df = restructure_dataset(df, 'Employment Term')
    plot_credit_distribution_percentage(employment_term_df, 'Credit Class Distribution by Employment Term', 'Employment Term', axs[1])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
