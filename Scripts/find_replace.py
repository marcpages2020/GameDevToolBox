import os

print("From which folder do you want to replace the names?")
folder_path = input()

print("Which word do you want to replace?")
restricted_word = input()

print("Which word do you want to set as new?")
replace_word = input()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.__contains__(restricted_word):
            old_name = file
            new_name = file.replace(restricted_word, replace_word)
            
            old_path = os.path.join(root, old_name)
            new_path = os.path.join(root, new_name)
            
            os.rename(old_path, new_path)
            
            print("Replaced: " + old_name + "with: " + new_name)