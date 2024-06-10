def string_slices(string: str) -> str:
    new_string = string[2:-2]
    return new_string
    
print(string_slices('%%Приказ об увольнении&#'))