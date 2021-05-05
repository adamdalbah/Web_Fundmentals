# 1- Biggie Size :
# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list

# l = [-1, 3, 5, -5]
# print(biggie_size(l))

#2- Count Positives:
# def count_positives(list):
#     count = 0;
#     for i in range(len(list)):
#         if list[i] > 0:
#             count += 1
#     list[len(list)-1] = count
#     return list
# x = [-1, 1, 1, 1]
# print(count_positives(x))

#3-Sum Total:
# def sum_total(list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return sum
# x = [1,2,3,4]
# print(sum_total(x)) 

#4-Average:
# def average(list):
#     sum = 0
#     for i in range(len(list)):
#         sum+=list[i]
#     return sum/len(list)

# x = [1,2,3,4]
# print(average(x))

#5- length:
# def length(list):
#     count = 0
#     for i in x:
#         count += 1
#     return count    
# x = [1, "apple", 2]  
# print(length(x))

#6- Minimum:
# def minimum(list):
#     min=list[0]
#     for i in range(len(list)):
#         if(list[i] < min):
#             min = list[i]
#     return min 
# x = [1,2,3,4,5,0]
# print(minimum(x))      

#7- Maximum:
# def maximum(list):
#     max = list[0]
#     for i in range(len(list)):
#         if list[i] > max:
#             max = list[i]
#     return max
# x= [1,2,3,4,5]
# print(max(x))  

#8- Ultimate Analysis:
# def ultimate_analysis(list):
#     sum = 0
#     min = list[0] 
#     max = list[0]
#     for i in range(len(list)):
        
#         if list[i] > max:
#             max = list[i]
#         elif list[i] < min:
#             min = list[i]
#         sum += list[i]
#     x = {'sumTotal': sum, 'average': sum/len(list), 'minimum':min, 'maximum':max, 'length':len(list)}
#     return x

# x = [37,2,1,-9]
# print(ultimate_analysis(x))

#9- Reverse List:
# def reverse_list(list):
#     for i in range(int(len(list)/2)):
#         temp = list[i]
#         list[i] = list[len(list)-1-i]
#         list[len(list)-1-i] = temp
#     return list
# x = [37,2,1,-9]
# print(reverse_list(x))    
