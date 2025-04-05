empty_tuple = ()

# Tuple with value
value = (1,2,3,4,5)

# mixed value
mix_value = (10, "hello", 3.14)

# nested value
nested_value = (2,(34,5,67) , (456))

# single element
single_element = (45)

print(value,mix_value,single_element,nested_value)

print(value.count)

newTuple = value+mix_value;
print(newTuple)