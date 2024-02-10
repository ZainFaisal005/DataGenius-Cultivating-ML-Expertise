class Scaler:
    def __init__(self):
        self.mean = None
        self.std_dev = None
        self.min_val = None
        self.max_val = None

    def normalize(self, data):
        if self.min_val is None or self.max_val is None:
            self.min_val = min(data)
            self.max_val = max(data)

        normalized_data = [(val - self.min_val) / (self.max_val - self.min_val) for val in data]
        return normalized_data

    def standardize(self, data):
        if self.mean is None or self.std_dev is None:
            self.mean = sum(data) / len(data)
            self.std_dev = (sum((val - self.mean) ** 2 for val in data) / len(data)) ** 0.5

        standardized_data = [(val - self.mean) / self.std_dev for val in data]
        return standardized_data

# Example usage:
data = [2, 4, 6, 8, 10]
scaler = Scaler()

# Normalization
normalized_data = scaler.normalize(data)

# Standardization
standardized_data = scaler.standardize(data)

print("Original data:", data)
print("Normalized data:", normalized_data)
print("Standardized data:", standardized_data)
