"""
write program that reverse senatnce 
"""


from itertools import count


def reverse_senatnce(sentance):
    split_senatnce = sentance.split()
    result = split_senatnce[::-1]
    return result

def reverse_senatnce(sentance):
    return sentance[::-1]

def revrese_string(data):
    reverse_string = ""
    for char in data:
        reverse_string = char + reverse_string
    return reverse_string

# check if my string is palindrom
def palindrome(data):
    string_number = str(data)
    if string_number == string_number[::-1]:
        return True
    return False

#Count Vowels and Consonants:
def find_vovel_consonent(s):
    vovels = "aeiouAEIOU"
    vovelCount = 0
    consonentCount = 0
    for char in s:
        if char in vovels:
            vovelCount +=1
        else:
            consonentCount +=1
    vovelCount = len(s) - vovelCount
    consonentCount = len(s) - consonentCount
    return vovelCount, consonentCount

def count_vobels_consonent(s):
    vovels = "aeiouAEIOU"
    vovelCount = sum(1 for char in s if char in vovels)
    consonent_count = len(s) - vovelCount
    return vovelCount, consonent_count

# remove duplicate from string
def remove_duplicate(s):
    result = ""
    for i in s:
        if i not  in result:
            result +=i
    
    return result

def remove_duplicates(s):
    uniques = set()
    result = ""
    for char in s:
        if char not in uniques:
            uniques.add(char)
            result +=char
    return result


def add(*args,**quargs):
    print(args)
    for key, value in quargs.items():
        print(key,":",value)

x = {"name":"nitesh", "age":34}
y = [1,2,3,4,5]
# add(y, **x)

def find_vovels_consonent(data):
    vovels = "aeiouAEIOU"
    vovels_count = 0
    consonent_count = 0
    for char in data:
        if char in vovels:
            vovels_count +=1
        else:
            consonent_count +=1
    return vovels_count, consonent_count

vovels, consonent = find_vovels_consonent("deepakii")
print(vovels, consonent)


# print(palindrome(125))

# find square
def squire(data):
    return [i*i if i%2 == 0 else "nan" for i in data]

print(squire([2,4,8,9]))


# find sum from array using target

def find_sum(nums, target):
    complements = {}
    for num in range(len(nums)):
        complement = target - nums[num]
        if complement in complements:
            print(complements,"main return")
            return [complements[complement], num]
        complements[nums[num]] = num
        print(complements,"updating complemnts")


num = [2,7,6,8]
target = 9
print(find_sum(num, target))
