class OneHotEncoder:
    def __init__(self):
        self.categories = None

    def fit(self, labels):
        self.categories = list(set(labels))

    def transform(self, labels):
        encoded_labels = []
        for label in labels:
            encoding = [1 if label == category else 0 for category in self.categories]
            encoded_labels.append(encoding)
        return encoded_labels

    def inverse_transform(self, encoded_labels):
        decoded_labels = [self.categories[index.index(1)] for index in encoded_labels]
        return decoded_labels


labels = ['Zain', 'Ali', 'Ahmed', 'Fatima', 'Ayesha', 'Bilal']
encoder = OneHotEncoder()
encoder.fit(labels)

encoded_labels = encoder.transform(labels)
decoded_labels = encoder.inverse_transform(encoded_labels)

print("Original labels:", labels)
print("Encoded labels:", encoded_labels)
print("Decoded labels:", decoded_labels)
