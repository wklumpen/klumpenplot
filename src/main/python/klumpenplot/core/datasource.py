class DataSource:
    """The main data source definition. Contains elements required by all data sources.
    """
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.charts = []

    def addChart(self, name):
        pass
