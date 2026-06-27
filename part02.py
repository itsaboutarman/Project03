import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the file dynamically (supports both real .xlsx and renamed .csv)
file_path = 'data.xlsx'
try:
    df = pd.read_excel(file_path)
except Exception:
    df = pd.read_csv(file_path)

# 2. Deep clean headers (removes hidden newlines \n, \r, extra spaces, or quotes)
df.columns = df.columns.astype(str).str.strip().str.replace('"', '')

# 3. Set the very first column dynamically as our X-axis index
first_col = df.columns[0]
df.set_index(first_col, inplace=True)

# 4. Deep clean index labels (e.g., turns '100KB\n' into '100KB')
df.index = df.index.astype(str).str.strip().str.replace('"', '')

# 5. Deep clean numeric values inside the table cells
for col in df.columns:
    if df[col].dtype == object:
        df[col] = pd.to_numeric(df[col].astype(str).str.strip().str.replace('"', ''), errors='coerce')


# =========================================================
# Part A & B: Dynamic Plotting (Bar, Line, Box)
# =========================================================

# Line Plot
plt.figure(figsize=(8, 5), dpi=120)
for col in df.columns:
    plt.plot(df.index, df[col], marker='o', linewidth=2, label=col)
plt.title('Execution Time vs Data Size (Line Plot)')
plt.xlabel('Data Size')
plt.ylabel('Execution Time')
plt.legend()
plt.grid(True, linestyle='--')
plt.savefig('part2_line_plot.png', dpi=300)
plt.close()

# Bar Plot
ax = df.plot(kind='bar', figsize=(8, 5), width=0.7, zorder=3)
ax.set_title('Execution Time by Algorithm (Bar Plot)')
ax.set_xlabel('Data Size')
ax.set_ylabel('Execution Time')
ax.grid(axis='y', linestyle='--', zorder=0)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('part2_bar_plot.png', dpi=300)
plt.close()

# Box Plot
plt.figure(figsize=(7, 5), dpi=120)
df.boxplot(column=list(df.columns), grid=True)
plt.title('Execution Time Distribution (Box Plot)')
plt.ylabel('Execution Time')
plt.savefig('part2_box_plot.png', dpi=300)
plt.close()

print("SUCCESS: All 3 plots generated successfully!")


# =========================================================
# Part C: Statistical Calculations for Alg.2
# =========================================================

# Grab the second column dynamically (Alg.2)
alg2_col = df.columns[1]

# Calculate mean explicitly for 100KB to 600KB range
target_sizes = ['100KB', '200KB', '300KB', '400KB', '500KB', '600KB']
subset_mean = df.loc[df.index.isin(target_sizes), alg2_col].mean()

# Calculate overall mean for the entire column (including 700KB when added)
total_mean = df[alg2_col].mean()

print(f"\n=== Statistical Analysis for [{alg2_col}] ===")
print(f"Mean execution time (100KB - 600KB) : {subset_mean:.2f}")
print(f"Overall Mean execution time (All rows): {total_mean:.2f}")