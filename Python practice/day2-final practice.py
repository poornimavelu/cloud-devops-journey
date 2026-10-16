error_code = "err-404-auth-fail"
filtered_code = ""

filtered_code = error_code.replace("-","*")

for filtered_code in range (0,-1): 
    print ("filtered code is:",filtered_code)


error_code = "err-404-auth-fail"
filtered_code = ""

# Loop directly over each character in the string
for char in error_code:
    if char == "-":
        filtered_code += "*"
    else:
        filtered_code += char.upper()

print("Filtered code is:", filtered_code)