from antibody_app.models import Antibody
import pandas as pd
import numpy as np
# from openpyxl import workbook, load_workbook

#Create mysql connection to antibody database



#'venv/Scripts/omip86_omip76.xlsx'
#importing data from excel
def importExcelSheet(filename):
    importedData = pd.read_excel(filename)
    importedData = importedData.fillna('')
    return importedData

def getColumnsDataFromExcelSpreadsheet(filename):
    data = importExcelSheet(filename)
    data_array = data.columns
    columns = []
    for i in data_array:
        columns.append(i)
    return columns

def createKeys(filename):
    data = importExcelSheet(filename)
    data_dict = data.to_dict()
    return data_dict

# Get the existing columns in the MySQL table
# def getExistingColumns(table_name):
#     mydb = mySqlConnection()
#     mycursor = mydb.cursor()
#
#     mycursor.execute(f"SHOW COLUMNS FROM {table_name}")
#     existing_columns = [col[0] for col in mycursor.fetchall()]
#
#     mydb.close()
#
#     return existing_columns

# Function to create a dictionary from the imported Excel data, with column names as keys and data as values
def createKeys(filename):
    data = importExcelSheet(filename)
    data_dict = data.to_dict()
    return data_dict

# Function to insert data from the Excel file into the Antibody model
def insertRowsIntoTable(data_dict):
    try:
        for index in range(len(data_dict['name'])):
            name_value = data_dict['name'][index]
            if name_value == '':
                continue

            antibody_instance = Antibody(
                name=name_value,
                target_antigen=data_dict['target_antigen'][index],
                host_species=data_dict['host_species'][index],
                ab_type=data_dict['ab_type'][index],
                isotype= dict['isotype'][index],
                clone= dict['clone'][index],
                fluorophore= dict['fluorophore'][index],
                metal_tag= dict['metal_tag'][index],
                other_tag= dict['other_tag'][index],
                supplier= dict['supplier'][index],
                catalogue_num = dict['catalogue_num'][index]
                # Add other fields as needed
            )
            antibody_instance.save()
    except Exception as e:
        raise Exception(f"Error occurred while inserting data: {e}")

def processUpload(filename):
    data_dict = createKeys(filename)
    try:
        insertRowsIntoTable(data_dict)
    except Exception as e:
        raise Exception(f"Error occurred during data processing: {e}")


