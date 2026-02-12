import pandas as pd

data = pd.read_csv("netflix_movies.csv")
# print(data)

print(data.shape)
print(data.head())
print(data.columns)

print('\n')

print("MISSING VALUES")


# missing values check
print(data.isnull().sum())


print('\n')

print("DUPLICATE VALUES")


# duplicate values
print(data.duplicated().sum())



# handle missing values
data['director'] = data['director'].fillna("Unknown")



data['cast'] = data['cast'].fillna("Unknown")



data['country'] = data['country'].fillna("Unknown")



data['rating'] = data['rating'].fillna(data['rating'].mode()[0])


data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])


print(data.isnull().sum())

data.columns = data.columns.str.lower().str.replace(" ", "_")
print(data.columns)

data['country'] = data['country'].str.strip()

data['director'] = data['director'].str.strip()

data['cast'] = data['cast'].str.strip()

data['rating'] = data['rating'].str.strip()

data['type'] = data['type'].str.strip()


