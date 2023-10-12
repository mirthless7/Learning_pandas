import pandas as pd

#lists and dictionaries
column=["Mariya","John","Dmytro"]

#dictionary made
titled_column={"name":column,
               "height":[6.1,6.2,5.7],
               "weight":[270,300,160]}

#turns the list into a dataframe
data =pd.DataFrame(titled_column)

#iloc means a row, selecting values from a dataframe
select_column=data["weight"][1]
select_row=data.iloc[1]["weight"]

#manipulate dataframe values
bmi=[]

#6:28 for
# #tommoro



print(select_row)
