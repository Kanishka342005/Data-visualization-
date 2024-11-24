import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\KANISHKA SAKTHIVEL\Desktop\Jupyter\food_ingredients_and_allergens.csv'
df = pd.read_csv(file_path)


df['Main Ingredient'] = df['Main Ingredient'].str.split(',')
ingredient_df = df.explode('Main Ingredient')

ingredient_df['Main Ingredient'] = ingredient_df['Main Ingredient'].str.strip()

ingredient_df['Main Ingredient'] = ingredient_df['Main Ingredient'].str.strip()


plt.figure(figsize=(12, 8))
ingredient_counts.sort_index().plot(kind='line', marker='o', color='blue')
plt.title('Frequency of Main Ingredients in Food Products')
plt.xlabel('Main Ingredient')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()