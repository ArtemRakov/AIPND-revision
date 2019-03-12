#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER:
# DATE CREATED:
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
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create
#       with this function
#   index 0 = pet image label (string)
#   index 1 = classifier label (string)
#   index 2 = 1/0 (int)  where 1 = match between pet image
#     and classifer labels and 0 = no match between labels
# ------ where index 3 & index 4 are added by this function -----
#  NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
#             0 = pet Image 'is-NOT-a' dog.
#  NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image
#             'as-a' dog and 0 = Classifier classifies image
#             'as-NOT-a' dog.
#
def calculates_results_stats(results_dic):
    results_stats_dic = {}
    results_stats_dic['n_images'] = len(results_dic)

    images = len(results_dic)
    n_dogs_img = n_match = n_correct_dogs = n_correct_notdogs = n_correct_breed = 0

    # this whole thing is very messy. (idk how to really solve this)
    # If I create methods to update variables it maybe be even messier

    for value in results_dic.values():
        n_dogs_img += value[3]
        n_match += value[2]
        n_correct_dogs += 1 if value[3] and value[4] else 0
        n_correct_notdogs += 1 if not value[3] and not value[4] else 0
        n_correct_breed += 1 if value[2] and value[3] else 0

    n_notdogs_img = images - n_dogs_img
    pct_match = n_match / images * 100
    pct_correct_dogs = n_correct_dogs / n_dogs_img * 100
    pct_correct_breed = n_correct_breed / n_dogs_img * 100
    pct_correct_notdogs = n_correct_notdogs / n_notdogs_img * 100

    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['pct_match'] = pct_match
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs

    return results_stats_dic
