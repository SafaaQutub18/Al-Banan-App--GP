fullstring = "صفاء السلام عليكم نهى صباح الخير"
substring = "السلام عليكم"

start_index= fullstring.find(substring)
if start_index != -1:
    
    print(start_index)
    print(len(substring) + start_index)
else:
    print("Not found!")