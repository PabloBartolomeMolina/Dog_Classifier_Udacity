#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Pablo Bartolomé Molina
# DATE CREATED: 10/08/2024, 09:25PM CEST                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = dict()

    # Initialize all variables with information from results_stats_dic to 0.0, where:
    # A : Number of Correct Dog Matches;
    # B : Number of Dog Images;
    # C : Number of Correct Not-a-Dog Images;
    # D : Number of Not-a-Dog Images;
    # E : Number of Correct Dog Breeds;
    # Y : Number of Label Matches;
    # Z : Number of images.
    A = B = C = D = E = Y = Z = 0.0

    # Z : Number of images. It can be directly calculated.
    Z = len(results_dic)

    for dog in results_dic:
        # A : Number of Correct Dog Matches & C : Number of Correct Not-a-Dog Images.
        # A & C can be calculated with an if-elif to minimize computation time.
        if results_dic[dog][3] is 1 and results_dic[dog][4] is 1 : A += 1
        elif results_dic[dog][3] is 0 and results_dic[dog][4] is 0 : C += 1
        
        # B : Number of Dog Images. Can be calculated with the value of the 3rd index.
        if results_dic[dog][3] is 1 : B += 1 

        # E : Number of Correct Dog Breeds & Y : Number of Label Matches
        # With this structure, we can reuse the condition for Y as it is a subset of the conditions for E.
        if results_dic[dog][2] is 1 :
            Y += 1
            if results_dic[dog][3] is 1: E += 1

    # D : Number of Not-a-Dog Images. Can be calculated at the end with a simple difference 
    # instead of using an if-elif structure with the computation of B : Number of Dog Images.
    D = Z - B
    
    results_stats_dic['n_images'] = int(Z)
    results_stats_dic['n_dogs_img'] = int(B)
    results_stats_dic['n_notdogs_img'] = int(D)
    results_stats_dic['n_correct_dogs'] = int(A)
    results_stats_dic['n_correct_notdogs'] = int(C)
    results_stats_dic['n_correct_breed'] = int(E)

    # Compute the percentages for the dictionary results_stats_dic.

    # Objective 1_a : % of Correctly Classified Dog Images, (A/B) * 100.
    results_stats_dic['pct_correct_dogs'] = (A/B) * 100
    # Objective 1_b : % of Correctly Classified Not-a-Dog Images, (C/D) * 100.
    results_stats_dic['pct_correct_notdogs'] = (C/D) * 100
    # Objective 2   : % of Correctly Classified Dog Breeds, (E/B) * 100.
    results_stats_dic['pct_correct_breed'] = (E/B) * 100
    # Optional      : % of Label Matches, (Y/Z) * 100.
    results_stats_dic['pct_label_matches'] = (Y/Z) * 100

    return results_stats_dic
