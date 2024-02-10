class LabelEncoder:
    def __init__(self):
        self.mapping = {}
        self.reverse_mapping = {}

    def fit(self, labels):
        unique_labels = set(labels)
        self.mapping = {label: index for index, label in enumerate(unique_labels)}
        self.reverse_mapping = {index: label for label, index in self.mapping.items()}

    def transform(self, labels):
        return [self.mapping[label] for label in labels]

    def inverse_transform(self, encoded_labels):
        return [self.reverse_mapping[index] for index in encoded_labels]


labels = ['Zain', 'Ali', 'Ahmed', 'Fatima', 'Ayesha', 'Bilal']
encoder = LabelEncoder()
encoder.fit(labels)

encoded_labels = encoder.transform(labels)
decoded_labels = encoder.inverse_transform(encoded_labels)

print("Original labels:", labels)
print("Encoded labels:", encoded_labels)
print("Decoded labels:", decoded_labels)
