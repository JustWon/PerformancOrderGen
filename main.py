
import itertools
import numpy as np
import math


def pre_performance(p_order,cur_idx):
    if cur_idx-1 >= 0:
        return p_order[cur_idx-1]
    return []

def next_performance(p_order,cur_idx):
    if cur_idx+1 < len(p_order)-1:
        return p_order[cur_idx+1]
    return []

def cal_cost(p_order):

    cost = 0
    for idx, p in enumerate(p_order):
        for individual in p:
            if individual in pre_performance(p_order, idx):
                cost+=1
            if individual in next_performance(p_order, idx):
                cost+=1
    return cost, p_order


def print_best(people_list,sampling=100000):
    min_cost = np.inf
    min_order = []
    mypermuatations =  itertools.permutations(np.arange(len(people_list)))
    for idx, perm in enumerate(mypermuatations):

        if (idx % sampling==0 ):
            print(idx ,'/' , math.factorial(len(people_list)), '/' , idx/math.factorial(len(people_list)))

        cost, people_order = cal_cost(people_list[np.array(perm)])
        # print(cost,order)

        if cost < min_cost:
            min_cost = cost
            min_people_order = people_order
            min_title_order = title_list[np.array(perm)]

            print('\n cost:',min_cost)
            for idx, po in enumerate(min_people_order):
                print(min_title_order[idx], '\t', po)
            print('------------------------------------------------------------------------------------------------')

unicode_data = open('performance_list', 'rb').read().decode('utf8')
performances = unicode_data.split('\n')

people_list = []
title_list =[]
for p in performances:
    title, people, time = p.split('/')
    title_list.append(title)

    if len(people.split(',')) > 1:
        temp = [x.strip() for x in people.split(',')]
        # temp.remove('')
        people_list.append(temp)
    else:
        temp = [x.strip() for x in people.split(' ')]
        temp.remove('')
        people_list.append(temp)

title_list = np.array(title_list)
people_list = np.array(people_list)


# print(title_list)
# print(people_list)
# print(len(title_list))
# print(len(people_list))


print_best(people_list)