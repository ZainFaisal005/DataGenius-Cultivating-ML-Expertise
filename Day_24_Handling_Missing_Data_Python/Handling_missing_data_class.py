class MinMaxScaler:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def fit(self, data):
        flat_data = [item for sublist in data for item in sublist]
        self.min_val = min(flat_data)
        self.max_val = max(flat_data)

    def transform(self, data):
        normalized_data = [
            [(val - self.min_val) / (self.max_val - self.min_val) if val is not None else None for val in row]
            for row in data
        ]
        return normalized_data

class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std_dev = None

    def fit(self, data):
        flat_data = [item for sublist in data for item in sublist if sublist is not None]
        self.mean = sum(flat_data) / len(flat_data)
        self.std_dev = (sum((val - self.mean) ** 2 for val in flat_data) / len(flat_data)) ** 0.5

    def transform(self, data):
        standardized_data = [
            [(val - self.mean) / self.std_dev if val is not None else None for val in row]
            for row in data
        ]
        return standardized_data

class MissingValuesHandler:
    def __init__(self):
        self.mean_values = None

    def fit(self, data):
        self.mean_values = [sum(filter(None, column)) / len(list(filter(None, column))) for column in zip(*data)]

    def transform(self, data):
        imputed_data = [
            [val if val is not None else mean for val, mean in zip(row, self.mean_values)]
            for row in data
        ]
        return imputed_data

class Scaler:
    def __init__(self):
        self.min_max_scaler = MinMaxScaler()
        self.standard_scaler = StandardScaler()
        self.missing_values_handler = MissingValuesHandler()

    def fit(self, data):
        self.min_max_scaler.fit(data)
        self.standard_scaler.fit(data)
        self.missing_values_handler.fit(data)

    def transform(self, data):
        normalized_data = self.min_max_scaler.transform(data)
        standardized_data = self.standard_scaler.transform(data)
        imputed_data = self.missing_values_handler.transform(data)

        return normalized_data, standardized_data, imputed_data

# Example usage:
data_with_missing_values = [
    [2, 4, 6, 8, 10],
    [1, 3, 12, 7, 9],
    [5, 8, 3, 9, 1],
]

scaler = Scaler()
scaler.fit(data_with_missing_values)
normalized_data, standardized_data, imputed_data = scaler.transform(data_with_missing_values)

print("Original data with missing values:")
for row in data_with_missing_values:
    print(row)

print("\nNormalized data:")
for row in normalized_data:
    print(row)

print("\nStandardized data:")
for row in standardized_data:
    print(row)

print("\nImputed data:")
for row in imputed_data:
    print(row)
