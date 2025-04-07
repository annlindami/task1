import pandas as pd  #importing library pandas
data=pd.read_csv("netflix_titles.csv")
#reading a csv file using pd.read_csv() function
print(data.head)  #printing some of the rows of data
print(data['show_id'])  #gives the variable named show_id
print(data.show_id[2])  #gives the 2nd element of the variable named show_id
print(data.isnull().sum()) #This will show the number of missing values in each column.
print(data.isnull().sum().sum()) #gives the total no of missing values in the dataset
data['director']=data['director'].fillna('Unknown')
data['cast']=data['cast'].fillna('Unknown')
data['country']=data['country'].fillna('Unknown')
data['date_added']=data['date_added'].fillna('Unknown')
data['rating']=data['rating'].fillna('Unknown')
data['duration']=data['duration'].fillna('Unknown') #fill unknown inplace of missing values
print(data.isnull().sum().sum()) #rechecking if there is any missing values
print(data.shape) # gives the number of cases and the no. of variables
data=data.drop_duplicates() # remove duplicate rows
print(data.shape) #rechecking, no of cases remians the same
data.reset_index(drop=True, inplace=True) # reseting the index
print(data.shape) # rechecking we can conclude that, there are no duplicate rows in this dataset
data['show_id'] = data['show_id'].str.title()
data['type'] = data['type'].str.title()
data['title'] = data['title'].str.title()
data['director'] = data['director'].str.title()
data['country'] = data['country'].str.upper()
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce') # standardising all the values
print(data.date_added[2])
data['date_added'] = data['date_added'].dt.strftime('%d-%m-%Y')
print(data.date_added[2]) # converting date formats to dd-mm-yyyy format. It is only possible to do this, after converting the date to a standard python form
print(data.columns) #printing column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
#modifying the column names to have no spaces and all lower case
print(data.columns) #rechecking
print(data.dtypes) #shows the datatype for each column
print(data['date_added'].dtype)  # should be datetime64[ns], but here the data type is object
data['date_added'] = pd.to_datetime(data['date_added'], format='%d %m, %Y', errors='coerce')
print(data['date_added'].dtype)
#used format option to specify the datatype of date_added 