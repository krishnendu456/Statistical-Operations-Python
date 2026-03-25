def mapper(text):
    words = text.split()
    mapped = [(word.lower(), 1) for word in words]
    
    print("\n--- Mapper Output ---")
    for pair in mapped:
        print(pair)
    
    return mapped


def shuffle(mapped_data):
    shuffled = {}
    for word, count in mapped_data:
        if word not in shuffled:
            shuffled[word] = []
        shuffled[word].append(count)
    
    print("\n--- Shuffle Output ---")
    for key, value in shuffled.items():
        print(f"{key} : {value}")
    
    return shuffled


def reducer(shuffled_data):
    reduced = {}
    for word, counts in shuffled_data.items():
        reduced[word] = sum(counts)
    
    print("\n--- Reducer Output ---")
    for key, value in reduced.items():
        print(f"{key} : {value}")
    
    return reduced


# Example input
text = "Hello world hello MapReduce world"

print("Input Text:", text)

# Step 1: Map
mapped = mapper(text)

# Step 2: Shuffle
shuffled = shuffle(mapped)

# Step 3: Reduce
result = reducer(shuffled)