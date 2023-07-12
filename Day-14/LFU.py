def __init__(self, capacity):
    self.key_to_val_frequency_mapping = collections.defaultdict(tuple)
    self.frequency_to_key_list_mapping = collections.defaultdict(collections.deque)
    self.min_frequency = 1
    self.capacity = capacity
    self.count = 0
    
def get(self, key):
    if key not in self.key_to_val_frequency_mapping:
        return -1
    
    self.move_frequency(key)
    return self.key_to_val_frequency_mapping[key][0]

def move_frequency(self, key):
    value, frequency = self.key_to_val_frequency_mapping[key]
    key_list = self.frequency_to_key_list_mapping[frequency]
    if len(key_list) == 1:
        self.frequency_to_key_list_mapping[frequency].remove(key)
        if self.min_frequency == frequency:
            self.min_frequency += 1
    else:
        self.frequency_to_key_list_mapping[frequency].remove(key)
    self.frequency_to_key_list_mapping[frequency + 1].append(key)
    self.key_to_val_frequency_mapping[key] = (value, frequency + 1)
    
def put(self, key, value):
    if not self.capacity:
        return
    if key in self.key_to_val_frequency_mapping:
        old_value, frequency = self.key_to_val_frequency_mapping[key]
        self.key_to_val_frequency_mapping[key] = (value, frequency)
        self.move_frequency(key)
    else:
        if self.count == self.capacity:
            removed_key = self.frequency_to_key_list_mapping[self.min_frequency].popleft()
            if not self.frequency_to_key_list_mapping[self.min_frequency]:
                self.frequency_to_key_list_mapping.pop(self.min_frequency)
            self.key_to_val_frequency_mapping.pop(removed_key)
            self.count -= 1
        self.key_to_val_frequency_mapping[key] = (value, 1)
        self.frequency_to_key_list_mapping[1].append(key)
        self.min_frequency = 1
        self.count += 1