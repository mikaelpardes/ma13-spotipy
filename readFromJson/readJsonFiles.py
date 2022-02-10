import json
import os


def read(folderPath):
    documents = os.listdir(folderPath)
    dataStorage = []
    for file in documents:
        with open(folderPath + "\\" + file) as fileInJson:
            jsonObject = json.load(fileInJson)
            dataStorage.append(jsonObject)
    return dataStorage


dataStorage = read("C:\songs (1)")
print(dataStorage)
