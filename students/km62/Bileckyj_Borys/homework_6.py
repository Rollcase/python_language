Skip to content
This repository
Search
Pull requests
Issues
Gist
 @Rollcase
 Watch 3
  Star 8
  Fork 72 tarys/python_language
 Code  Issues 0  Pull requests 79  Projects 0  Wiki  Pulse  Graphs
Tree: a15da6371f Find file Copy pathpython_language/students/km62/Malyarenko_Illya/homework_6.py
fe3ec7c  13 hours ago
@ASIMER ASIMER 6. list
1 contributor
RawBlameHistory     
423 lines (342 sloc)  16.5 KB
# task1------------------------------------------------------------
"""
�������� ��� �������� ������ � ������� ��������� (�� ���� A[0], A[2], A[4], ...).
"""

# defaults
#������ ������
list_output = []
# input
#���� ������ � ��������
list= input().split()
# main
for index in range(len(list)):
	#�������� ������� �� ��������
    if index % 2 == 0:
        list_output.append(list[index])
# result
print(' '.join(list_output))

# -----------------------------------------------------------------


# task2------------------------------------------------------------
"""
�������� ��� ������ �������� ������. ��� ���� ����������� ���� for, ������������ �������� ������, � �� �� �������!
"""

# defaults
#������ ������
list_output = []
# input
#���� ������ � ��������
list= input().split()
# main
for element in list:
    if element != ' ':
		#�������� �������� �� ��������
        if int(element)%2 == 0:
            list_output.append(element)
# result
print(' '.join(list_output))

# -----------------------------------------------------------------


# task3------------------------------------------------------------
"""
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������.
"""


# defaults
#������ ������
list_output = []
# input
#���� ������ � ��������
list= input().split()
# main
#���� ���������� ��� ���������� ����. �������.
element_buffer=list[0]
#������� ���������
for element in list:
    if element != ' ':
        #��������� ��������� � ��������� ����������
        if float(element)>float(element_buffer):
            list_output.append(element)
    element_buffer = element
# result
print(' '.join(list_output))

# -----------------------------------------------------------------


# task4------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. ���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����.
"""


# defaults
#������ ������
list_output = []
# input
#���� ������ � ��������
list= input().split()
# main
#���� ���������� ��� ���������� ����. �������.
element_buffer=list[0]
#������� ��������� �� ��������� ����� 1-��
for element in list[1:len(list)+1]:
    if element != ' ':
        #��������� ��������� � ��������� ����������
        if float(element)/abs(float(element)) == float(element_buffer)/abs(float(element_buffer)):
            list_output.append(str(element_buffer)); list_output.append(str(element))
            break
    element_buffer = float(element)
# result
print(' '.join(list_output))

# -----------------------------------------------------------------


# task5------------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ���� ������ ���������, ������� ������ ���� ����� �������, � �������� ���������� ����� ���������. ������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.
"""


# defaults
#������ ������
list_output = []
counter = 0
# input
#���� ������ � ��������
list= input().split()
#�������� ����� ������
if len(list)>=3:
    # main
    #���� ���������� ��� ���������� ����. �������.
    element_buffer_first=list[0]
    element_buffer_second=list[1]
    #������� ��������� �� ��������� ����� 1-��
    for element in list[2:len(list)+1]:
       if element != ' ':
            #��������� ��������� � ��������� ����������
          if element_buffer_first < element_buffer_second > element:
             counter += 1
       element_buffer_first = element_buffer_second
       element_buffer_second = element
# result
print(counter)

# -----------------------------------------------------------------


# task6------------------------------------------------------------
"""
��� ������ �����. �������� �������� ����������� �������� � ������, � ����� ������ ����� �������� � ������. ���� ���������� ��������� ���������, �������� ������ ������� �� ���.
"""


# defaults
index = 0
index_output = 0
# input
#���� ������ � ��������
list= input().split()
# main
#���� ���������� ��� ���������� ����. �������.
element_buffer=list[0]
#������� ���������
for element in list:
    if element != ' ':
        #��������� ��������� � ��������� ����������
        if float(element)>float(element_buffer):
            element_buffer = element
            index_output = index
        index += 1

# result
print(element_buffer, index_output)

# -----------------------------------------------------------------

# task7------------------------------------------------------------
"""
���� ������� � ������ �����. �� ����� ����������� ��� ������������ ���������� ��� ����� � �����. �������� ��� ��� �������.
��������� �������� �� ���� �������������� ������������������ ����������� �����, ���������� ���� ������� �������� � �����. ����� ����� �������� ����� X � ���� ����. ��� ����� �� ������� ������ ����������� � �� ��������� 200.
�������� �����, ��� ������� ���� ������ ������ � �����. ���� � ����� ���� ���� � ���������� ������, ����� ��, ��� � ����, �� �� ������ ������ ����� ���.
"""


# defaults
counter = 1
# input
#���� ������ � ��������
list= input().split()
height = float(input())
# main
#���� ���������� ��� ���������� ����. �������.
element_buffer=list[0]
#������� ���������
for element in list:
    if element != ' ':
        #��������� ��������� � ��������� ����������
        if float(element)>=float(height):
            counter += 1
# result
print(counter)

# -----------------------------------------------------------------


# task8------------------------------------------------------------
"""
��� ������, ������������� �� ���������� ��������� � ���. ����������, ������� � ��� ��������� ���������.
"""


# defaults
counter = 1
# input
#���� ������ � ��������
list= input().split()
# main
#���� ���������� ��� ���������� ����. �������.
element_buffer=list[0]
#������� ���������
for element in list:
    if element != ' ':
        #��������� ��������� � ��������� ����������
        if float(element)!=float(element_buffer):
            counter += 1
        element_buffer = element
# result
print(counter)

# -----------------------------------------------------------------


# task9------------------------------------------------------------
"""
����������� �������� �������� ������ (A[0] c A[1], A[2] c A[3] � �. �.). ���� ��������� �������� �����, �� ��������� ������� �������� �� ����� �����.
"""


# defaults
counter_prew_index = 1
element_buffer = 0
# input
#���� ������ � ��������
list= input().split()
# main
#�������� �� �������� ����� ������
if len(list) % 2 != 0:
    max_count = len(list) - 1 #�������� ���������� ��� ����� � ����� for
else:
    max_count = len(list)
for i in range(0, max_count, 2):
    element_buffer = list[i]
    list[i] = list[i+1]
    list[i+1] = element_buffer
# result
print(' '.join(list))

# -----------------------------------------------------------------


# task10------------------------------------------------------------
"""
� ������ ��� �������� ��������. ��������� ������� ����������� � ������������ ������� ����� ������.
"""


# defaults
index_counter = -1
index_max = 0
index_min = 0
# input
#���� ������ � �������
list= input().split()
# main
#���� ���������� ��� ���������� ����. �������.
min_element_buffer = list[0]
max_element_buffer = list[0]
#������� ���������
for element in list:
    index_counter += 1
    if element != ' ':
        if float(min_element_buffer) > float(element):
            min_element_buffer = element
            index_min = index_counter
        if float(max_element_buffer) < float(element):
            max_element_buffer = element     
            index_max = index_counter

element_buffer = list[index_min]
list[index_min] = list[index_max]
list[index_max] = element_buffer
# result
print(' '.join(list))


# -----------------------------------------------------------------


# task11------------------------------------------------------------
"""
��� ������ �� ����� � ������ �������� � ������ k. ������� �� ������ ������� � �������� k, ������� ����� ��� ��������, ������� ������ �������� � �������� k.
��������� �������� �� ���� ������, ����� ����� k. ��������� �������� ��� ��������, � ����� ����� ������� ��������� ������� ������ ��� ������ ������ pop() ��� ����������.
��������� ������ ������������ ����� ��������������� � ������, � �� ������ ��� ��� ������ ���������. ����� ������ ������������ �������������� ������. ����� �� ������� ������������ ����� pop(k) � ����������.
"""


# input
#���� ������ � ��������
list= input().split()
index = int(input()) + 1
# main
while index < len(list):
    list[index-1] = list[index]
    index += 1
list.pop()
# result
print(' '.join(list))

# -----------------------------------------------------------------


# task12------------------------------------------------------------
"""
��� ������ ����� �����, ����� k � �������� C. ���������� �������� � ������ �� ������� � �������� k �������, ������ C, ������� ��� ��������, ������� ������ �� ����� k, ������.
��������� ��� ���� ���������� ��������� � ������ �������������, ����� ���������� ������ � ��� ����� ����� ����� �������� ����� �������, ��������� ����� append.
������� ���������� ������������ ��� � ��������� ������, �� ����� ����� ��� ������ � �� �������� ��������������� ������.
"""

# input
#���� ������ � ��������
list = input().split()
index_and_number = input().split()
# main
list.append(index_and_number[1])
index = len(list) - 1
while int(index_and_number[0]) < index:
    element_buffer = list[index-1]
    list[index-1] = list[index]
    list[index] = element_buffer
    index -= 1
# result
print(' '.join(list))


# -----------------------------------------------------------------


# task13------------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ��� ��� ���������, ������ ���� �����. ���������, ��� ����� ��� ��������, ������ ���� ����� �������� ���� ����, ������� ���������� ���������.
"""


#default
counter = 0
# input
#���� ������ � ��������
list= input().split()

# main
#�������� ��������
for element_iteration_1 in list:
    #����� ����
    for element_iteration_2 in list:
        if element_iteration_1 == element_iteration_2:
            counter += 1 #����������� ������ 1, ����� ������� �������� ����
    counter -= 1#�������� ������ �������
# result
print(counter/2) #��� ��� � ���� 2 ��������, � ������ ���� ����, ����� ����� � 2 ���� ������ ��� ���

# -----------------------------------------------------------------


# task14------------------------------------------------------------
"""
��� ������. �������� �� ��� ��������, ������� ����������� � ������ ������ ���� ���. �������� ����� �������� � ��� �������, � ������� ��� ����������� � ������.
"""


#default
#������ ������
list_output = []
element_buffer = 0
counter = -1
# input
#���� ������ � ��������
list= input().split()
# main
#������� ��������� �� ��������� ����� 1-��
for element in list:
    counter=-1
    for element_find in list:
        if counter == 1:
            break
        elif element == element_find:
            counter+=1
    if counter == 0:
        list_output.append(element)
# result
print(' '.join(list_output))


# -----------------------------------------------------------------


# task15------------------------------------------------------------
"""
N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. ����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � �������� �� li �� ri ������������. ����������, ����� ����� �������� ������ �� �����.
��������� �������� �� ���� ���������� ������ N � ���������� ������� K. ����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N.
��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ ���� �I�, ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����.
"""


#defaunt
list = []
# input
#���� ������ � ��������
list_instruction = input().split()
# main
for list_size in range(int(list_instruction[0])):
    list.append('I')
for number_kick in range (int(list_instruction[1])):
    list_kick = input().split()
    for index in range(int(list_kick[0])-1, int(list_kick[1]) ,1):
        list[index] = '.'
# result
print(''.join(list))

# -----------------------------------------------------------------

Contact GitHub API Training Shop Blog About
� 2016 GitHub, Inc. Terms Privacy Security Status Help