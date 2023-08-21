# slicing = create a substring by 
# extracting elements from another string

# indexing[] or slice()
# [start:stop:step]

name = "Luiza Picoli"
first_name = name[0:5]
last_name = name[6:]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(reversed_name)

website = "http://wikipedia.com"

slice = slice(7,-4)
print(website[slice])
