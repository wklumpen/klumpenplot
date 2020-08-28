from klumpenplot.core.datasource import DataSource

class Project:
    """Master project class
    """
    def __init__(self):
        self.name = None
        self.filepath = None
        self.data = None
        self.dataSources = dict()
        self.saved = False
        self.currentDataSource = None
        self.dataSourceIndex = 1

    def newDataSource(self, number, name):
        self.dataSources[number] = DataSource(number, name)
        self.setCurrentDataSource(number)
        self.dataSourceIndex += 1

    def setCurrentDataSource(self, number):
        self.currentDataSource = self.dataSources[number]

    def renameDataSource(self, number, newName):
        self.dataSources[number].name = newName