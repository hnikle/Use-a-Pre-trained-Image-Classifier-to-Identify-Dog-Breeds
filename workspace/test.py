from os import listdir



filename_list = listdir("pet_images/")
#     print("\nPrints 10 filenames from folder pet_images/")
#     for idx in range(0,40,1):
#     print("{:2d} file: {:>25}".format(idx+1, filename_list[idx]) )

# Creates empty dictionary named results_dic
results_dic = dict()

# Determines number of items in dictionary
items_in_dic = len(results_dic)
print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

# Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
# a List that contains only one item - the pet image label
filenames = filename_list
pet_labels =[]
for name in filenames:
    pet_name = ""
    for word in name.lower().split('_'):
        if word.isalpha():
            pet_name += word + " "

    pet_name = pet_name.strip()
    pet_labels.append(pet_name)

for idx in range(0, len(filenames), 1):
    if filenames[idx] not in results_dic:
         results_dic[filenames[idx]] = [pet_labels[idx]]
    else:
         print("** Warning: Key=", filenames[idx], 
               "already exists in results_dic with value =", results_dic[filenames[idx]])

#Iterating through a dictionary printing all keys & their associated values
print("\nPrinting all key-value pairs in dictionary results_dic:")
for key in results_dic:
    print("Filename=", key, "   Pet Label=", results_dic[key][0])
    
    
    
######################################################  
    
    
from classifier import classifier 
images_dir="pet_images"
model="vgg"
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
for key in results_dic:
    model_label = classifier(images_dir+"/"+key, model)
    model_label = model_label.lower().strip()
    truth = results_dic[key][0]

    if truth in model_label:
        results_dic[key].extend([model_label,1])
    else:
        results_dic[key].extend([model_label,0])

print(results_dic)



##########################################################
dogfile = "dognames.txt"
# Creates dognames dictionary for quick matching to results_dic labels from
# real answer & classifier's answer
dognames_dic = dict()

# Reads in dognames from file, 1 name per line & automatically closes file
with open(dogfile, "r") as infile:
    # Reads in dognames from first line in file
    line = infile.readline()

    # Processes each line in file until reaching EOF (end-of-file) by 
    # processing line and adding dognames to dognames_dic with while loop
    while line != "":

        # TODO: 4a. REPLACE pass with CODE to remove the newline character
        #           from the variable line  
        #
        # Process line by striping newline from line
        line = line.rstrip()

        # TODO: 4b. REPLACE pass with CODE to check if the dogname(line) 
        #          exists within dognames_dic, then if the dogname(line) 
        #          doesn't exist within dognames_dic then add the dogname(line) 
        #          to dognames_dic as the 'key' with the 'value' of 1. 
        #
        # adds dogname(line) to dogsnames_dic if it doesn't already exist 
        # in the dogsnames_dic dictionary
        if line not in dognames_dic:
            dognames_dic[line] = 1

        # Reads in next line in file to be processed with while loop
        # if this line isn't empty (EOF)
        line = infile.readline()

            
# Add to whether pet labels & classifier labels are dogs by appending
# two items to end of value(List) in results_dic. 
# List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
# List Index 4 = whether(1) or not(0) Classifier Label is a dog
# How - iterate through results_dic if labels are found in dognames_dic
# then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
for key in results_dic:

    # Pet Image Label IS of Dog (e.g. found in dognames_dic)
    if results_dic[key][0] in dognames_dic:
        
        # Classifier Label IS image of Dog (e.g. found in dognames_dic)
        # appends (1, 1) because both labels are dogs
        if results_dic[key][1] in dognames_dic:
            results_dic[key].extend((1, 1))

        # TODO: 4c. REPLACE pass BELOW with CODE that adds the following to
        #           results_dic dictionary for the key indicated by the 
        #           variable key - append (1,0) to the value using 
        #           the extend list function. This indicates
        #           the pet label is-a-dog, classifier label is-NOT-a-dog. 
        #                              
        # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
        # appends (1,0) because only pet label is a dog
        else:
            results_dic[key].extend((1, 0))

    # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
    else:
        # TODO: 4d. REPLACE pass BELOW with CODE that adds the following to
        #           results_dic dictionary for the key indicated by the 
        #           variable key - append (0,1) to the value uisng
        #           the extend list function. This indicates
        #           the pet label is-NOT-a-dog, classifier label is-a-dog. 
        #                              
        # Classifier Label IS image of Dog (e.g. found in dognames_dic)
        # appends (0, 1)because only Classifier labe is a dog
        if results_dic[key][1] in dognames_dic:
            results_dic[key].extend((0, 1))

        # TODO: 4e. REPLACE pass BELOW with CODE that adds the following to
        #           results_dic dictionary for the key indicated by the 
        #           variable key - append (0,0) to the value using the 
        #           extend list function. This indicates
        #           the pet label is-NOT-a-dog, classifier label is-NOT-a-dog. 
        #                                              
        # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
        # appends (0, 0) because both labels aren't dogs
        else:
            results_dic[key].extend((0, 0))

print(results_dic)