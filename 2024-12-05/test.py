# List of tuples
pairs = [
    ('47', '53'), ('97', '13'), ('97', '61'), ('97', '47'), ('75', '29'),
    ('61', '13'), ('75', '53'), ('29', '13'), ('97', '29'), ('53', '29'),
    ('61', '53'), ('97', '53'), ('61', '29'), ('47', '13'), ('75', '47'),
    ('97', '75'), ('47', '61'), ('75', '61'), ('47', '29'), ('75', '13'),
    ('53', '13')
]

# Define the value n you want to search for
n = '97'

# Get all pairs where the first element is 'n'
result = [second for first, second in pairs if first == n]

print(result)