import pandas as pd

# Load Titanic dataset from seaborn (built-in source)
import seaborn as sns
titanic = sns.load_dataset("titanic")

# Show first few rows
print("Sample Data:")
print(titanic.head())

# Create a pivot table: Average age and survival rate by sex and class
pivot_table = pd.pivot_table(
    titanic,
    values=["age", "survived"],
    index="sex",
    columns="class",
    aggfunc={"age": "mean", "survived": "mean"}
)

print("\nPivot Table (Mean Age & Survival Rate by Sex and Class):")
print(pivot_table)

OUTPUT:
Sample Data:
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True

[5 rows x 15 columns]

Pivot Table (Mean Age & Survival Rate by Sex and Class):
              age                        survived                    
class       First     Second      Third     First    Second     Third
sex                                                                  
female  34.611765  28.722973  21.750000  0.968085  0.921053  0.500000
male    41.281386  30.740707  26.507589  0.368852  0.157407  0.135447
