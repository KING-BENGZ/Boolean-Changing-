# Boolean value
T = True
F = False 
boolean_value = F #slot the response here 

# Convert boolean to custom string
string_value = "Yes" if boolean_value == T else "No"

print(string_value)  # Output: 'Yes'

boolean_value = True if string_value.lower() == "yes" else False

print(boolean_value)  # Output: True
