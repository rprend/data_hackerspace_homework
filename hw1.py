#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    parsed_list = []
    hour_list = [0] * 24
    with open(filename) as plane_crashes:
        row_reader = csv.reader(plane_crashes, delimiter='\n')
        parsed_list = list(row_reader)
    parsed_list = [x[0].split(',') for x in parsed_list]
    print(parsed_list[0])
    for x in parsed_list:
        try:
            print(x[1][:2])
            hour_list[int(x[1][:2])] += 1
        except:
            continue
    print(hour_list)

def weigh_pokemons(filename, weight):
    poke_json = {}
    name_list = []
    with open(filename) as pokemon_list:
        poke_json = json.load(pokemon_list)
    for x in poke_json['pokemon']:
        if (float(x['weight'].split(' ')[0]) == weight):
            name_list.append(x['name'])
    return(name_list)

def single_type_candy_count(filename):
    poke_json = {}
    sum_candy = 0
    with open(filename) as pokemon_list:
        poke_json = json.load(pokemon_list)
    for x in poke_json['pokemon']:
        if 'candy_count' in x:
            if len(x['type']) == 1:
                sum_candy += x['candy_count']
    return(sum_candy)

def reflections_and_projections(points):
    #Reflect over y = 1
    for idx,x in enumerate(points):
        if idx == 1:
            points[idx] = 1 - (x-1)
    #Rotates pi/2 about the origin
    rot_matrix = np.vstack((np.array([0, -1]),np.array([1, 0])))
    points = np.matmul(rot_matrix, points)
    #Projects onto the line y = 3x
    proj_matrix = (1/10) * np.vstack((np.array([1, 3]), np.array([3, 9])))
    points = np.matmul(proj_matrix, points)
    return points

def normalize(image):
    imageMax = np.amax(image)
    imageMin = np.amin(image)
    print(image - imageMin)
    image = (image-imageMin) * (255 / (imageMax - imageMin)) 
    return image

def sigmoid_normalize(image,a):
    import math
    return (255 * (1 + math.e ** ((-a) ** -1 * (image - 128))) ** -1).astype(int)