text = "hell     ll "
try:
    array_of_text = list(text)
    starting_index = 0
    index = 0
    stibiliser = 0
    length = len(array_of_text)
    while array_of_text[index] == " ":
        if array_of_text[index] == " ":
            array_of_text[index] = "\\"
            index +=1
            starting_index += 1
except IndexError:
    array_of_text = ''
    final_text = array_of_text
    return final_text

while index + 1 < length:
    if array_of_text[index] == array_of_text[index+1] == " ":
        array_of_text[index] = "\\"
        stabiliser += 1                                
    else:
        pointer += 1
    
for i in range(stabiliser + starting_index):
    array_of_text.remove("\\")
if array_of_text[-1] == " ":
    array_of_text.pop()

