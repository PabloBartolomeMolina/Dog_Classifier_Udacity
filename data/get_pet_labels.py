#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Pablo Bartolomé Molina
# DATE CREATED: 04/08/2024, 17:10 CEST                                    
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    filename_list = listdir(image_dir) # List of filenames.
    results_dic = dict()  # Initialize an empty dictionary.

    for filename in filename_list:
      # Raw filename to be properly formatted as label.
      label = filename
      # Replace underscores with spaces and convert to lowercase.
      label = filename.replace('_', ' ').lower().strip()
      # Split the string into words. This allows to easily remove all characters that are not letter.
      words = label.split()
      # Filter out words including symbols and/or numbers and strip extra spaces.
      # If different format are in the input filenames to those existing, this line would need an adaptation.
      words = [word.strip() for word in words if word.isalpha()]
      # Join the words back into a single string with spaces between them.
      label = ' '.join(words)
      tmp_list = [label]  # Formatting to make easier the later handling of information.
      # New element in the dictionary including key and label in the requested format.
      results_dic[filename] = tmp_list
    
    # Debug purpose, print each pair key-element.
    #for key, value in results_dic.items():
      #print(f'{key}: {value}')

    return results_dic
