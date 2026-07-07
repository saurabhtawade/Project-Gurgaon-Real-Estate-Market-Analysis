import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data in excel.csv')
# df.shape
# df.info()

# # Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

# # Numeric Columns cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

# print(df["price"])
# print(df["area"])
# print(df["rate_per_sqft"])

# Categorical Columns cleaning

df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()

df = df.drop_duplicates()

# print(df)
# print(df.info())

# #Question 1: Which is the costliest flat?
# df = df.loc[df["price"].idxmax()]
# print("Costliest flat details:")
# print(df)


# #Question 2: Which locality has the highest average price?
# df = df.groupby("locality")["price"].mean().sort_values(ascending=False)
# print("Locality with highest average price:")
# print(df.head(1))

# #Question 3: Which locality has the highest rate per square foot?
# df = df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)
# print("Locality with highest rate per square foot:")
# print(df.head(1))

#Question 4: Ready-to-move vs Under-construction pricing
df = df.groupby("status")["price"].median()
print("Pricing comparison between ready-to-move and under-construction properties:")
print(df)

# # Question 5: Does RERA approval affect pricing?
# df = df.groupby("rera_approval")["price"].median()
# print("Impact of RERA approval on pricing:")
# print(df)

# # Question 6: How does area impact price?
# sns.scatterplot(x="area", y="price", data=df)
# plt.show()


# #Question 7: Which BHK configuration is most expensive?
# df.groupby("bhk_count")["price"].mean()

# #Question 8: Which property type is the costliest?
# df.groupby("flat_type")["price"].mean()

# #Question 9: Do certain builders price higher?
# df.groupby("company_name")["price"].mean().sort_values(ascending=False)

# #Question 10: Are larger homes more expensive per sqft?
# sns.scatterplot(x="area", y="rate_per_sqft", data=df)
# plt.show()

