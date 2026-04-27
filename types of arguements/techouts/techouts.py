" you are given a integer array nums find the length of the longest contiguous "
" subarray where the number of even elements equals the number of odd elements."

# nums=[1,2,3,4,5,6]
# i=0
# count=0
# while 1<=len(nums):
#     if nums[i]%2==0 or nums[i]%2==1:
#         i+=1
#         count=count+i

# def longest_even_odd_balance():
#     nums=[1,2,3,4,5,6]   
#     count=0
#     i=0
#     if nums[i]%2==0 or nums[i]%2==1:
#        i+=6
#        count=count+i
#     return count
# n=longest_even_odd_balance()
# print(n)

"""Iris flower classification using EDA and machine learning
      perform basic data cleaning, visulalization and model building. submit your work as a well-structured 
      jupyter notebook or report clearly show rour code,charts,and final evaluation results"""
"data cleaning & prepation"

from sklearn.datasets import load_iris
data=load_iris()
print(data)
