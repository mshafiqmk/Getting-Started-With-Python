phone = input("Phone: ")
digits_mapping = {
    "1" : "ONE",
    "2" : "TWO",
    "3" : "THREE",
    "4" : "FOUR"
}
for ch in phone:
    print(digits_mapping.get(ch,"!"))