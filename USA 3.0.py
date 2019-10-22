from __future__ import division
import math
import locale

import numpy as np
import random
from random import randint
import copy
import time
#from matplotlib.pylab import *



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[98m'
    END = '\033[0m'

First_Names = ["Barack", "Rodrigo", "Dick", "Mitt", "Darrell", "Natalie", "Abigail", "Sarah", "Virginia", "Joan", "Alice", "Margaret", "Karen", "Cynthia", "Kimberly", "Diana", "Mary", "Patricia", "Jennifer", "Alexandria", "Ilhan", "Ayanna", "Xochitl", "Jesus", "Beto", "Newt", "Mitch", "Bill", "Donald", "John", "George", "Al", "Ronald", "Ron", "Gary","Steve", "Robert", "Alan", "Barry", "Jeff", "Julian", "Bernie", "Ted", "Marco", "Jeb", "Hilary", "Kirsten", "Rashida", "Sharice", "Cindy", "Maggie", "Tammy", "Elizabeth", "Steve", "Joseph", "Orrin", "Richard", "Lisa", "Dan", "Tom", "Barbara", "Cory", "Chris", "Mark", "Joni", "Angus", "Debbie", "Amy", "Thad", "Claire", "Roy", "Jon", "Ben", "Deanne", "Jeanne", "Kelly", "Thom", "Heidi", "Sherrod", "Sheldon", "Lindsey", "Lamar", "Bob", "Maria", "Patty", "Shelley", "Mike", "Earl"]
Last_Names = ["Obama", "Romney", "Cheney", "Issa", "Aderholt", "Grijalva", "Salmon", "Omar", "Ocasio-Cortez", "Garcia", "Pressley", "Davids", "Axne", "Tlaib", "McSally", "Goscar", "McClintock", "Lofgren", "Cardenas", "Farr", "Shiff", "Westmoreland", "Loudermilk", "Shimkus", "Ruppersberger", "Van Hollen", "McGovern", "Amash", "Walberg", "Amodei", "Titus", "Heck", "Watson Coleman", "Lujan Grisham", "Tonko", "Stefanik", "Katko", "Jackson Lee", "Vela", "Ribble", "Grothman", "Lummis",   "Gingrich", "McConnell", "Clinton", "Trump", "McCain", "Bush", "Gore", "Reagan","Johnson", "Portman", "Keyes", "Sessions", "Castro", "Sanders", "Cruz", "Rubio", "Gilibrand", "Hassan", "Duckworth", "Warren", "Shelby", "Capito", "Murkowski", "Sisolak", "Neguse", "Fast", "Lloyd", "Simmons", "Foster", "Hayes", "Diaz", "Gonzales", "Ramirez", "Rodriguez", "Bryant", "Griffin", "Watson", "Barnes", "Jenkins", "Aldag", "Wagner", "Hudson", "Bell", "Bailey", "Murphy", "Morris", "Rogers", "Reed", "Cook", "Coleman", "Woodhouse", "Key", "Upston", "Garrison", "Kwan", "Cormier", "Ambrose", "Kmiec", "Liepert", "Kang", "Eglinski", "Calkins", "Aboultaif", "Laxalt", "O'Rourke", "Torres Small", "Malinowski", "Slotkin", "Levin", "Sullivan", "Flake", "Cotton", "Feinstein", "Blumenthal", "Jones Jr", "Smith", "Murphy", "Coons", "Nelson", "King", "Isakson", "Gates", "Melvin", "Washington", "Sabato", "Silver", "Wang", "Crapo", "Hirono", "Carlsen", "Schumer", "Nakamura", "Blume", "Estevan", "Santana", "Svidler", "Escobar", "Aronian", "Risch", "Trout", "Sturgeon", "Salmon", "Grassley", "Williams", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Martinez", "Menedez", "Rodriguez", "Robinson", "Martin", "Hall", "Allan", "Peterson", "Butler", "Bryant", "Alexander", "Hayes", "Murray", "Freeman", "Wells", "Webb", "Morales", "Robinson", "Hunt", "Black", "Daniels", "Ray Tomblin"]

Native = {"Republican": 0.12, "Democrat": 0.6, "Independent": 0.28, "Education": 0.162, "Conservative": 0.33, "Moderate": 0.34, "Liberal": 0.33, "Turnout": 35}
Mormon = {"Republican": 0.7, "Democrat": 0.19, "Independent": 0.11, "Education": 0.273, "Conservative": 0.6, "Moderate": 0.32, "Liberal": 0.08, "Turnout": 75}
White = {"Republican": 0.36, "Democrat": 0.28, "Independent": 0.36, "Education": 0.362, "Conservative": 0.43, "Moderate": 0.37, "Liberal": 0.20, "Turnout": 65}
Black = {"Republican": 0.04, "Democrat": 0.72, "Independent": 0.24, "Education": 0.225, "Conservative": 0.24, "Moderate": 0.46, "Liberal": 0.30, "Turnout": 60}
Hispanic = {"Republican": 0.17, "Democrat": 0.50, "Independent": 0.33, "Education": 0.155, "Conservative": 0.34, "Moderate": 0.38, "Liberal": 0.23, "Turnout": 45}
Asian = {"Republican": 0.16, "Democrat": 0.42, "Independent": 0.42, "Education": 0.539, "Conservative": 0.21, "Moderate": 0.46, "Liberal": 0.31, "Turnout": 45}
Educated = {"Republican": 0.25, "Democrat": 0.36, "Independent": 0.39, "Conservative": 0.29, "Moderate": 0.36, "Liberal": 0.35, 'Turnout': 70}
Uneducated = {"Republican": 0.38, "Democrat": 0.32, "Independent": 0.30, "Conservative": 0.40, "Moderate": 0.36, "Liberal": 0.24, 'Turnout': 50}
Conservative = {"Republican": 0.62, "Democrat": 0.12, "Independent": 0.26}
Moderate = {"Republican": 0.24, "Democrat": 0.34, "Independent": 0.42}
Liberal = {"Republican": 0.06, "Democrat": 0.64, "Independent": 0.3}
Republican = {"Color": color.RED, 'Letter': "R", 'Native': -8, 'Mormon': +8, "Republican": +18, "Democrat": -18, "Independent": 0, "Conservative": +8, "Moderate": 0, "Liberal": -8, "Black": -16, "White": +4, "Hispanic": -6, "Asian": -8, "Degree": -3, "No Degree": +3}
Democrat = {"Color": color.BLUE, 'Letter': "D", 'Native': +8, 'Mormon': -8, "Republican": -18, "Democrat": +18, "Independent": 0, "Conservative": -8, "Moderate": 0, "Liberal": +8, "Black": +16, "White": -4, "Hispanic": +6, "Asian": +8, "Degree": +3, "No Degree": -3}
Independent = {"Color": color.BLACK, 'Letter': "I", 'Native': 0, 'Mormon': 0, "Republican": 0, "Democrat": 0, "Independent": 0, "Conservative": 0, "Moderate": 0, "Liberal": 0, "Black": 0, "White": 0, "Hispanic": 0, "Asian": 0, "Degree": 0, "No Degree": 0}
Urban = {"Republican": -5, "Democrat": +5, 'Native': -20, "Independent": 0, 'Mormon': -20, "Conservative": -10, "Moderate": 0, "Liberal": +10, "Black": +20, "White": -20, "Hispanic": +10, "Asian": +10, "Degree": +5, "No Degree": -5}
Suburban = {"Republican": -3, "Democrat": -3, 'Native': -10, "Independent": +6, 'Mormon': +10, "Conservative": +2, "Moderate": +2, "Liberal": -4, "Black": -10, "White": +10, "Hispanic": -5, "Asian": 0, "Degree": +15, "No Degree": -15}
Rural = {"Republican": +10, "Democrat": -5, "Independent": -5, 'Native': +30, 'Mormon': +20, "Conservative": +10, "Moderate": 0, "Liberal": -10, "Black": -20, "White": +20, "Hispanic": -10, "Asian": -10, "Degree": -20, "No Degree": +20}


Generic_R = {"Name": "Generic R", 'District Name Rec': 100, 'State Name Rec': 100, 'Nat Name Rec': 100, "District": 'WV-03', 'Momentum': 0, 'State': "West Virginia", "D+": 0, "S+": 0, "Party": "Republican", 'Native': 0, 'Mormon': 0, "Republican": 0, "Democrat": 0, "Independent": 0, "Conservative": 0, "Moderate": 0, "Liberal": 0, "Black": 0, "White": 0, "Hispanic": 0, "Asian": 0, "Degree": 0, "No Degree": 0}
Generic_D = {"Name": "Generic D", 'District Name Rec': 100, 'State Name Rec': 100, 'Nat Name Rec': 100, "District": 'WV-03', 'Momentum': 0, 'State': "West Virginia", "D+": 0, "S+": 0, "Party": "Democrat", 'Native': 0, 'Mormon': 0, "Republican": 0, "Democrat": 0, "Independent": 0, "Conservative": 0, "Moderate": 0, "Liberal": 0, "Black": 0, "White": 0, "Hispanic": 0, "Asian": 0, "Degree": 0, "No Degree": 0}
Generic_I = {"Name": "Generic I", 'District Name Rec': 100, 'State Name Rec': 100, 'Nat Name Rec': 100, "District": 'WV-03', 'Momentum': 0, 'State': "West Virginia", "D+": 0, "S+": 0, "Party": "Independent", 'Native': 0, 'Mormon': 0, "Republican": 0, "Democrat": 0, "Independent": 0, "Conservative": 0, "Moderate": 0, "Liberal": 0, "Black": 0, "White": 0, "Hispanic": 0, "Asian": 0, "Degree": 0, "No Degree": 0}

Modifier = {'Republican': 0, 'Democrat': 0, 'Independent': 0}
Results = {'Electoral Votes': {}, 'Popular Vote': {}, 'Generic Congressional Ballot': {}}

Amy_Klobuchar = {'Profile': 30, 'District Name Rec': 90, 'State Name Rec': 80, 'Nat Name Rec': 50, 'Momentum': 0, 'Age': 58, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Amy Klobuchar", 'Incumbent': True, "District": 'MN-03', 'State': "Minnesota", "D+": +7, "S+": +14, "Party": "Democrat", "Republican": +4, "Democrat": -2, "Independent": +2, "Conservative": +2, "Moderate": +4, "Liberal": -10, "Black": -2, 'Native': +1, "White": +2, 'Mormon': +4, "Hispanic": -4, "Asian": -4, "Degree": -1, "No Degree": -1}
Bernie_Sanders = {'Profile': 60, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 95, 'Momentum': 0, 'Age': 77, 'Senate Terms': 3, 'Terms': 1, 'Governor Terms': 0, "Name": "Bernie Sanders", 'Incumbent': True, "District": 'VT-AL', 'State': "Vermont", "D+": +5, "S+": +15, "Party": "Democrat", "Republican": -4, "Democrat": -2, "Independent": +5, "Conservative": -6, "Moderate": -2, "Liberal": +11, "Black": -2, 'Native': -4, "White": +4, 'Mormon': +3, "Hispanic": -1, "Asian": -2, "Degree": -4, "No Degree": +2}
Elizabeth_Warren = {'Profile': 40, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 80, 'Momentum': 0, 'Age': 69, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Elizabeth Warren", 'Incumbent': True, "District": 'MA-01', 'State': "Massachusetts", "D+": +2, "S+": +5, "Party": "Democrat", "Republican": -5, "Democrat": +5, "Independent": -3, "Conservative": -5, "Moderate": -3, "Liberal": +15, "Black": -3, 'Native': -10, "White": +4, 'Mormon': -6, "Hispanic": -3, "Asian": -1, "Degree": +12, "No Degree": -4}
Joe_Biden = {'Profile': 60, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 95, 'Momentum': 0, 'Age': 76, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Joe Biden", 'Incumbent': False, "District": 'DE-AL', 'State': "Delaware", "D+": +2, "S+": +10, "Party": "Democrat", "Republican": +2, "Democrat": -1, "Independent": +3, "Conservative": +7, "Moderate": +14, "Liberal": -10, "Black": +9, 'Native': -2, "White": +2, 'Mormon': +4, "Hispanic": -3, "Asian": -3, "Degree": -6, "No Degree": +5}
Beto_ORourke = {'Profile': 35, 'District Name Rec': 95, 'State Name Rec': 90, 'Nat Name Rec': 60, 'Momentum': 0, 'Age': 46, 'Senate Terms': 0, 'Terms': 2, 'Governor Terms': 0, "Name": "Beto O'Rourke", 'Incumbent': False, "District": 'TX-10', 'State': "Texas", "D+": +10, "S+": +7, "Party": "Democrat", "Republican": -2, "Democrat": +2, "Independent": +3, "Conservative": -2, "Moderate": +2, "Liberal": -1, "Black": +1, 'Native': +2, "White": -2, 'Mormon': -1, "Hispanic": +8, "Asian": +1, "Degree": +4, "No Degree": -3}
Kamala_Harris = {'Profile': 40, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 75, 'Momentum': 0, 'Age': 54, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Kamala Harris", 'Incumbent': True, "District": 'CA-25', 'State': "California", "D+": +2, "S+": +10, "Party": "Democrat", "Republican": -3, "Democrat": +4, "Independent": -1, "Conservative": -2, "Moderate": -1, "Liberal": +6, "Black": +2, 'Native': +2, "White": -1, 'Mormon': -3, "Hispanic": +5, "Asian": +5, "Degree": +6, "No Degree": -2}
Joe_Manchin = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 71, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "Joe Manchin", 'Incumbent': True, "District": 'WV-01', 'State': "West Virginia", "D+": +10, "S+": +25, "Party": "Democrat", "Republican": +4, "Democrat": -3, "Independent": +1, "Conservative": +5, "Moderate": +3, "Liberal": -5, "Black": -6, "White": +4, 'Native': -5, "Hispanic": -5, 'Mormon': +2, "Asian": -3, "Degree": -2, "No Degree": +3}
Alexandra_Cortez = {'Profile': 20, 'District Name Rec': 85, 'State Name Rec': 70, 'Nat Name Rec': 50, 'Momentum': 0, 'Age': 29, 'Senate Terms': 0, 'Terms': 1, 'Governor Terms': 0, "Name": "Alexandra Ocasio-Cortez", 'Incumbent': True, "District": 'NY-25', 'State': "New York", "D+": +10, "S+": +3, "Party": "Democrat", "Republican": -10, "Democrat": +6, "Independent": -2, "Conservative": -10, "Moderate": -6, "Liberal": +15, "Black": +3, 'Native': +3, "White": -5, 'Mormon': -5, "Hispanic": +6, "Asian": +1, "Degree": +6, "No Degree": -3}
Doug_Jones = {'Profile': 10, 'District Name Rec': 85, 'State Name Rec': 85, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 64, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Doug Jones", 'Incumbent': True, "District": 'AL-01', 'State': "Alabama", "D+": +2, "S+": +8, "Party": "Democrat", "Republican": +2, "Democrat": -2, "Independent": +4, "Conservative": +1, "Moderate": +6, "Liberal": -2, "Black": +5, "White": +5, 'Native': -3, "Hispanic": -3, 'Mormon': +5, "Asian": -3, "Degree": +3, "No Degree": -1}
Jon_Tester = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 62, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "Jon Tester", 'Incumbent': True, "District": 'MT-AL', 'State': "Montana", "D+": +1, "S+": +18, "Party": "Democrat", "Republican": +4, "Democrat": -4, "Independent": +6, "Conservative": +4, "Moderate": +4, "Liberal": -4, "Black": -5, "White": +5, 'Native': +5, "Hispanic": -5, 'Mormon': +5, "Asian": -5, "Degree": +1, "No Degree": +1}
Laura_Kelly = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 90, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 68, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 1, "Name": "Laura Kelly", 'Incumbent': True, "District": 'KS-04', 'State': "Kansas", "D+": +3, "S+": +15, "Party": "Democrat", "Republican": +6, "Democrat": -2, "Independent": +4, "Conservative": +6, "Moderate": +4, "Liberal": -5, "Black": -6, "White": +6, 'Native': +2, "Hispanic": -6, 'Mormon': +7, "Asian": -6, "Degree": +6, "No Degree": -2}
Roy_Cooper = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 90, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 61, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 1, "Name": "Roy Cooper", 'Incumbent': True, "District": 'NC-04', 'State': "North Carolina", "D+": +6, "S+": +15, "Party": "Democrat", "Republican": +2, "Democrat": -1, "Independent": +5, "Conservative": +2, "Moderate": +4, "Liberal": -2, "Black": +2, "White": +4, 'Native': -3, "Hispanic": +1, 'Mormon': +2, "Asian": -3, "Degree": +6, "No Degree": -2}
Krysten_Sinema = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 90, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 42, 'Senate Terms': 1, 'Terms': 2, 'Governor Terms': 0, "Name": "Krysten Sinema", 'Incumbent': True, "District": 'AZ-02', 'State': "Arizona", "D+": +8, "S+": +10, "Party": "Democrat", "Republican": +4, "Democrat": -2, "Independent": +5, "Conservative": +3, "Moderate": +6, "Liberal": -2, "Black": -3, "White": +3, 'Native': +2, "Hispanic": +7, 'Mormon': +3, "Asian": -2, "Degree": +5, "No Degree": -2}
Sherrod_Brown = {'Profile': 25, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 60, 'Momentum': 0, 'Age': 66, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Sherrod Brown", 'Incumbent': True, "District": 'OH-01', 'State': "Ohio", "D+": +4, "S+": +12, "Party": "Democrat", "Republican": -1, "Democrat": +2, "Independent": +4, "Conservative": -1, "Moderate": +3, "Liberal": +3, "Black": +2, 'Native': -5, "White": +4, 'Mormon': +3, "Hispanic": -4, "Asian": -4, "Degree": -4, "No Degree": +2}
Ralph_Northam = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 59, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 2, "Name": "Ralph Northam", 'Incumbent': True, "District": 'VA-05', 'State': "Virginia", "D+": +3, "S+": +10, "Party": "Democrat", "Republican": +3, "Democrat": -2, "Independent": +5, "Conservative": +3, "Moderate": +5, "Liberal": -3, "Black": +2, "White": +4, 'Native': -5, "Hispanic": +3, 'Mormon': +2, "Asian": -4, "Degree": +5, "No Degree": -2}
John_Edwards = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 52, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 1, "Name": "John Bel Edwards", 'Incumbent': True, "District": 'LA-01', 'State': "Louisiana", "D+": +3, "S+": +8, "Party": "Democrat", "Republican": +2, "Democrat": -2, "Independent": +3, "Conservative": +3, "Moderate": +5, "Liberal": -7, "Black": 0, "White": +6, 'Native': -5, "Hispanic": -6, 'Mormon': +2, "Asian": -6, "Degree": -3, "No Degree": +2}
Tony_Evers = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 67, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 1, "Name": "Tony Evers", 'Incumbent': True, "District": 'WI-02', 'State': "Wisconsin", "D+": +3, "S+": +10, "Party": "Democrat", "Republican": +1, "Democrat": 0, "Independent": +2, "Conservative": +2, "Moderate": +3, "Liberal": -2, "Black": +2, "White": +4, 'Native': -1, "Hispanic": +3, 'Mormon': +2, "Asian": -2, "Degree": +2, "No Degree": -1}
Tom_Wolf = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 70, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 2, "Name": "Tom Wolf", 'Incumbent': True, "District": 'PA-03', 'State': "Pennsylvania", "D+": +3, "S+": +10, "Party": "Democrat", "Republican": +3, "Democrat": -2, "Independent": +5, "Conservative": +3, "Moderate": +5, "Liberal": -3, "Black": +2, "White": +4, 'Native': -5, "Hispanic": +3, 'Mormon': +2, "Asian": -4, "Degree": +5, "No Degree": -2}
Tim_Kaine = {'Profile': 30, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 55, 'Momentum': 0, 'Age': 60, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 1, "Name": "Tim Kaine", 'Incumbent': True, "District": 'VA-03', 'State': "Virginia", "D+": +3, "S+": +12, "Party": "Democrat", "Republican": +1, "Democrat": -1, "Independent": +1, "Conservative": +1, "Moderate": +5, "Liberal": -1, "Black": +2, "White": +2, 'Native': -2, "Hispanic": +6, 'Mormon': 0, "Asian": -2, "Degree": +5, "No Degree": -2}
Tammy_Baldwin = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 56, 'Senate Terms': 2, 'Terms': 5, 'Governor Terms': 0, "Name": "Tammy Baldwin", 'Incumbent': True, "District": 'WI-03', 'State': "Wisconsin", "D+": +10, "S+": +12, "Party": "Democrat", "Republican": -2, "Democrat": +3, "Independent": +2, "Conservative": -2, "Moderate": +2, "Liberal": +5, "Black": +1, "White": -1, 'Native': +1, "Hispanic": +1, 'Mormon': +2, "Asian": +1, "Degree": +2, "No Degree": -1}
Jacky_Rosen = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 61, 'Senate Terms': 1, 'Terms': 2, 'Governor Terms': 0, "Name": "Jacky Rosen", 'Incumbent': True, "District": 'NV-03', 'State': "Nevada", "D+": +8, "S+": +8, "Party": "Democrat", "Republican": -1, "Democrat": +1, "Independent": +1, "Conservative": -1, "Moderate": +2, "Liberal": 0, "Black": -2, "White": +2, 'Native': -2, "Hispanic": +4, 'Mormon': +2, "Asian": -2, "Degree": +3, "No Degree": -1}
Maria_Cantwell = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 60, 'Senate Terms': 3, 'Terms': 1, 'Governor Terms': 0, "Name": "Maria Cantwell", 'Incumbent': True, "District": 'WA-01', 'State': "Washington", "D+": +6, "S+": +8, "Party": "Democrat", "Republican": -2, "Democrat": +2, "Independent": 0, "Conservative": -1, "Moderate": +1, "Liberal": +1, "Black": -2, "White": +1, 'Native': -1, "Hispanic": -1, 'Mormon': 0, "Asian": -1, "Degree": +5, "No Degree": -2}
Bob_Casey = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 58, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Bob Casey Jr", 'Incumbent': True, "District": 'PA-05', 'State': "Pennsylvania", "D+": +5, "S+": +12, "Party": "Democrat", "Republican": -1, "Democrat": +2, "Independent": +5, "Conservative": -1, "Moderate": +2, "Liberal": +1, "Black": +1, "White": +4, 'Native': -5, "Hispanic": -2, 'Mormon': +2, "Asian": -4, "Degree": -2, "No Degree": +1}
Sheldon_Whitehouse = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 63, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Sheldon Whitehouse", 'Incumbent': True, "District": 'RI-01', 'State': "Rhode Island", "D+": +2, "S+": +8, "Party": "Democrat", "Republican": -1, "Democrat": +2, "Independent": +4, "Conservative": -1, "Moderate": +2, "Liberal": +3, "Black": +3, 'Native': -2, "White": +2, 'Mormon': +1, "Hispanic": -2, "Asian": -2, "Degree": -1, "No Degree": +1}
Debbie_Stabenow = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 68, 'Senate Terms': 3, 'Terms': 5, 'Governor Terms': 0, "Name": "Debbie Stabenow", 'Incumbent': True, "District": 'MI-08', 'State': "Michigan", "D+": +8, "S+": +6, "Party": "Democrat", "Republican": -1, "Democrat": -1, "Independent": +3, "Conservative": -3, "Moderate": +3, "Liberal": -2, "Black": -3, "White": +2, 'Native': -3, "Hispanic": -3, 'Mormon': +2, "Asian": -4, "Degree": -2, "No Degree": +1}
Martin_Heinrich = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 47, 'Senate Terms': 2, 'Terms': 2, 'Governor Terms': 0, "Name": "Martin Heinrich", 'Incumbent': True, "District": 'NM-03', 'State': "New Mexico", "D+": +8, "S+": +10, "Party": "Democrat", "Republican": -2, "Democrat": +3, "Independent": 0, "Conservative": -1, "Moderate": 0, "Liberal": +3, "Black": -2, "White": +1, 'Native': +4, "Hispanic": +6, 'Mormon': +2, "Asian": -2, "Degree": +5, "No Degree": -2}
Chris_Murphy = {'Profile': 25, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 45, 'Senate Terms': 2, 'Terms': 3, 'Governor Terms': 0, "Name": "Chris Murphy", 'Incumbent': True, "District": 'CT-05', 'State': "Connecticut", "D+": +3, "S+": +10, "Party": "Democrat", "Republican": -5, "Democrat": +3, "Independent": +1, "Conservative": -5, "Moderate": -2, "Liberal": +7, "Black": +3, 'Native': +2, "White": -2, 'Mormon': -2, "Hispanic": +3, "Asian": +3, "Degree": +5, "No Degree": -2}
Tom_Carper = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 71, 'Senate Terms': 3, 'Terms': 5, 'Governor Terms': 2, "Name": "Tom Carper", 'Incumbent': True, "District": 'DE-AL', 'State': "Delaware", "D+": +5, "S+": +15, "Party": "Democrat", "Republican": +2, "Democrat": -2, "Independent": +3, "Conservative": +2, "Moderate": +2, "Liberal": -3, "Black": -5, "White": +4, 'Native': -5, "Hispanic": -5, 'Mormon': +2, "Asian": -5, "Degree": 0, "No Degree": 0}
Bob_Menendez = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 65, 'Momentum': 0, 'Age': 65, 'Senate Terms': 3, 'Terms': 6, 'Governor Terms': 0, "Name": "Bob Menendez", 'Incumbent': True, "District": 'NJ-13', 'State': "New Jersey", "D+": +7, "S+": -2, "Party": "Democrat", "Republican": -3, "Democrat": -5, "Independent": -5, "Conservative": -3, "Moderate": -5, "Liberal": -5, "Black": -3, "White": -7, 'Native': -5, "Hispanic": -5, 'Mormon': -3, "Asian": -5, "Degree": -5, "No Degree": -2}
Jeanne_Shaheen = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 71, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "Jeanne Shaheen", 'Incumbent': True, "District": 'NH-01', 'State': "New Hampshire", "D+": +2, "S+": +10, "Party": "Democrat", "Republican": +1, "Democrat": -1, "Independent": +4, "Conservative": -1, "Moderate": +3, "Liberal": +1, "Black": +3, 'Native': -2, "White": +2, 'Mormon': +1, "Hispanic": -2, "Asian": -2, "Degree": +3, "No Degree": -1}
Jeff_Merkley = {'Profile': 25, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 60, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Jeff Merkley", 'Incumbent': True, "District": 'OR-05', 'State': "Oregon", "D+": +2, "S+": +10, "Party": "Democrat", "Republican": -5, "Democrat": +6, "Independent": -1, "Conservative": -5, "Moderate": -3, "Liberal": +8, "Black": +1, 'Native': +2, "White": -2, 'Mormon': -2, "Hispanic": +3, "Asian": +5, "Degree": +5, "No Degree": -2}
Mark_Warner = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 64, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 1, "Name": "Mark Warner", 'Incumbent': True, "District": 'VA-05', 'State': "Virginia", "D+": +3, "S+": +12, "Party": "Democrat", "Republican": +1, "Democrat": -1, "Independent": +1, "Conservative": +1, "Moderate": +5, "Liberal": -1, "Black": +2, "White": +2, 'Native': -2, "Hispanic": +6, 'Mormon': 0, "Asian": -2, "Degree": +5, "No Degree": -2}
Jack_Reed = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 69, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Jack Reed", 'Incumbent': True, "District": 'RI-02', 'State': "Rhode Island", "D+": +8, "S+": +8, "Party": "Democrat", "Republican": +3, "Democrat": -1, "Independent": +4, "Conservative": +2, "Moderate": +2, "Liberal": -1, "Black": -3, 'Native': -2, "White": +5, 'Mormon': +1, "Hispanic": -2, "Asian": -2, "Degree": -1, "No Degree": +1}
Cory_Booker = {'Profile': 35, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 65, 'Momentum': 0, 'Age': 49, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Cory Booker", 'Incumbent': True, "District": 'NJ-01', 'State': "New Jersey", "D+": +2, "S+": +10, "Party": "Democrat", "Republican": -3, "Democrat": +2, "Independent": +1, "Conservative": -2, "Moderate": +1, "Liberal": -2, "Black": +5, 'Native': +2, "White": -2, 'Mormon': -3, "Hispanic": +3, "Asian": +3, "Degree": +4, "No Degree": -3}
Tom_Udall = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 70, 'Senate Terms': 2, 'Terms': 5, 'Governor Terms': 0, "Name": "Tom Udall", 'Incumbent': True, "District": 'NM-03', 'State': "New Mexico", "D+": +8, "S+": +8, "Party": "Democrat", "Republican": -1, "Democrat": +2, "Independent": +1, "Conservative": 0, "Moderate": +1, "Liberal": +1, "Black": -2, "White": +2, 'Native': +2, "Hispanic": +2, 'Mormon': +2, "Asian": -2, "Degree": 0, "No Degree": 0}
Chris_Coons = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 55, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Chris Coons", 'Incumbent': True, "District": 'DE-AL', 'State': "Delaware", "D+": +5, "S+": +8, "Party": "Democrat", "Republican": 0, "Democrat": 0, "Independent": +5, "Conservative": 0, "Moderate": +5, "Liberal": 0, "Black": +1, "White": +1, 'Native': -5, "Hispanic": -5, 'Mormon': 0, "Asian": -5, "Degree": 0, "No Degree": 0}
Dick_Durbin = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 74, 'Senate Terms': 4, 'Terms': 7, 'Governor Terms': 0, "Name": "Dick Durbin", 'Incumbent': True, "District": 'IL-20', 'State': "Illinois", "D+": +12, "S+": +10, "Party": "Democrat", "Republican": +1, "Democrat": -2, "Independent": +4, "Conservative": +1, "Moderate": +4, "Liberal": -1, "Black": +3, "White": -1, 'Native': -5, "Hispanic": -5, 'Mormon': 0, "Asian": -5, "Degree": 0, "No Degree": 0}
Gary_Peters = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 60, 'Senate Terms': 1, 'Terms': 3, 'Governor Terms': 0, "Name": "Gary Peters", 'Incumbent': True, "District": 'MI-14', 'State': "Michigan", "D+": +8, "S+": +10, "Party": "Democrat", "Republican": +2, "Democrat": -1, "Independent": +3, "Conservative": +1, "Moderate": +3, "Liberal": -2, "Black": +3, "White": +1, 'Native': -3, "Hispanic": -3, 'Mormon': +2, "Asian": -4, "Degree": -2, "No Degree": +1}
Tina_Smith = {'Profile': 15, 'District Name Rec': 90, 'State Name Rec': 80, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 60, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Tina Smith", 'Incumbent': True, "District": 'MN-03', 'State': "Minnesota", "D+": +1, "S+": +10, "Party": "Democrat", "Republican": -1, "Democrat": +1, "Independent": +2, "Conservative": -1, "Moderate": +3, "Liberal": -2, "Black": 0, 'Native': +1, "White": +3, 'Mormon': +3, "Hispanic": -4, "Asian": -4, "Degree": 0, "No Degree": 0}
Catherine_Masto = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 54, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Catherine Cortez Masto", 'Incumbent': True, "District": 'NV-02', 'State': "Nevada", "D+": +2, "S+": +11, "Party": "Democrat", "Republican": -2, "Democrat": +3, "Independent": +1, "Conservative": -1, "Moderate": +1, "Liberal": +2, "Black": +1, "White": -1, 'Native': -2, "Hispanic": +7, 'Mormon': 0, "Asian": +2, "Degree": +5, "No Degree": -2}
Maggie_Hassan = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 60, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 2, "Name": "Maggie Hassan", 'Incumbent': True, "District": 'NH-02', 'State': "New Hampshire", "D+": +3, "S+": +12, "Party": "Democrat", "Republican": +3, "Democrat": -1, "Independent": +4, "Conservative": +2, "Moderate": +3, "Liberal": -1, "Black": +1, 'Native': -2, "White": +3, 'Mormon': +2, "Hispanic": -2, "Asian": -2, "Degree": +3, "No Degree": -1}
Michael_Bennet = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 54, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Michael Bennet", 'Incumbent': True, "District": 'CO-05', 'State': "Colorado", "D+": +1, "S+": +10, "Party": "Democrat", "Republican": +1, "Democrat": -1, "Independent": +1, "Conservative": +1, "Moderate": +3, "Liberal": -1, "Black": +1, "White": +1, 'Native': -2, "Hispanic": +6, 'Mormon': -1, "Asian": -2, "Degree": +5, "No Degree": -2}
Richard_Blumenthal = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 72, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Richard Blumenthal", 'Incumbent': True, "District": 'CT-01', 'State': "Connecticut", "D+": +2, "S+": +9, "Party": "Democrat", "Republican": -1, "Democrat": +2, "Independent": +4, "Conservative": -1, "Moderate": +2, "Liberal": +3, "Black": +3, 'Native': -2, "White": +2, 'Mormon': +1, "Hispanic": -2, "Asian": -2, "Degree": 0, "No Degree": 0}
Tammy_Duckworth = {'Profile': 25, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 50, 'Senate Terms': 1, 'Terms': 2, 'Governor Terms': 0, "Name": "Tammy Duckworth", 'Incumbent': True, "District": 'IL-08', 'State': "Illinois", "D+": +8, "S+": +10, "Party": "Democrat", "Republican": -2, "Democrat": +3, "Independent": +3, "Conservative": -2, "Moderate": +1, "Liberal": +3, "Black": +3, "White": -3, 'Native': -5, "Hispanic": -3, 'Mormon': 0, "Asian": +10, "Degree": 0, "No Degree": 0}
Ron_Wyden = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 69, 'Senate Terms': 4, 'Terms': 6, 'Governor Terms': 0, "Name": "Ron Wyden", 'Incumbent': True, "District": 'OR-03', 'State': "Oregon", "D+": +8, "S+": +8, "Party": "Democrat", "Republican": -4, "Democrat": +5, "Independent": -2, "Conservative": -4, "Moderate": +1, "Liberal": +5, "Black": -1, 'Native': -1, "White": +1, 'Mormon': +1, "Hispanic": -1, "Asian": -1, "Degree": 0, "No Degree": 0}
Patty_Murray = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 68, 'Senate Terms': 5, 'Terms': 2, 'Governor Terms': 0, "Name": "Patty Murray", 'Incumbent': True, "District": 'WA-01', 'State': "Washington", "D+": +6, "S+": +10, "Party": "Democrat", "Republican": -3, "Democrat": +4, "Independent": -1, "Conservative": -2, "Moderate": -1, "Liberal": +4, "Black": -2, "White": +1, 'Native': -1, "Hispanic": -1, 'Mormon': 0, "Asian": -1, "Degree": +5, "No Degree": -2}
Kirsten_Gillibrand = {'Profile': 30, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 52, 'Senate Terms': 2, 'Terms': 1, 'Governor Terms': 0, "Name": "Kirsten Gillibrand", 'Incumbent': True, "District": 'NY-20', 'State': "New York", "D+": +7, "S+": +12, "Party": "Democrat", "Republican": -3, "Democrat": +1, "Independent": -2, "Conservative": -2, "Moderate": +1, "Liberal": -1, "Black": 0, 'Native': +2, "White": +1, 'Mormon': +1, "Hispanic": +2, "Asian": +2, "Degree": -1, "No Degree": -4}
Tim_Walz = {'Profile': 20, 'District Name Rec': 90, 'State Name Rec': 80, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 54, 'Senate Terms': 0, 'Terms': 6, 'Governor Terms': 1, "Name": "Tim Walz", 'Incumbent': True, "District": 'MN-03', 'State': "Minnesota", "D+": +8, "S+": +9, "Party": "Democrat", "Republican": +4, "Democrat": -1, "Independent": +2, "Conservative": +2, "Moderate": +3, "Liberal": -3, "Black": +1, 'Native': +1, "White": +4, 'Mormon': +4, "Hispanic": -2, "Asian": -2, "Degree": +2, "No Degree": -1}
Gretchen_Whitmer = {'Profile': 20, 'District Name Rec': 90, 'State Name Rec': 80, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 47, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 1, "Name": "Gretchen Whitmer", 'Incumbent': True, "District": 'MI-03', 'State': "Michigan", "D+": +3, "S+": +12, "Party": "Democrat", "Republican": +2, "Democrat": -1, "Independent": +1, "Conservative": +1, "Moderate": +1, "Liberal": -1, "Black": +3, 'Native': +1, "White": +3, 'Mormon': +4, "Hispanic": -2, "Asian": -2, "Degree": +5, "No Degree": -2}
Pete_Buttigieg = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 80, 'Nat Name Rec': 55, 'Momentum': 0, 'Age': 37, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 0, "Name": "Pete Buttigieg", 'Incumbent': False, "District": 'IN-03', 'State': "Indiana", "D+": +14, "S+": +4, "Party": "Democrat", "Republican": -3, "Democrat": +3, "Independent": +1, "Conservative": -6, "Moderate": -4, "Liberal": +5, "Black": -9, 'Native': -1, "White": +4, 'Mormon': -5, "Hispanic": -3, "Asian": -3, "Degree": +8, "No Degree": -5}
Julian_Castro = {'Profile': 8, 'District Name Rec': 85, 'State Name Rec': 60, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 44, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 0, "Name": "Julian Castro", 'Incumbent': False, "District": 'TX-14', 'State': "Texas", "D+": +10, "S+": +3, "Party": "Democrat", "Republican": -3, "Democrat": +3, "Independent": -2, "Conservative": -2, "Moderate": +4, "Liberal": +1, "Black": +1, 'Native': +2, "White": -4, 'Mormon': -3, "Hispanic": +12, "Asian": +1, "Degree": +4, "No Degree": -3}
Andrew_Yang = {'Profile': 6, 'District Name Rec': 50, 'State Name Rec': 45, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 44, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 0, "Name": "Andrew Yang", 'Incumbent': False, "District": 'CA-07', 'State': "California", "D+": +1, "S+": +3, "Party": "Democrat", "Republican": -2, "Democrat": -4, "Independent": +5, "Conservative": +3, "Moderate": +5, "Liberal": -4, "Black": -8, 'Native': -5, "White": +5, 'Mormon': +2, "Hispanic": -5, "Asian": +10, "Degree": -5, "No Degree": +2}


Angus_King = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 74, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 2, "Name": "Angus King", 'Incumbent': True, "District": 'ME-02', 'State': "Maine", "D+": +5, "S+": +12, "Party": "Independent", "Republican": -4, "Democrat": +6, "Independent": +8, "Conservative": -2, "Moderate": +6, "Liberal": +3, "Black": -6, "White": +6, 'Native': -5, "Hispanic": -5, 'Mormon': +2, "Asian": -3, "Degree": +5, "No Degree": -2}


Donald_Trump = {'Profile': 100, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 95, 'Momentum': 0, 'Pres Terms': 1, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 0, 'Age': 72, "Name": "Donald Trump", 'Incumbent': True, "District": 'NY-01', 'State': "New York", "D+": 0, "S+": +5, "Party": "Republican", "Republican": +4, "Democrat": -2, "Independent": -3, "Conservative": +2, "Moderate": 0, "Liberal": -3, "Black": -7, 'Native': -10, "White": +5, "Hispanic": -7, 'Mormon': -30, "Asian": -7, "Degree": -8, "No Degree": +5}
Susan_Collins = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 50, 'Momentum': 0, 'Age': 66, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "Susan Collins", 'Incumbent': True, "District": 'ME-01', 'State': "Maine", "D+": +1, "S+": +10, "Party": "Republican", "Republican": -2, "Democrat": +4, "Independent": +5, "Conservative": -3, "Moderate": +3, "Liberal": +1, "Black": -4, "White": +3, 'Native': -3, "Hispanic": -3, 'Mormon': +2, "Asian": -3, "Degree": +2, "No Degree": -1}
Larry_Hogan = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 62, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 2, "Name": "Larry Hogan", 'Incumbent': True, "District": 'MD-02', 'State': "Maryland", "D+": +5, "S+": +20, "Party": "Republican", "Republican": -5, "Democrat": +6, "Independent": +5, "Conservative": -3, "Moderate": +6, "Liberal": +3, "Black": +4, "White": +2, 'Native': +2, "Hispanic": +2, 'Mormon': +2, "Asian": -3, "Degree": +5, "No Degree": -2}
Charlie_Baker = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 62, 'Senate Terms': 0, 'Terms': 0, 'Governor Terms': 2, "Name": "Charlie Baker", 'Incumbent': True, "District": 'MA-01', 'State': "Massachusetts", "D+": +5, "S+": +25, "Party": "Republican", "Republican": -5, "Democrat": +6, "Independent": +5, "Conservative": -3, "Moderate": +6, "Liberal": +4, "Black": +4, "White": +2, 'Native': +2, "Hispanic": +2, 'Mormon': +2, "Asian": -3, "Degree": +5, "No Degree": -2}
Cory_Gardner = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 44, 'Senate Terms': 1, 'Terms': 2, 'Governor Terms': 0, "Name": "Cory Gardner", 'Incumbent': True, "District": 'CO-03', 'State': "Colorado", "D+": +5, "S+": +6, "Party": "Republican", "Republican": +4, "Democrat": -5, "Independent": -2, "Conservative": +3, "Moderate": -2, "Liberal": -5, "Black": -2, "White": -1, 'Native': -2, "Hispanic": +1, 'Mormon': +3, "Asian": -1, "Degree": -1, "No Degree": 0}
Thom_Tillis = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 58, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Thom Tillis", 'Incumbent': True, "District": 'NC-05', 'State': "North Carolina", "D+": +2, "S+": +8, "Party": "Republican", "Republican": +3, "Democrat": -3, "Independent": 0, "Conservative": +2, "Moderate": -1, "Liberal": -4, "Black": -1, "White": +1, 'Native': -2, "Hispanic": -2, 'Mormon': +2, "Asian": -1, "Degree": +2, "No Degree": -1}
John_Cornyn = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 66, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "John Cornyn", 'Incumbent': True, "District": 'TX-12', 'State': "Texas", "D+": +2, "S+": +10, "Party": "Republican", "Republican": +4, "Democrat": -3, "Independent": -1, "Conservative": +3, "Moderate": -2, "Liberal": -4, "Black": -2, "White": +1, 'Native': -2, "Hispanic": +1, 'Mormon': +3, "Asian": -1, "Degree": 0, "No Degree": 0}
Joni_Ernst = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 48, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Joni Ernst", 'Incumbent': True, "District": 'IA-03', 'State': "Iowa", "D+": +2, "S+": +10, "Party": "Republican", "Republican": +5, "Democrat": -3, "Independent": 0, "Conservative": +5, "Moderate": -1, "Liberal": -4, "Black": -2, "White": +3, 'Native': -2, "Hispanic": -2, 'Mormon': +3, "Asian": -1, "Degree": -5, "No Degree": +2}
David_Perdue = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 69, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "David Perdue", 'Incumbent': True, "District": 'GA-05', 'State': "Georgia", "D+": +2, "S+": +7, "Party": "Republican", "Republican": +3, "Democrat": -3, "Independent": -1, "Conservative": +2, "Moderate": -1, "Liberal": -4, "Black": -2, "White": +1, 'Native': -2, "Hispanic": -3, 'Mormon': +2, "Asian": -1, "Degree": 0, "No Degree": 0}
Steve_Daines = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 56, 'Senate Terms': 1, 'Terms': 1, 'Governor Terms': 0, "Name": "Steve Daines", 'Incumbent': True, "District": 'MT-AL', 'State': "Montana", "D+": +2, "S+": +9, "Party": "Republican", "Republican": +2, "Democrat": -1, "Independent": -1, "Conservative": +2, "Moderate": -2, "Liberal": -3, "Black": -2, "White": +2, 'Native': -3, "Hispanic": -3, 'Mormon': +3, "Asian": -1, "Degree": -2, "No Degree": +1}
Cindy_Smith = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 59, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Cindy Hyde-Smith", 'Incumbent': True, "District": 'MS-02', 'State': "Mississippi", "D+": +2, "S+": +7, "Party": "Republican", "Republican": +1, "Democrat": -3, "Independent": -2, "Conservative": +3, "Moderate": -2, "Liberal": -4, "Black": -6, "White": +2, 'Native': -2, "Hispanic": -3, 'Mormon': -2, "Asian": -1, "Degree": -5, "No Degree": +1}
Marco_Rubio = {'Profile': 35, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 60, 'Momentum': 0, 'Age': 47, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Marco Rubio", 'Incumbent': True, "District": 'FL-20', 'State': "Florida", "D+": +2, "S+": +7, "Party": "Republican", "Republican": +2, "Democrat": -2, "Independent": -1, "Conservative": +3, "Moderate": -2, "Liberal": -3, "Black": -2, "White": -2, 'Native': -2, "Hispanic": +3, 'Mormon': +5, "Asian": -2, "Degree": +2, "No Degree": -1}
Rick_Scott = {'Profile': 25, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 50, 'Momentum': 0, 'Age': 66, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 2, "Name": "Rick Scott", 'Incumbent': True, "District": 'FL-17', 'State': "Florida", "D+": +2, "S+": +12, "Party": "Republican", "Republican": -1, "Democrat": +2, "Independent": +2, "Conservative": +2, "Moderate": +1, "Liberal": -3, "Black": -1, "White": +1, 'Native': -2, "Hispanic": +4, 'Mormon': +5, "Asian": -2, "Degree": 0, "No Degree": 0}
Rob_Portman = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 63, 'Senate Terms': 2, 'Terms': 6, 'Governor Terms': 0, "Name": "Rob Portman", 'Incumbent': True, "District": 'OH-02', 'State': "Ohio", "D+": +6, "S+": +11, "Party": "Republican", "Republican": -3, "Democrat": +4, "Independent": +3, "Conservative": -2, "Moderate": +4, "Liberal": -1, "Black": +3, "White": -2, 'Native': +2, "Hispanic": +2, 'Mormon': +2, "Asian": +2, "Degree": +5, "No Degree": -2}
Ron_Johnson = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 63, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Ron Johnson", 'Incumbent': True, "District": 'WI-02', 'State': "Wisconsin", "D+": +2, "S+": +10, "Party": "Republican", "Republican": +3, "Democrat": -4, "Independent": +1, "Conservative": +5, "Moderate": -2, "Liberal": -3, "Black": -3, "White": +4, 'Native': -3, "Hispanic": -3, 'Mormon': +3, "Asian": -3, "Degree": 0, "No Degree": 0}
Pat_Toomey = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 57, 'Senate Terms': 2, 'Terms': 3, 'Governor Terms': 0, "Name": "Pat Toomey", 'Incumbent': True, "District": 'PA-15', 'State': "Pennsylvania", "D+": +5, "S+": +7, "Party": "Republican", "Republican": +2, "Democrat": -2, "Independent": -1, "Conservative": +2, "Moderate": -2, "Liberal": -3, "Black": -1, "White": +1, 'Native': -2, "Hispanic": +1, 'Mormon': +3, "Asian": -1, "Degree": 0, "No Degree": 0}
Richard_Burr = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 58, 'Senate Terms': 3, 'Terms': 5, 'Governor Terms': 0, "Name": "Richard Burr", 'Incumbent': True, "District": 'NC-05', 'State': "North Carolina", "D+": +5, "S+": +10, "Party": "Republican", "Republican": -3, "Democrat": +3, "Independent": +2, "Conservative": -1, "Moderate": +1, "Liberal": +2, "Black": +2, "White": -1, 'Native': +1, "Hispanic": +1, 'Mormon': +2, "Asian": +1, "Degree": +2, "No Degree": -1}
Chuck_Grassley = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 85, 'Senate Terms': 6, 'Terms': 3, 'Governor Terms': 0, "Name": "Chuck Grassley", 'Incumbent': True, "District": 'IA-03', 'State': "Iowa", "D+": +10, "S+": +15, "Party": "Republican", "Republican": +5, "Democrat": -3, "Independent": -1, "Conservative": +5, "Moderate": -2, "Liberal": -4, "Black": -2, "White": +3, 'Native': -2, "Hispanic": -2, 'Mormon': +3, "Asian": -1, "Degree": -5, "No Degree": +2}
Martha_McSally = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 52, 'Senate Terms': 1, 'Terms': 1, 'Governor Terms': 0, "Name": "Martha McSally", 'Incumbent': True, "District": 'AZ-02', 'State': "Arizona", "D+": +6, "S+": +9, "Party": "Republican", "Republican": -2, "Democrat": +1, "Independent": +2, "Conservative": -3, "Moderate": +4, "Liberal": +2, "Black": 0, "White": -1, 'Native': +1, "Hispanic": +1, 'Mormon': +4, "Asian": 0, "Degree": +2, "No Degree": -1}
Johnny_Isakson = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 15, 'Momentum': 0, 'Age': 74, 'Senate Terms': 3, 'Terms': 3, 'Governor Terms': 0, "Name": "Johnny Isakson", 'Incumbent': True, "District": 'GA-06', 'State': "Georgia", "D+": +5, "S+": +10, "Party": "Republican", "Republican": +4, "Democrat": -3, "Independent": -2, "Conservative": +3, "Moderate": -2, "Liberal": -4, "Black": -2, "White": +2, 'Native': -2, "Hispanic": -2, 'Mormon': +2, "Asian": -1, "Degree": -2, "No Degree": +1}
Ted_Cruz = {'Profile': 40, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 70, 'Momentum': 0, 'Age': 48, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Ted Cruz", 'Incumbent': True, "District": 'TX-12', 'State': "Texas", "D+": +2, "S+": +8, "Party": "Republican", "Republican": +5, "Democrat": -4, "Independent": -2, "Conservative": +7, "Moderate": -3, "Liberal": -5, "Black": -3, "White": +2, 'Native': -3, "Hispanic": +1, 'Mormon': +3, "Asian": -3, "Degree": -3, "No Degree": +1}
Tim_Scott = {'Profile': 30, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 50, 'Momentum': 0, 'Age': 53, 'Senate Terms': 2, 'Terms': 1, 'Governor Terms': 0, "Name": "Tim Scott", 'Incumbent': True, "District": 'SC-01', 'State': "South Carolina", "D+": +1, "S+": +10, "Party": "Republican", "Republican": +1, "Democrat": 0, "Independent": -2, "Conservative": +5, "Moderate": -1, "Liberal": -3, "Black": +5, "White": +1, 'Native': -3, "Hispanic": -3, 'Mormon': +1, "Asian": -3, "Degree": +2, "No Degree": -1}
Lindsey_Graham = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 60, 'Momentum': 0, 'Age': 63, 'Senate Terms': 2, 'Terms': 4, 'Governor Terms': 0, "Name": "Lindsey Graham", 'Incumbent': True, "District": 'SC-03', 'State': "South Carolina", "D+": +4, "S+": +8, "Party": "Republican", "Republican": +5, "Democrat": -6, "Independent": -3, "Conservative": -2, "Moderate": +1, "Liberal": +2, "Black": -2, "White": +2, 'Native': -3, "Hispanic": -3, 'Mormon': +1, "Asian": -3, "Degree": -5, "No Degree": +2}
Lisa_Murkowski = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 40, 'Momentum': 0, 'Age': 61, 'Senate Terms': 3, 'Terms': 0, 'Governor Terms': 0, "Name": "Lisa Murkowski", 'Incumbent': True, "District": 'AK-AL', 'State': "Alaska", "D+": +1, "S+": +12, "Party": "Republican", "Republican": -6, "Democrat": +6, "Independent": +7, "Conservative": -6, "Moderate": +6, "Liberal": +5, "Black": -4, "White": +4, 'Native': +6, "Hispanic": -3, 'Mormon': -3, "Asian": +2, "Degree": +5, "No Degree": -2}
Dan_Sullivan = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 54, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Dan Sullivan", 'Incumbent': True, "District": 'AK-AL', 'State': "Alaska", "D+": +1, "S+": +8, "Party": "Republican", "Republican": -3, "Democrat": +3, "Independent": +2, "Conservative": -3, "Moderate": +3, "Liberal": +2, "Black": -4, "White": +3, 'Native': -1, "Hispanic": -3, 'Mormon': -3, "Asian": -3, "Degree": 0, "No Degree": 0}
Roger_Wicker = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 67, 'Senate Terms': 2, 'Terms': 6, 'Governor Terms': 0, "Name": "Roger Wicker", 'Incumbent': True, "District": 'MS-01', 'State': "Mississippi", "D+": +8, "S+": +9, "Party": "Republican", "Republican": +4, "Democrat": -2, "Independent": -1, "Conservative": +4, "Moderate": -1, "Liberal": -2, "Black": -2, "White": +3, 'Native': -2, "Hispanic": -3, 'Mormon': -2, "Asian": -1, "Degree": 0, "No Degree": 0}
Mike_Braun = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 25, 'Momentum': 0, 'Age': 64, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Mike Braun", 'Incumbent': True, "District": 'IN-02', 'State': "Indiana", "D+": +2, "S+": +7, "Party": "Republican", "Republican": +3, "Democrat": -3, "Independent": -1, "Conservative": +5, "Moderate": -2, "Liberal": -3, "Black": -3, "White": +4, 'Native': -3, "Hispanic": -3, 'Mormon': +1, "Asian": -3, "Degree": -5, "No Degree": +2}
Todd_Young = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 35, 'Momentum': 0, 'Age': 46, 'Senate Terms': 1, 'Terms': 3, 'Governor Terms': 0, "Name": "Todd Young", 'Incumbent': True, "District": 'IN-09', 'State': "Indiana", "D+": +7, "S+": +9, "Party": "Republican", "Republican": +4, "Democrat": -3, "Independent": 0, "Conservative": +3, "Moderate": -1, "Liberal": -2, "Black": -2, "White": +3, 'Native': -2, "Hispanic": -2, 'Mormon': +4, "Asian": -2, "Degree": 0, "No Degree": 0}
Josh_Hawley = {'Profile': 20, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 30, 'Momentum': 0, 'Age': 39, 'Senate Terms': 1, 'Terms': 3, 'Governor Terms': 0, "Name": "Josh Hawley", 'Incumbent': True, "District": 'MO-05', 'State': "Missouri", "D+": +2, "S+": +8, "Party": "Republican", "Republican": +3, "Democrat": -2, "Independent": -1, "Conservative": +2, "Moderate": -1, "Liberal": -1, "Black": -3, "White": +3, 'Native': -2, "Hispanic": -3, 'Mormon': -2, "Asian": -2, "Degree": 0, "No Degree": 0}
Roy_Blount = {'Profile': 10, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 69, 'Senate Terms': 2, 'Terms': 7, 'Governor Terms': 0, "Name": "Roy Blount", 'Incumbent': True, "District": 'MO-07', 'State': "Missouri", "D+": +5, "S+": +7, "Party": "Republican", "Republican": +5, "Democrat": -3, "Independent": -2, "Conservative": +3, "Moderate": -1, "Liberal": -3, "Black": -3, "White": +2, 'Native': -2, "Hispanic": -3, 'Mormon': +3, "Asian": -2, "Degree": -5, "No Degree": +2}
Bill_Cassidy = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 61, 'Senate Terms': 1, 'Terms': 3, 'Governor Terms': 0, "Name": "Bill Cassidy", 'Incumbent': True, "District": 'LA-06', 'State': "Louisiana", "D+": +6, "S+": +9, "Party": "Republican", "Republican": -2, "Democrat": +2, "Independent": +2, "Conservative": -1, "Moderate": +2, "Liberal": +1, "Black": +2, "White": -1, 'Native': +1, "Hispanic": +1, 'Mormon': +2, "Asian": +1, "Degree": +2, "No Degree": -1}
John_Kennedy = {'Profile': 15, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 20, 'Momentum': 0, 'Age': 67, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "John Kennedy", 'Incumbent': True, "District": 'LA-03', 'State': "Louisiana", "D+": +1, "S+": +10, "Party": "Republican", "Republican": 0, "Democrat": 0, "Independent": +1, "Conservative": 0, "Moderate": 0, "Liberal": +1, "Black": +2, "White": +1, 'Native': -1, "Hispanic": -1, 'Mormon': +1, "Asian": +1, "Degree": +4, "No Degree": -2}
Mitt_Romney = {'Profile': 65, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 90, 'Momentum': 0, 'Age': 71, 'Senate Terms': 1, 'Terms': 0, 'Governor Terms': 0, "Name": "Mitt Romney", 'Incumbent': True, "District": 'UT-01', 'State': "Utah", "D+": +1, "S+": +10, "Party": "Republican", "Republican": -5, "Democrat": +3, "Independent": +5, "Conservative": -2, "Moderate": +3, "Liberal": +1, "Black": +4, "White": -5, 'Native': +4, "Hispanic": -2, 'Mormon': +12, "Asian": +4, "Degree": +8, "No Degree": -4}
Mike_Lee = {'Profile': 30, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 45, 'Momentum': 0, 'Age': 47, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Mike Lee", 'Incumbent': True, "District": 'UT-03', 'State': "Utah", "D+": +1, "S+": +12, "Party": "Republican", "Republican": +2, "Democrat": -1, "Independent": -1, "Conservative": +5, "Moderate": -2, "Liberal": -3, "Black": -2, "White": +1, 'Native': -1, "Hispanic": -2, 'Mormon': +5, "Asian": -1, "Degree": 0, "No Degree": 0}
Mitch_McConnell = {'Profile': 45, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 85, 'Momentum': 0, 'Age': 76, 'Senate Terms': 5, 'Terms': 0, 'Governor Terms': 0, "Name": "Mitch McConnell", 'Incumbent': True, "District": 'KY-05', 'State': "Kentucky", "D+": +1, "S+": +10, "Party": "Republican", "Republican": +4, "Democrat": -3, "Independent": -1, "Conservative": +3, "Moderate": -2, "Liberal": -4, "Black": -2, "White": +1, 'Native': -2, "Hispanic": +1, 'Mormon': +3, "Asian": -1, "Degree": 0, "No Degree": 0}
Rand_Paul = {'Profile': 35, 'District Name Rec': 95, 'State Name Rec': 95, 'Nat Name Rec': 55, 'Momentum': 0, 'Age': 56, 'Senate Terms': 2, 'Terms': 0, 'Governor Terms': 0, "Name": "Rand Paul", 'Incumbent': True, "District": 'KY-03', 'State': "Kentucky", "D+": +1, "S+": +9, "Party": "Republican", "Republican": +5, "Democrat": -3, "Independent": -2, "Conservative": +6, "Moderate": -3, "Liberal": -4, "Black": -3, "White": +5, 'Native': -3, "Hispanic": -4, 'Mormon': +2, "Asian": -1, "Degree": 0, "No Degree": 0}



Races = {"White": White, "Black": Black, "Asian": Asian, "Hispanic": Hispanic, 'Mormon': Mormon, 'Native': Native}
Ideologies = {"Moderate": Moderate, "Conservative": Conservative, "Liberal": Liberal}
Educations = {"Degree": Educated, "No Degree": Uneducated}
Parties = {"Republican": Republican, "Democrat": Democrat, "Independent": Independent}
Turnout = {'President': 1, 'Senator': 0.5, 'Governor': 0.75, 'MC': 0.25}


California = {'CDs': 53, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Jungle', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': "CA", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.42, "Black": 0.06, "Hispanic": 0.39, "Asian": 0.13, 'Population': 38802500, 'Name': 'California', 'Education': 0.314, 'Conservative': 0.29, 'Moderate': 0.37, 'Liberal': 0.34, 'Race Adjustments': {"White": {"Democrat": +0.15, "Republican": -0.12, "Independent": -0.03}}}
Mississippi = {'CDs': 4, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [3], 'Abbrev': "MS", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.59, "Black": 0.37, "Hispanic": 0.03, "Asian": 0.01, 'Population': 2984100, 'Name': 'Mississippi', 'Education': 0.207, 'Conservative': 0.47, 'Moderate': 0.38, 'Liberal': 0.15, 'Race Adjustments': {"White": {"Democrat": -0.25, "Republican": +0.5, "Independent": -0.25}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
West_Virginia = {'CDs': 3, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [0], 'Abbrev': "WV", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.94, "Black": 0.03, "Hispanic": 0.02, "Asian": 0.01, 'Population': 1815857, 'Name': 'West Virginia', 'Education': 0.192, 'Conservative': 0.40, 'Moderate': 0.40, 'Liberal': 0.20, 'Race Adjustments': {"White": {"Democrat": -0.12, "Republican": +0.07, "Independent": +0.05}}}
Ohio = {'CDs': 16, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'OH', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.75, "Black": 0.17, "Hispanic": 0.05, "Asian": 0.03, 'Population': 11658609, 'Name': 'Ohio', 'Education': 0.278, 'Conservative': 0.37, 'Moderate': 0.4, 'Liberal': 0.23, 'Race Adjustments': {"White": {"Democrat": +0.01, "Republican": -0.03, "Independent": +0.02}}}
Nevada = {'CDs': 4, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Mormon'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'NV', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.37, 'Mormon': 0.04, "Black": 0.13, "Hispanic": 0.39, "Asian": 0.07, 'Population': 2998039, 'Name': 'Nevada', 'Education': 0.23, 'Conservative': 0.35, 'Moderate': 0.41, 'Liberal': 0.24, 'Race Adjustments': {"White": {"Democrat": -0.13, "Republican": +0.09, "Independent": +0.04}, "Hispanic": {"Democrat": -0.1, "Republican": +0.05, "Independent": +0.05}}}
Utah = {'CDs': 4, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Mormon'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [0],'Abbrev': 'UT', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.31, 'Mormon': 0.55, "Black": 0.01, "Hispanic": 0.11, "Asian": 0.02, 'Population': 3101833, 'Name': 'Utah', 'Education': 0.311, 'Conservative': 0.44, 'Moderate': 0.37, 'Liberal': 0.19, 'Race Adjustments': {}}
Texas = {'CDs': 36, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'TX', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.46, "Black": 0.12, "Hispanic": 0.38, "Asian": 0.04, 'Population': 28304596, 'Name': 'Texas', 'Education': 0.295, 'Conservative': 0.4, 'Moderate': 0.38, 'Liberal': 0.22, 'Race Adjustments': {"White": {"Democrat": -0.12, "Republican": +0.16, "Independent": -0.04}, "Hispanic": {"Democrat": -0.20, "Republican": +0.25, "Independent": -0.05}}}
Iowa = {'CDs': 4, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': 'IA', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.90, "Black": 0.03, "Hispanic": 0.05, "Asian": 0.02, 'Population': 3145711, 'Name': 'Iowa', 'Education': 0.267, 'Conservative': 0.39, 'Moderate': 0.36, 'Liberal': 0.25, 'Race Adjustments': {"White": {"Democrat": +0.11, "Republican": -0.17, "Independent": +0.06}}}
New_Hampshire = {'CDs': 2, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [0,2], 'Abbrev': 'NH', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.93, "Black": 0.01, "Hispanic": 0.04, "Asian": 0.02, 'Population': 1342795, 'Name': 'New Hampshire', 'Education': 0.349, 'Conservative': 0.33, 'Moderate': 0.41, 'Liberal': 0.26, 'Race Adjustments': {"White": {"Democrat": +0.11, "Republican": -0.21, "Independent": +0.10}}}
South_Carolina = {'CDs': 7, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "SC", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.65, "Black": 0.27, "Hispanic": 0.06, "Asian": 0.02, 'Population': 5024369, 'Name': 'South Carolina', 'Education': 0.258, 'Conservative': 0.41, 'Moderate': 0.35, 'Liberal': 0.17, 'Race Adjustments': {"White": {"Democrat": -0.15, "Republican": +0.35, "Independent": -0.2}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Virginia = {'CDs': 11, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [1], 'Abbrev': "VA", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.64, "Black": 0.20, "Hispanic": 0.09, "Asian": 0.07, 'Population': 8470020, 'Name': 'Virginia', 'Education': 0.363, 'Conservative': 0.35, 'Moderate': 0.40, 'Liberal': 0.25, 'Race Adjustments': {"White": {"Democrat": -0.03, "Republican": +0.09, "Independent": -0.06}, "Black": {"Democrat": +0.05, "Independent": -0.05}}}
Georgia = {'CDs': 14, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "GA", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.57, "Black": 0.31, "Hispanic": 0.09, "Asian": 0.03, 'Population': 10429739, 'Name': 'Georgia', 'Education': 0.288, 'Conservative': 0.38, 'Moderate': 0.39, 'Liberal': 0.23, 'Race Adjustments': {"White": {"Democrat": -0.23, "Republican": +0.45, "Independent": -0.22}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Massachusetts = {'CDs': 9, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'MA', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.74, "Black": 0.09, "Hispanic": 0.10, "Asian": 0.07, 'Population': 6859819, 'Name': 'Massachusetts', 'Education': 0.405, 'Conservative': 0.23, 'Moderate': 0.4, 'Liberal': 0.37, 'Race Adjustments': {"White": {"Democrat": +0.14, "Republican": -0.28, "Independent": +0.14}}}
Alabama = {'CDs': 7, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "AL", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.68, "Black": 0.27, "Hispanic": 0.04, "Asian": 0.01, 'Population': 4874747, 'Name': 'Alabama', 'Education': 0.235, 'Conservative': 0.46, 'Moderate': 0.36, 'Liberal': 0.18, 'Race Adjustments': {"White": {"Democrat": -0.25, "Republican": +0.47, "Independent": -0.22}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Minnesota = {'CDs': 8, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'MN', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.84, "Black": 0.06, "Hispanic": 0.05, "Asian": 0.05, 'Population': 5450868, 'Name': 'Minnesota', 'Education': 0.337, 'Conservative': 0.34, 'Moderate': 0.38, 'Liberal': 0.28, 'Race Adjustments': {"White": {"Democrat": +0.11, "Republican": -0.14, "Independent": +0.03}}}
Vermont = {'CDs': 1, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [0,2], 'Abbrev': 'VT', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.93, "Black": 0.02, "Hispanic": 0.02, "Asian": 0.03, 'Population': 623657, 'Name': 'Vermont', 'Education': 0.36, 'Conservative': 0.26, 'Moderate': 0.33, 'Liberal': 0.41, 'Race Adjustments': {"White": {"Democrat": +0.7, "Republican": -0.3, "Independent": -0.2}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Alaska = {'CDs': 1, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': 'AK', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.68, "Black": 0.04, "Hispanic": 0.07, "Asian": 0.06, 'Native': 0.15, 'Population': 739795, 'Name': 'Alaska', 'Education': 0.28, 'Conservative': 0.38, 'Moderate': 0.44, 'Liberal': 0.18, 'Race Adjustments': {'White': {"Democrat": -0.18, "Independent": +0.18}}}
Arkansas = {'CDs': 4, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "AR", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.75, "Black": 0.17, "Hispanic": 0.07, "Asian": 0.01, 'Population': 3004279, 'Name': 'Arkansas', 'Education': 0.235, 'Conservative': 0.45, 'Moderate': 0.37, 'Liberal': 0.18, 'Race Adjustments': {"White": {"Democrat": -0.18, "Republican": +0.36, "Independent": -0.18}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Oklahoma = {'CDs': 5, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "OK", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.71, "Black": 0.08, "Hispanic": 0.1, "Asian": 0.02, 'Native': 0.09, 'Population': 3930864, 'Name': 'Oklahoma', 'Education': 0.241, 'Conservative': 0.45, 'Moderate': 0.37, 'Liberal': 0.18, 'Race Adjustments': {"White": {"Democrat": -0.22, "Republican": +0.44, "Independent": -0.22}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Tennessee = {'CDs': 9, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': "TN", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.69, "Black": 0.2, "Hispanic": 0.09, "Asian": 0.02, 'Population': 6715984, 'Name': 'Tennessee', 'Education': 0.249, 'Conservative': 0.42, 'Moderate': 0.38, 'Liberal': 0.2, 'Race Adjustments': {"White": {"Democrat": -0.2, "Republican": +0.4, "Independent": -0.2}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Washington_DC = {'CDs': 1, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [], 'Mansion Years': [], 'Abbrev': "DC", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.35, "Black": 0.52, "Hispanic": 0.09, "Asian": 0.04, 'Population': 693972, 'Name': 'Washington DC', 'Education': 0.546, 'Conservative': 0.16, 'Moderate': 0.34, 'Liberal': 0.5, 'Race Adjustments': {"White": {"Democrat": +0.66, "Republican": -0.33, "Independent": -0.33}, "Black": {"Democrat": +0.3, "Independent": -0.25, "Republican": -0.05}, "Hispanic": {"Democrat": +0.4, "Independent": -0.2, "Republican": -0.2}, "Asian": {"Democrat": +0.3, "Independent": -0.15, "Republican": -0.15}}}
Kansas = {'CDs': 4, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "KS", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.79, "Black": 0.06, "Hispanic": 0.12, "Asian": 0.03, 'Population': 2913123, 'Name': 'Kansas', 'Education': 0.31, 'Conservative': 0.4, 'Moderate': 0.4, 'Liberal': 0.2, 'Race Adjustments': {"White": {"Democrat": -0.16, "Republican": +0.09, "Independent": +0.07}}}
Kentucky = {'CDs': 6, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [3], 'Abbrev': "KY", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.88, "Black": 0.08, "Hispanic": 0.03, "Asian": 0.01, 'Population': 4454189, 'Name': 'Kentucky', 'Education': 0.223, 'Conservative': 0.43, 'Moderate': 0.37, 'Liberal': 0.2, 'Race Adjustments': {"White": {"Democrat": -0.08, "Republican": +0.16, "Independent": -0.08}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Louisiana = {'CDs': 6, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Jungle', 'Senate Seats': [0,4], 'Mansion Years': [3], 'Abbrev': "LA", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.6, "Black": 0.33, "Hispanic": 0.05, "Asian": 0.02, 'Population': 4684333, 'Name': 'Louisiana', 'Education': 0.225, 'Conservative': 0.43, 'Moderate': 0.38, 'Liberal': 0.19, 'Race Adjustments': {"White": {"Democrat": -0.25, "Republican": +0.6, "Independent": -0.35}, "Black": {"Democrat": +0.2, "Independent": -0.15, 'Republican': -0.05}}}
Maine = {'CDs': 2, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'ME', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.95, "Black": 0.01, "Hispanic": 0.02, "Asian": 0.02, 'Population': 1341582, 'Name': 'Maine', 'Education': 0.29, 'Conservative': 0.35, 'Moderate': 0.32, 'Liberal': 0.32, 'Race Adjustments': {"White": {"Democrat": +0.15, "Republican": -0.35, "Independent": +0.2}}}
Hawaii = {'CDs': 2, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'HI', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.34, "Black": 0.03, "Hispanic": 0.09, "Asian": 0.54, 'Population': 1427538, 'Name': 'Hawaii', 'Education': 0.31, 'Conservative': 0.27, 'Moderate': 0.46, 'Liberal': 0.27, 'Race Adjustments': {"Asian": {"Democrat": +0.15, "Republican": -0.15}, "White": {"Democrat": +0.25, "Republican": -0.2, "Independent": -0.05}}}
Idaho = {'CDs': 2, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Mormon'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2],'Abbrev': 'ID', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.66, 'Mormon': 0.19, "Black": 0.01, "Hispanic": 0.12, "Asian": 0.02, 'Population': 3101833, 'Name': 'Idaho', 'Education': 0.311, 'Conservative': 0.44, 'Moderate': 0.37, 'Liberal': 0.19, 'Race Adjustments': {"White": {"Democrat": -0.1, "Republican": +0.15, "Independent": -0.05}, "Hispanic": {"Democrat": -0.11, "Republican": +0.14, "Independent": -0.03}}}
Michigan = {'CDs': 14, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'MI', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.78, "Black": 0.14, "Hispanic": 0.05, "Asian": 0.03, 'Population': 9995915, 'Name': 'Michigan', 'Education': 0.269, 'Conservative': 0.37, 'Moderate': 0.38, 'Liberal': 0.25, 'Race Adjustments': {"White": {"Democrat": +0.07, "Republican": -0.11, "Independent": +0.04}}}
Wyoming = {'CDs': 1, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Mormon'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': "WY", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.76, 'Mormon': 0.1, "Black": 0.02, "Hispanic": 0.11, "Asian": 0.01, 'Population': 579315, 'Name': 'Wyoming', 'Education': 0.257, 'Conservative': 0.48, 'Moderate': 0.38, 'Liberal': 0.14, 'Race Adjustments': {"White": {"Democrat": -0.15, "Republican": +0.32, "Independent": -0.17}}}
Florida = {'CDs': 27, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': "FL", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.54, "Black": 0.17, "Hispanic": 0.26, "Asian": 0.03, 'Population': 21299325, 'Name': 'Florida', 'Education': 0.273, 'Conservative': 0.37, 'Moderate': 0.39, 'Liberal': 0.24, 'Race Adjustments': {"White": {"Democrat": -0.1, "Republican": +0.25, "Independent": -0.15}, "Hispanic": {"Democrat": -0.07, "Independent": +0.07}, "Black": {"Democrat": +0.15, "Independent": -0.15}}}
Illinois = {'CDs': 18, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': 'IL', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.64, "Black": 0.15, "Hispanic": 0.16, "Asian": 0.05, 'Population': 12741080, 'Name': 'Illinois', 'Education': 0.323, 'Conservative': 0.32, 'Moderate': 0.39, 'Liberal': 0.29, 'Race Adjustments': {"White": {"Democrat": +0.1, "Republican": -0.12, "Independent": +0.02}}}
Missouri = {'CDs': 8, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [0], 'Abbrev': "MO", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.82, "Black": 0.12, "Hispanic": 0.04, "Asian": 0.02, 'Population': 6113532, 'Name': 'Missouri', 'Education': 0.271, 'Conservative': 0.4, 'Moderate': 0.38, 'Liberal': 0.22, 'Race Adjustments': {"White": {"Democrat": -0.1, "Republican": +0.06, "Independent": +0.04}, "Black": {"Democrat": +0.1, "Independent": -0.1}}}
North_Carolina = {'CDs': 13, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [0], 'Abbrev': "NC", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.67, "Black": 0.23, "Hispanic": 0.08, "Asian": 0.02, 'Population': 10383620, 'Name': 'North Carolina', 'Education': 0.284, 'Conservative': 0.39, 'Moderate': 0.39, 'Liberal': 0.22, 'Race Adjustments': {"White": {"Democrat": -0.07, "Republican": +0.15, "Independent": -0.08}, "Black": {"Democrat": +0.1, "Independent": -0.1}}}
Arizona = {'CDs': 9, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Mormon'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'AZ', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.57, 'Mormon': 0.04, "Black": 0.04, "Hispanic": 0.31, "Asian": 0.04, 'Population': 7016270, 'Name': 'Arizona', 'Education': 0.275, 'Conservative': 0.35, 'Moderate': 0.4, 'Liberal': 0.25, 'Race Adjustments': {"White": {"Democrat": -0.05, "Republican": +0.1, "Independent": -0.05}, "Hispanic": {"Democrat": -0.07, "Republican": +0.07}}}
Colorado = {'CDs': 7, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': 'CO', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.71, "Black": 0.04, "Hispanic": 0.22, "Asian": 0.03, 'Population': 5695564, 'Name': 'Colorado', 'Education': 0.381, 'Conservative': 0.32, 'Moderate': 0.39, 'Liberal': 0.29, 'Race Adjustments': {"White": {"Democrat": +0.03, "Republican": -0.06, "Independent": +0.03}}}
North_Dakota = {'CDs': 1, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [0], 'Abbrev': "ND", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.89, "Black": 0.01, "Hispanic": 0.04, "Asian": 0.01, 'Native': 0.05, 'Population': 755393, 'Name': 'North Dakota', 'Education': 0.277, 'Conservative': 0.4, 'Moderate': 0.44, 'Liberal': 0.16, 'Race Adjustments': {"White": {"Democrat": -0.09, "Republican": +0.18, "Independent": -0.09}}}
Wisconsin = {'CDs': 8, 'Open Primary': True, 'Term Limits': False, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'WI', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.85, "Black": 0.06, "Hispanic": 0.07, "Asian": 0.02, 'Population': 5795483, 'Name': 'Wisconsin', 'Education': 0.276, 'Conservative': 0.37, 'Moderate': 0.39, 'Liberal': 0.24, 'Race Adjustments': {"White": {"Democrat": +0.12, "Republican": -0.2, "Independent": +0.08}}}
New_York = {'CDs': 27, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'NY', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.59, "Black": 0.16, "Hispanic": 0.18, "Asian": 0.07, 'Population': 19542209, 'Name': 'New York', 'Education': 0.342, 'Conservative': 0.29, 'Moderate': 0.38, 'Liberal': 0.33, 'Race Adjustments': {"White": {"Democrat": +0.12, "Republican": -0.26, "Independent": +0.14}}}
Connecticut = {'CDs': 5, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'CT', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.73, "Black": 0.10, "Hispanic": 0.13, "Asian": 0.04, 'Population': 3588184, 'Name': 'Connecticut', 'Education': 0.376, 'Conservative': 0.29, 'Moderate': 0.39, 'Liberal': 0.32, 'Race Adjustments': {"White": {"Democrat": +0.09, "Republican": -0.18, "Independent": +0.09}}}
Delaware = {'CDs': 1, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [0], 'Abbrev': 'DE', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.67, "Black": 0.22, "Hispanic": 0.08, "Asian": 0.03, 'Population': 961939, 'Name': 'Delaware', 'Education': 0.3, 'Conservative': 0.3, 'Moderate': 0.4, 'Liberal': 0.3, 'Race Adjustments': {"White": {"Democrat": +0.06, "Republican": -0.15, "Independent": +0.09}}}
Maryland = {'CDs': 8, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'MD', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.51, "Black": 0.3, "Hispanic": 0.13, "Asian": 0.06, 'Population': 6052177, 'Name': 'Maryland', 'Education': 0.38, 'Conservative': 0.29, 'Moderate': 0.4, 'Liberal': 0.31, 'Race Adjustments': {"White": {"Democrat": +0.02, "Republican": -0.04, "Independent": +0.02}}}
Pennsylvania = {'CDs': 18, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [2], 'Abbrev': 'PA', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.8, "Black": 0.11, "Hispanic": 0.06, "Asian": 0.03, 'Population': 12805537, 'Name': 'Pennsylvania', 'Education': 0.286, 'Conservative': 0.35, 'Moderate': 0.4, 'Liberal': 0.25, 'Race Adjustments': {"White": {"Democrat": +0.06, "Republican": -0.09, "Independent": +0.03}}}
Rhode_Island = {'CDs': 2, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'RI', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.77, "Black": 0.06, "Hispanic": 0.14, "Asian": 0.03, 'Population': 1059639, 'Name': 'Rhode Island', 'Education': 0.319, 'Conservative': 0.27, 'Moderate': 0.42, 'Liberal': 0.31, 'Race Adjustments': {"White": {"Democrat": +0.14, "Republican": -0.23, "Independent": +0.09}}}
Indiana = {'CDs': 9, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,2], 'Mansion Years': [0], 'Abbrev': 'IN', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.82, "Black": 0.1, "Hispanic": 0.06, "Asian": 0.02, 'Population': 6666818, 'Name': 'Indiana', 'Education': 0.241, 'Conservative': 0.36, 'Moderate': 0.39, 'Liberal': 0.24, 'Race Adjustments': {"White": {"Democrat": -0.07, "Republican": +0.07}}}
Oregon = {'CDs': 5, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': 'OR', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.8, "Black": 0.02, "Hispanic": 0.14, "Asian": 0.04, 'Population': 4142776, 'Name': 'Oregon', 'Education': 0.308, 'Conservative': 0.29, 'Moderate': 0.39, 'Liberal': 0.32, 'Race Adjustments': {"White": {"Democrat": +0.14, "Republican": -0.28, "Independent": +0.14}}}
Washington = {'CDs': 10, 'Open Primary': False, 'Term Limits': False, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Jungle', 'Senate Seats': [0,2], 'Mansion Years': [0], 'Abbrev': 'WA', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.76, "Black": 0.04, "Hispanic": 0.12, "Asian": 0.08, 'Population': 7405743, 'Name': 'Washington', 'Education': 0.329, 'Conservative': 0.31, 'Moderate': 0.38, 'Liberal': 0.31, 'Race Adjustments': {"White": {"Democrat": +0.16, "Republican": -0.32, "Independent": +0.16}}}
Montana = {'CDs': 1, 'Open Primary': True, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [0], 'Abbrev': "MT", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.89, "Black": 0.01, "Hispanic": 0.03, "Asian": 0.01, 'Native': 0.06, 'Population': 1050493, 'Name': 'Montana', 'Education': 0.295, 'Conservative': 0.43, 'Moderate': 0.35, 'Liberal': 0.21, 'Race Adjustments': {}}
New_Jersey = {'CDs': 12, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'NJ', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.6, "Black": 0.14, "Hispanic": 0.18, "Asian": 0.08, 'Population': 9005644, 'Name': 'New Jersey', 'Education': 0.368, 'Conservative': 0.31, 'Moderate': 0.41, 'Liberal': 0.28, 'Race Adjustments': {"White": {"Democrat": +0.09, "Republican": -0.15, "Independent": +0.08}}}
New_Mexico = {'CDs': 3, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Democrat', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': 'NM', "Parties": ["Republican", "Democrat", "Independent"], "White": 0.37, "Black": 0.03, "Hispanic": 0.48, "Asian": 0.02, 'Native': 0.1, 'Population': 2088070, 'Name': 'New Mexico', 'Education': 0.263, 'Conservative': 0.34, 'Moderate': 0.4, 'Liberal': 0.26, 'Race Adjustments': {"White": {"Democrat": -0.11, "Republican": +0.16, "Independent": -0.05}}}
South_Dakota = {'CDs': 1, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Nonpartisan', 'Races': ['White', 'Black', 'Hispanic', 'Asian', 'Native'], 'Primary Type': 'Regular', 'Senate Seats': [0,4], 'Mansion Years': [2], 'Abbrev': "SD", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.85, "Black": 0.01, "Hispanic": 0.03, "Asian": 0.01, 'Native': 0.1, 'Population': 869666, 'Name': 'South Dakota', 'Education': 0.27, 'Conservative': 0.43, 'Moderate': 0.42, 'Liberal': 0.15, 'Race Adjustments': {"White": {"Democrat": -0.05, "Republican": +0.1, "Independent": -0.05}}}
Nebraska = {'CDs': 3, 'Open Primary': False, 'Term Limits': True, 'Redistricting': 'Republican', 'Races': ['White', 'Black', 'Hispanic', 'Asian'], 'Primary Type': 'Regular', 'Senate Seats': [2,4], 'Mansion Years': [2], 'Abbrev': "NE", "Parties": ["Republican", "Democrat", "Independent"], "White": 0.83, "Black": 0.05, "Hispanic": 0.1, "Asian": 0.02, 'Population': 1920076, 'Name': 'Nebraska', 'Education': 0.293, 'Conservative': 0.43, 'Moderate': 0.35, 'Liberal': 0.22, 'Race Adjustments': {"White": {"Democrat": -0.09, "Republican": +0.17, "Independent": -0.08}}}

GE_Order = ['IN', 'KY', 'FL', 'GA', 'NH', 'SC', 'VT', 'VA', 'DC', 'NC', 'OH', 'WV', 'AL', 'CT', 'DE', 'IL', 'KS', 'ME', 'MD', 'MA', 'MI', 'MS', 'MO', 'NJ', 'ND', 'OK', 'PA', 'RI', 'SD', 'TX', 'TN', 'AR', 'AZ', 'LA', 'CO', 'MN', 'NE', 'NM', 'NY', 'WI', 'WY', 'ID', 'IA', 'MT', 'NV', 'UT', 'CA', 'OR', 'WA', 'HI', 'AK']

Primary = {'Febuary 3rd': ['IA'], 'February 11th': ['NH'], 'February 22': ['NV'], 'February 29th': ['SC'], 'March 3rd': ['AL', 'CA', 'CO', 'GA', 'MA', 'MN', 'NC', 'OK', 'TN', 'TX', 'VT', 'VA'], 'March 7th': ['LA', 'ME', 'NE'], 'March 10th': ['KS', 'MI', 'MS', 'MO', 'OH'], 'March 17th': ['AZ', 'FL', 'ID', 'IL', 'UT'], 'March 26th': ['AK', 'HI', 'WA'], 'April 7th': ['WI', 'WY'], 'April 19th': ['NY'], 'April 28th': ['CT', 'DE', 'MD', 'PA', 'RI'], 'May 5th': ['IN'], 'May 12th': ['WV'], 'May 19th': ['AR','KY','OR'], 'June 2nd': ['MT', 'NJ', 'NM', 'ND', 'SD'], 'June 16th': ['DC']}
USA = {'States': {'IA': Iowa, 'NH': New_Hampshire, 'SC': South_Carolina, 'NV': Nevada, "MI": Michigan, "WY": Wyoming, "HI": Hawaii, "ID": Idaho, "LA": Louisiana, "ME": Maine, "KS": Kansas, "KY": Kentucky, 'VT': Vermont, 'OK': Oklahoma, 'TN': Tennessee, 'AK': Alaska, 'AR': Arkansas, 'MN': Minnesota, 'MA': Massachusetts, 'AL': Alabama, 'GA': Georgia, 'VA': Virginia, 'TX': Texas, 'DC': Washington_DC, 'FL': Florida, "NC": North_Carolina, "MO": Missouri, "IL": Illinois, 'UT': Utah, "CO": Colorado, 'ND': North_Dakota, 'WI': Wisconsin, 'AZ': Arizona, 'NY': New_York, 'CT': Connecticut, "PA": Pennsylvania, "RI": Rhode_Island, 'DE': Delaware, 'OH': Ohio, 'MD': Maryland, 'WV': West_Virginia, 'IN': Indiana, "OR": Oregon, 'WA': Washington, 'MT': Montana, 'NJ': New_Jersey, 'MS': Mississippi, 'NM': New_Mexico, 'NE': Nebraska, 'SD': South_Dakota, 'CA': California}, 'Natenv': Parties, 'President': Donald_Trump}


def redistricting(state):
    print(state['Name'] + ' Redistricting')
    increment = int(len(state['Districts'][state['Abbrev'] + "-01"]) / 5)
    rep = 0
    dem = 0
    leans = {}
    for i in state['District Facts']:
        leans[i] = state['District Facts'][i]['Partisan Lean']
        if leans[i] < 0:
            rep += 1
        else:
            dem += 1
    ideal = 50 + (state['Partisan Lean'] / 2)
    actual = (dem / (dem + rep)) * 100
    order = sorted(leans, key=leans.get) #most republican to most democrat
    if state['CDs'] % 2 == 1:
        med = leans[order[math.floor(len(order) / 2)]]
    else:
        med = round((leans[order[int(len(order) / 2)]] + leans[order[int(len(order) / 2 - 1)]]) / 2, 1)
    if med < 0:
        print(state['Name'] + " median district before: " + color.RED + "+" + str(abs(med)) + "R" + color.END)
    else:
        print(state['Name'] + " median district before: " + color.BLUE + "+" + str(abs(med)) + "D" + color.END)
    additions = {}
    total = {}
    for i in order:
        additions[i] = []
        total[i] = 0
    for i in state['Districts']:
        part = randint(0, 4)
        x = part * increment
        y = part * increment + increment
        if y > len(state['Districts'][i]):
            y = len(state['Districts'][i])
        for z in range(x, y):
            additions[i].append(state['Districts'][i][z])
        del state['Districts'][i][x:y]
    for i in additions:
        if state['Redistricting'] == 'Republican':
            for n in additions[i]:
                if n['Party ID'] == 'Republican':
                    total[i] += 1
        elif state['Redistricting'] == 'Democrat':
            for n in additions[i]:
                if n['Party ID'] == 'Democrat':
                    total[i] += 1
        elif state['Redistricting'] == 'Independent':
            for n in additions[i]:
                if n['Party ID'] == 'Independent':
                    total[i] += 1
        else:
            if ideal - actual > 15:
                for n in additions[i]:
                    if n['Party ID'] == 'Democrat':
                        total[i] += 1
            elif ideal - actual < -15:
                for n in additions[i]:
                    if n['Party ID'] == 'Republican':
                        total[i] += 1
            else:
                for n in total:
                    total[n] = randint(0,1000)
    order1 = sorted(total, key=total.get)
    lst = []
    for i in order1:
        lst.append(additions[i])
    farthest = {}
    for i in leans:
        farthest[i] = 100 - abs(leans[i])
    order2 = sorted(farthest, key=farthest.get)
    for i in range(0, len(order2)):
        state['Districts'][order2[i]] += lst[i]
    for i in state['Districts']:
        district_facts(i, state)
    state_facts(state)
    leans = {}
    for i in state['District Facts']:
        leans[i] = state['District Facts'][i]['Partisan Lean']
    order = sorted(leans, key=leans.get)  # most republican to most democrat
    if state['CDs'] % 2 == 1:
        med = leans[order[math.floor(len(order) / 2)]]
    else:
        med = round((leans[order[int(len(order) / 2)]] + leans[order[int(len(order) / 2 - 1)]]) / 2, 1)
    if med < 0:
        print(state['Name'] + " median district after: " + color.RED + "+" + str(abs(med)) + "R" + color.END)
    else:
        print(state['Name'] + " median district after: " + color.BLUE + "+" + str(abs(med)) + "D" + color.END)


def normalize(probs, greatest):  # Makes sure inconvenient sets of probabilities sum to one
    s = sum(probs.values())
    for i in probs:
        probs[i] = round(probs[i] / s, 2)
    if sum(probs.values()) != 1.0:
        s = sum(probs.values())
        for i in probs:
            probs[i] = round(probs[i] / s, 2)
        if sum(probs.values()) != 1.0:
            probs[greatest] += 1.0 - sum(probs.values())
            probs[greatest] = round(probs[greatest], 2)


def state_education(race, state):  # Adjusts the rate of education for any individual race based on the education rate of the state
    r = Races[race]
    d = 0
    for i in state['Races']:
        d += Races[i]['Education'] * state[i]
    college = round((r["Education"] * state["Education"]) / d, 3)
    coll = {"Degree": college, "No Degree": 1 - college}
    return coll


def col_index(state):  # Prepares state for voter creation using education adjustment
    state["ColIndex"] = {}
    for i in state['Races']:
        state["ColIndex"][i] = state_education(i, state)


def probabilities(race, education):  # Extracts the probability of being from an ideology given education/race
    probs = {}
    adj = {}
    r = Races[race]
    college = r['Education']
    no_college = 1 - college
    for n in Ideologies:
        adj[n] = r[n]
    if education == "Degree":
        for n in Ideologies:
            probs[n] = adj[n] / (college + (no_college * Uneducated[n] / Educated[n]))
    else:
        for n in Ideologies:
            probs[n] = adj[n] / (no_college + (college * Educated[n] / Uneducated[n]))
    normalize(probs, "Moderate")
    return probs


def rematrix(state):  # Prepares state for voter creation with probabilities function
    state["R-E Matrix 1"] = {}
    for f in state['Races']:
        state["R-E Matrix 1"][f] = {}
        state["R-E Matrix 1"][f]["Degree"] = probabilities(f, "Degree")
        state["R-E Matrix 1"][f]["No Degree"] = probabilities(f, "No Degree")
    state["R-E Matrix"] = copy.copy(state["R-E Matrix 1"])
    adjusts = {}
    for f in state['Races']:
        for u in state["R-E Matrix 1"][f]:
            for i in state["R-E Matrix 1"][f][u]:
                adjusts[i] = 0
    for f in state['Races']:
        for u in state["R-E Matrix 1"][f]:
            for i in adjusts:
                adjusts[i] += state["R-E Matrix 1"][f][u][i] * state["ColIndex"][f][u] * state[f]
    for f in state['Races']:
        for u in state["R-E Matrix 1"][f]:
            for i in adjusts:
                state["R-E Matrix"][f][u][i] = state[i] / adjusts[i] * state["R-E Matrix 1"][f][u][i]
    for f in state['Races']:
        for u in state["R-E Matrix"][f]:
            normalize(state["R-E Matrix"][f][u], "Moderate")
    del state["R-E Matrix 1"]


def voter(state):  # Generates a voter with ideology, race, and education level based on the state
    v = {}
    z = randint(0, 100) / 100
    v['Race'] = 'White'
    h = 0
    for i in state['Races']:
        h += state[i]
        if z <= h:
            v["Race"] = i
            break
    h = 0
    z = randint(0, 100) / 100
    for u in state["ColIndex"][v["Race"]]:
        h += state["ColIndex"][v["Race"]][u]
        if z <= h:
            v["Education"] = u
            break
    z = randint(0, 100) / 100
    h = 0
    for i in state["R-E Matrix"][v["Race"]][v["Education"]]:
        h += state["R-E Matrix"][v["Race"]][v["Education"]][i]
        if z <= h:
            v["Ideology"] = i
            break
        v["Ideology"] = i
    return v


def state_stats(state, voters):
    parties = {}
    races = {}
    ideologies = {}
    educations = {}
    for i in state['Parties']:
        parties[i] = 0
    for i in state['Races']:
        races[i] = 0
    for i in Ideologies:
        ideologies[i] = 0
    for i in Educations:
        educations[i] = 0
    for n in range(0, len(voters)):
        x = voters[n]
        if x['Race'] == "Hispanic" and x['Education'] == "No Degree":
            for i in state['Parties']:
                if x['Party ID'] == i:
                    parties[i] += 1
            for i in Ideologies:
                if x['Ideology'] == i:
                    ideologies[i] += 1
            for i in state['Races']:
                if x['Race'] == i:
                    races[i] += 1
            for i in Educations:
                if x['Education'] == i:
                    educations[i] += 1
    normalize(races, 'White')
    normalize(ideologies, 'Moderate')
    normalize(parties, 'Independent')
    normalize(educations, 'No Degree')
    things = [races, ideologies, parties, educations]
    for i in range(0, len(things)):
        for u in things[i]:
            print(str(u) + ": " + str(round(things[i][u] * 100, 1)) + "%")
        print()


def vote(vtr, cands, natcorrelation, natenv, state, district, upballot):

    scores = {}
    for n in cands:
        scores[cands[n]['Name']] = 0
        number = randint(0,100)
        if district == cands[n]['District'] and number < max(cands[n]['District Name Rec'], cands[n]['State Name Rec'], cands[n]['Nat Name Rec']):
            scores[cands[n]['Name']] += cands[n]['D+']
            scores[cands[n]['Name']] += cands[n]['S+']
            for i in vtr:
                scores[cands[n]['Name']] += cands[n][vtr[i]]
        elif state == cands[n]['State'] and number < max(cands[n]['State Name Rec'], cands[n]['Nat Name Rec']):
            scores[cands[n]['Name']] += cands[n]['S+']
            for i in vtr:
                scores[cands[n]['Name']] += cands[n][vtr[i]]
        elif number < cands[n]['Nat Name Rec']:
            for i in vtr:
                scores[cands[n]['Name']] += cands[n][vtr[i]]
        else:
            scores[cands[n]['Name']] -= 20
        for i in vtr:
            scores[cands[n]['Name']] += natenv[cands[n]['Party']][vtr[i]] * natcorrelation
        if cands[n]['Party'] == 'Independent':
            scores[cands[n]['Name']] += (upballot[cands[n]['Party']] / 2) * natcorrelation
        else:
            scores[cands[n]['Name']] += upballot[cands[n]['Party']] * natcorrelation
        scores[cands[n]['Name']] += cands[n]['Momentum']
    if len(cands) == 2:
        n = 0
        for i in cands:
            if n == 0:
                x = cands[i]
                n += 1
            else:
                y = cands[i]
        scores[x['Name']] = 1 / (1 + np.e ** (-1/20 * (scores[x['Name']] - scores[y['Name']])))
        scores[y['Name']] = 1 - scores[x['Name']]
    else:
        for n in cands:
            scores[cands[n]['Name']] = 1 / (1 + np.e ** (-1/20 * scores[cands[n]['Name']])) ** (len(cands) - 0.5)
    x = random.choice(list(cands.keys()))
    normalize(scores, x)
    z = randint(0, 100) / 100
    result = x
    h = 0
    for n in scores:
        h += scores[n]
        if z <= h:
            result = n
            break
    return result


def voterlst(state, n):
    col_index(state)
    rematrix(state)
    state["Master Matrix"] = {}
    state['Targets'] = {"Republican": {}, "Democrat": {}, "Independent": {}}
    state['Totals'] = {}
    state['Sections'] = {"Republican": {}, "Democrat": {}, "Independent": {}}
    state['Proportions'] = {"Republican": {}, "Democrat": {}, "Independent": {}}
    state['Overall Targets'] = {"Republican": 0, "Democrat": 0, "Independent": 0}
    for i in state['Races']:
        state['Totals'][i] = 1
        for j in state['Parties']:
            adj = Races[i][j]
            if i in state['Race Adjustments']:
                if j in state['Race Adjustments'][i]:
                    adj += state['Race Adjustments'][i][j]
            state['Overall Targets'][j] += round(adj * state[i], 2)
            state['Targets'][j][i] = adj
            state['Sections'][j][i] = 0
            state['Proportions'][j][i] = 0
    targets = {}
    for i in Educations:
        state['Totals'][i] = 1
        for j in state['Parties']:
            targets[j] = 0
            z = state['Overall Targets'][j]
            if i == "No Degree":
                c = "Degree"
                r = 1 - state['Education']
            else:
                c = "No Degree"
                r = state['Education']
            q = Educations[c][j] / Educations[i][j]
            state['Targets'][j][i] = round(z / (q * (1 - r) + r), 2)
            state['Sections'][j][i] = 0
            state['Proportions'][j][i] = 0
    for i in Ideologies:
        state['Totals'][i] = 1
        for j in state['Parties']:
            targets[j] += Ideologies[i][j]
            state['Targets'][j][i] = Ideologies[i][j]
            state['Sections'][j][i] = 0
            state['Proportions'][j][i] = 0
    for i in Ideologies:
        for j in state['Parties']:
            state['Targets'][j][i] = round(Ideologies[i][j] + state[i] * (targets[j] - 3 * state['Overall Targets'][j]) / 3, 2)
    lst = []
    for i in state["R-E Matrix"]:
        state["Master Matrix"][i] = {}
        for j in state["R-E Matrix"][i]:
            state["Master Matrix"][i][j] = {}
            for k in state["R-E Matrix"][i][j]:
                state["Master Matrix"][i][j][k] = {}
                for q in state['Parties']:
                    state["Master Matrix"][i][j][k][q] = Races[i][q]
    for m in range(0, n):
        v = voter(state)
        r = randint(0, 100)
        h = 0
        for i in state['Parties']:
            h += state['Master Matrix'][v['Race']][v['Education']][v['Ideology']][i] * 100
            if r <= h:
                v['Party ID'] = i
                state['Sections'][i][v['Race']] += 1
                state['Sections'][i][v['Education']] += 1
                state['Sections'][i][v['Ideology']] += 1
                state['Totals'][v['Race']] += 1
                state['Totals'][v['Education']] += 1
                state['Totals'][v['Ideology']] += 1
                break
            v['Party ID'] = i
        lst.append(v)
        if m % 10 == 0:
            for i in state['Parties']:
                for j in state['Races']:
                    p = state['Sections'][i][j] / state['Totals'][j]
                    if p < state['Targets'][i][j]:
                        for k in Educations:
                            for l in Ideologies:
                                if state['Master Matrix'][j][k][l][i] < 0.99:
                                    state['Master Matrix'][j][k][l][i] += 0.01
                    elif p > state['Targets'][i][j]:
                        for k in Educations:
                            for l in Ideologies:
                                if state['Master Matrix'][j][k][l][i] > 0.01:
                                    state['Master Matrix'][j][k][l][i] -= 0.01
                for j in Educations:
                    p = state['Sections'][i][j] / state['Totals'][j]
                    if p < state['Targets'][i][j]:
                        for k in state['Races']:
                            for l in Ideologies:
                                if state['Master Matrix'][k][j][l][i] < 0.99:
                                    state['Master Matrix'][k][j][l][i] += 0.01
                    elif p > state['Targets'][i][j]:
                        for k in state['Races']:
                            for l in Ideologies:
                                if state['Master Matrix'][k][j][l][i] > 0.01:
                                    state['Master Matrix'][k][j][l][i] -= 0.01
                for j in Ideologies:
                    p = state['Sections'][i][j] / state['Totals'][j]
                    if p < state['Targets'][i][j]:
                        for k in state['Races']:
                            for l in Educations:
                                if state['Master Matrix'][k][l][j][i] < 0.99:
                                    state['Master Matrix'][k][l][j][i] += 0.01
                    elif p > state['Targets'][i][j]:
                        for k in state['Races']:
                            for l in Educations:
                                if state['Master Matrix'][k][l][j][i] > 0.01:
                                    state['Master Matrix'][k][l][j][i] -= 0.01
            for i in state["Master Matrix"]:
                for j in state["R-E Matrix"][i]:
                    for k in state["R-E Matrix"][i][j]:
                        normalize(state["Master Matrix"][i][j][k], 'Independent')
    del state['Targets']
    del state['Overall Targets']
    del state['Master Matrix']
    del state['ColIndex']
    del state['R-E Matrix']
    del state['Totals']
    del state['Sections']
    del state['Proportions']
    state['Voters'] = lst
    return lst


def district_election(cands, natcorrelation, natenv, state, district, modifier):
    votes = {}
    crosstabs = {}
    groups = [Races, Educations, Ideologies, Parties]
    for i in range(0, len(groups)):
        for n in groups[i]:
            crosstabs[n] = {}
            for z in cands:
                crosstabs[n][cands[z]['Name']] = 0
    for n in cands:
        votes[cands[n]['Name']] = 0
    for n in range(0, len(state['Districts'][district])):
        t = turnout(state['Districts'][district][n], {'MC': cands}, natenv, state['Name'], district, modifier)
        if t is True:
            v = vote(state['Districts'][district][n], cands, natcorrelation, natenv, state['Name'], district, Modifier)
            votes[v] += 1
            crosstabs[state['Districts'][district][n]['Race']][v] += 1
            crosstabs[state['Districts'][district][n]['Ideology']][v] += 1
            crosstabs[state['Districts'][district][n]['Education']][v] += 1
            crosstabs[state['Districts'][district][n]['Party ID']][v] += 1
    #vote_summary(votes)
    #summarize(crosstabs)
    return [votes, crosstabs]


def vote_summary(votes):
    for n in votes:
        print(n + ": " + str(round(votes[n] / sum(votes.values()) * 100, 1)) + "%")


def state_election(state, cands, natcorrelation, natenv, modifier):
    votes = {}
    crosstabs = {}
    groups = [Races, Educations, Ideologies, Parties]
    for i in range(0, len(groups)):
        for n in groups[i]:
            crosstabs[n] = {}
            for z in cands:
                crosstabs[n][cands[z]['Name']] = 0
    for i in state['Districts']:
        crosstabs[i] = {}
        for z in cands:
            crosstabs[i][cands[z]['Name']] = 0
    for n in cands:
        votes[cands[n]['Name']] = 0
    for n in state['Districts']:
        for i in range(0, len(state['Districts'][n])):
            t = turnout(state['Districts'][n][i], {'MC': cands}, natenv, state['Name'], n, modifier)
            if t is True:
                v = vote(state['Districts'][n][i], cands, natcorrelation, natenv, state['Name'], n, Modifier)
                votes[v] += 1
                crosstabs[state['Districts'][n][i]['Race']][v] += 1
                crosstabs[state['Districts'][n][i]['Ideology']][v] += 1
                crosstabs[state['Districts'][n][i]['Education']][v] += 1
                crosstabs[state['Districts'][n][i]['Party ID']][v] += 1
                crosstabs[n][v] += 1
    # vote_summary(votes)
    # summarize(crosstabs)
    return [votes, crosstabs]


def summarize(crosstabs):
    for n in crosstabs:
        print()
        print("Among " + n + " Voters")
        if sum(crosstabs[n].values()) == 0:
            print("N/A")
        else:
            for i in crosstabs[n]:
                print(i + ": " + str(round(crosstabs[n][i] / sum(crosstabs[n].values()) * 100, 1)) + "%")


def districts(state):
    voterlst(state, int(state['Population'] / 1000) + 1)
    state['District Facts'] = {}
    state['Districts'] = {}
    for i in range(1, state['CDs'] + 1):
        if state['CDs'] == 1 and i == 1:
            name = state['Abbrev'] + "-AL"
        elif i < 10:
            name = state['Abbrev'] + "-0" + str(i)
        else:
            name = state['Abbrev'] + "-" + str(i)
        state['Districts'][name] = []
        state['District Facts'][name] = {}
    buckets = {"Urban": [], "Suburban": [], "Rural": []}
    regions = {"Urban": Urban, "Suburban": Suburban, "Rural": Rural}
    for i in range(0, len(state['Voters'])):
        scores = {"Urban": 0, "Suburban": 0, "Rural": 0}
        for j in regions:
            for k in state['Voters'][i]:
                scores[j] += regions[j][state['Voters'][i][k]]
            scores[j] = 1 / (1 + np.e ** (-1/20 * scores[j])) ** 2.5
        normalize(scores, 'Suburban')
        z = randint(0, 100) / 100
        result = "Urban"
        h = 0
        for n in scores:
            h += scores[n]
            if z <= h:
                result = n
                break
        buckets[result].append(state['Voters'][i])
    n = int((len(state['Voters']) - 1) / state['CDs'])
    for i in state['Districts']:
        for z in range(1,5):
            type = randint(0,len(state['Voters']))
            if type < len(buckets['Urban']):
                type = 0
            elif type < len(buckets['Urban']) + len(buckets['Suburban']):
                type = 1
            else:
                type = 2
            if type == 0:
                for q in range(0, min(int(n / 4), len(buckets["Urban"]))):
                    state['Districts'][i].append(buckets["Urban"][q])
                    buckets['Urban'][q] = 0
                q = 0
                while q < len(buckets['Urban']):
                    if buckets['Urban'][q] == 0:
                        del buckets["Urban"][q]
                        q -= 1
                    q += 1
            elif type == 1:
                for q in range(0, min(int(n / 4), len(buckets["Suburban"]))):
                    state['Districts'][i].append(buckets["Suburban"][q])
                    buckets['Suburban'][q] = 0
                q = 0
                while q < len(buckets['Suburban']):
                    if buckets['Suburban'][q] == 0:
                        del buckets["Suburban"][q]
                        q -= 1
                    q += 1
            else:
                for q in range(0, min(int(n / 4), len(buckets["Rural"]))):
                    state['Districts'][i].append(buckets["Rural"][q])
                    buckets["Rural"][q] = 0
                q = 0
                while q < len(buckets['Rural']):
                    if buckets['Rural'][q] == 0:
                        del buckets["Rural"][q]
                        q -= 1
                    q += 1
    lst = []
    for i in buckets:
        for n in range(0, len(buckets[i])):
            lst.append(buckets[i][n])
    for i in state['Districts']:
        while len(state['Districts'][i]) < (len(state['Voters']) - 1) / state['CDs'] and len(lst) != 0:
            state['Districts'][i].append(lst[0])
            del lst[0]
    for i in state['Districts']:
        district_facts(i, state)
    state_facts(state)
    if state['CDs'] > 1:
        redistricting(state)


def generate_candidate(party, state, district):
    if state == 'RNG':
        n = randint(0, len(USA['States'].values()) - 1)
        k = 0
        for i in USA['States']:
            if k == n:
                state = USA['States'][i]
                break
            else:
                k += 1
    if district == 'RNG':
        x = randint(1, state['CDs'])
        if state['CDs'] == 1:
            d = state['Abbrev'] + "-AL"
        elif x < 10:
            d = state['Abbrev'] + "-0" + str(x)
        else:
            d = state['Abbrev'] + "-" + str(x)
    else:
        d = district
    candidate = {'Profile': 0, 'Momentum': 0, 'Senate Terms': 0, 'Governor Terms': 0, 'Terms': 0, 'Incumbent': False, "Age": randint(24, 75), "S+": np.random.normal(0.5, 4), "State": state['Name'], "District": d, "D+": np.random.normal(1, 4), "Party": party}
    first = First_Names[randint(0, len(First_Names) - 1)]
    last = Last_Names[randint(0, len(Last_Names) - 1)]
    if candidate['Party'] == 'Independent':
        candidate['Nat Name Rec'] = -110 + np.random.normal(0, 30)
    else:
        candidate['Nat Name Rec'] = -45 + np.random.normal(0, 10)
    if candidate['Party'] == 'Independent':
        candidate['State Name Rec'] = candidate['Nat Name Rec'] + np.random.normal(45 * (1/np.sqrt(state['CDs'])), 25)
    else:
        candidate['State Name Rec'] = candidate['Nat Name Rec'] + np.random.normal(35 * (1/np.sqrt(state['CDs'])), 10)
    if state['CDs'] == 1:
        candidate['District Name Rec'] = candidate['State Name Rec']
    elif candidate['Party'] == 'Independent':
        candidate['District Name Rec'] = candidate['State Name Rec'] + np.random.normal(15, 15)
    else:
        candidate['District Name Rec'] = candidate['State Name Rec'] + np.random.normal(20, 5)
    candidate['District Name Rec'] = 100 / (1 + np.e ** (-1 / 20 * (candidate['District Name Rec'])))
    candidate['State Name Rec'] = 100 / (1 + np.e ** (-1 / 20 * (candidate['State Name Rec'])))
    candidate['Nat Name Rec'] = 100 / (1 + np.e ** (-1 / 20 * (candidate['Nat Name Rec'])))
    candidate['Name'] = first + " " + last
    candidate['Mormon'] = np.random.normal(0, 15)
    candidate['White'] = np.random.normal(0, 6)
    candidate['Black'] = np.random.normal(0 - candidate['White'], 6)
    candidate['Hispanic'] = np.random.normal(0 - candidate['White'], 6)
    candidate['Asian'] = np.random.normal(0 - candidate['White'], 6)
    candidate['Native'] = np.random.normal(0 - candidate['White'], 6)
    candidate['Degree'] = np.random.normal(0, 6)
    candidate['No Degree'] = np.random.normal(0 - candidate['Degree'], 6)
    candidate['Degree'] += np.random.normal(0, 6)
    candidate['Republican'] = np.random.normal(0, 6)
    candidate['Democrat'] = np.random.normal(0 - candidate['Republican'], 6)
    if party == 'Republican':
        candidate['Independent'] = np.random.normal(0 - candidate['Republican'], 6)
    elif party == 'Democrat':
        candidate['Independent'] = np.random.normal(0 - candidate['Democrat'], 6)
    else:
        candidate['Independent'] = np.random.normal(0, 6)
    candidate['Republican'] += np.random.normal(0, 6)
    candidate['Conservative'] = np.random.normal(0, 6)
    candidate['Liberal'] = np.random.normal(0 - candidate['Conservative'], 6)
    candidate['Conservative'] = np.random.normal(0, 6)
    candidate['Moderate'] = np.random.normal(12 - abs(candidate['Conservative'] - candidate['Liberal']), 6)
    return candidate


def candidatelist(party, state, district, n):
    lst = []
    for i in range(0, n):
        lst.append(generate_candidate(party, state, district))
    return lst


def senators(state, party1, party2):
    state['Senator 1'] = generate_candidate(party1, state, 'RNG')
    if randint(0, 100) > 50:
        state['Senator 1']['Incumbent'] = True
        state['Senator 1']['S+'] += 4
        state['Senator 1']['State Name Rec'] += (100 - state['Senator 1']['State Name Rec']) * 0.9
    state['Senator 2'] = generate_candidate(party2, state, 'RNG')
    if randint(0, 100) > 50:
        state['Senator 2']['Incumbent'] = True
        state['Senator 2']['S+'] += 4
        state['Senator 2']['State Name Rec'] += (100 - state['Senator 2']['State Name Rec']) * 0.9
    state['Senator 1']['Senate Terms'] = 0
    state['Senator 2']['Senate Terms'] = 0


def prep(country):
    country['President'] = Donald_Trump
    pop = 0
    for i in country['States']:
        pop += country['States'][i]['Population']
    total = 0
    point = 0.1
    for i in country['States']:
        districts(country['States'][i])
        country['States'][i]['Electoral Votes'] = country['States'][i]['CDs'] + 2
        country['States'][i]['Delegates'] = country['States'][i]['Electoral Votes'] * 5
        if country['States'][i]['Name'] != "Washington DC":
            if country['States'][i]['Partisan Lean'] > 15:
                senators(country['States'][i], 'Democrat', 'Democrat')
            elif country['States'][i]['Partisan Lean'] < -15:
                senators(country['States'][i], 'Republican', 'Republican')
            else:
                if randint(0, 10) < 5:
                    senators(country['States'][i], 'Democrat', 'Republican')
                else:
                    senators(country['States'][i], 'Republican', 'Democrat')
            for z in country['States'][i]['District Facts']:
                if country['States'][i]['District Facts'][z]['Partisan Lean'] > -8.5:
                    country['States'][i]['District Facts'][z]['MC'] = generate_candidate('Democrat', country['States'][i], z)
                else:
                    country['States'][i]['District Facts'][z]['MC'] = generate_candidate('Republican', country['States'][i], z)
                if randint(0,100) > 25:
                    country['States'][i]['District Facts'][z]['MC']['Incumbent'] = True
                    country['States'][i]['District Facts'][z]['MC']['D+'] += randint(2,7)
                    country['States'][i]['District Facts'][z]['MC']['District Name Rec'] += (100 - country['States'][i]['District Facts'][z]['MC']['District Name Rec']) * 0.8
                    country['States'][i]['District Facts'][z]['MC']['Terms'] = abs(int(country['States'][i]['District Facts'][z]['MC']['D+'] / 3))
                else:
                    country['States'][i]['District Facts'][z]['MC']['Terms'] = 0
            if country['States'][i]['Partisan Lean'] > 0:
                country['States'][i]['Governor'] = generate_candidate('Democrat', country['States'][i], 'RNG')
            else:
                country['States'][i]['Governor'] = generate_candidate('Republican', country['States'][i], 'RNG')
            if randint(0, 100) > 50:
                country['States'][i]['Governor']['Incumbent'] = True
                country['States'][i]['Governor']['S+'] += 6
                country['States'][i]['Governor']['Governor Terms'] = 1
                country['States'][i]['Governor']['State Name Rec'] += (100 - country['States'][i]['Governor']['State Name Rec']) * 0.9
            country['States'][i]['Governor']['Governor Terms'] = 0
        total += country['States'][i]['Population']
        if total / pop > point:
            print("loading... " + str(int(point * 100)) + "%")
            point += 0.1
    country['States']['WV']['Senator 1'] = Joe_Manchin
    country['States']['CA']['Senator 1'] = Kamala_Harris
    country['States']['MN']['Senator 1'] = Amy_Klobuchar
    country['States']['VT']['Senator 1'] = Bernie_Sanders
    country['States']['MA']['Senator 1'] = Elizabeth_Warren
    country['States']['MT']['Senator 1'] = Jon_Tester
    country['States']['AL']['Senator 2'] = Doug_Jones
    country['States']['NY']['District Facts']['NY-25']['MC'] = Alexandra_Cortez
    country['States']['KS']['Governor'] = Laura_Kelly
    country['States']['NC']['Governor'] = Roy_Cooper
    country['States']['MI']['Governor'] = Gretchen_Whitmer
    country['States']['MN']['Governor'] = Tim_Walz
    country['States']['AZ']['Senator 2'] = Krysten_Sinema
    country['States']['OH']['Senator 2'] = Sherrod_Brown
    country['States']['ME']['Senator 1'] = Angus_King
    country['States']['ME']['Senator 2'] = Susan_Collins
    country['States']['LA']['Governor'] = John_Edwards
    country['States']['VA']['Governor'] = Ralph_Northam
    country['States']['MD']['Governor'] = Larry_Hogan
    country['States']['MA']['Governor'] = Charlie_Baker
    country['States']['WI']['Governor'] = Tony_Evers
    country['States']['PA']['Governor'] = Tom_Wolf
    country['States']['NV']['Senator 2'] = Jacky_Rosen
    country['States']['VA']['Senator 1'] = Tim_Kaine
    country['States']['WI']['Senator 2'] = Tammy_Baldwin
    country['States']['DE']['Senator 1'] = Tom_Carper
    country['States']['CT']['Senator 2'] = Chris_Murphy
    country['States']['RI']['Senator 1'] = Sheldon_Whitehouse
    country['States']['PA']['Senator 2'] = Bob_Casey
    country['States']['NM']['Senator 1'] = Martin_Heinrich
    country['States']['MI']['Senator 1'] = Debbie_Stabenow
    country['States']['WA']['Senator 2'] = Maria_Cantwell
    country['States']['CO']['Senator 2'] = Cory_Gardner
    country['States']['NC']['Senator 2'] = Thom_Tillis
    country['States']['TX']['Senator 1'] = Ted_Cruz
    country['States']['TX']['Senator 2'] = John_Cornyn
    country['States']['GA']['Senator 2'] = David_Perdue
    country['States']['IA']['Senator 2'] = Joni_Ernst
    country['States']['NJ']['Senator 1'] = Bob_Menendez
    country['States']['NH']['Senator 2'] = Jeanne_Shaheen
    country['States']['MI']['Senator 2'] = Gary_Peters
    country['States']['MN']['Senator 2'] = Tina_Smith
    country['States']['NM']['Senator 2'] = Tom_Udall
    country['States']['NJ']['Senator 2'] = Cory_Booker
    country['States']['VA']['Senator 2'] = Mark_Warner
    country['States']['IL']['Senator 2'] = Dick_Durbin
    country['States']['DE']['Senator 2'] = Chris_Coons
    country['States']['RI']['Senator 2'] = Jack_Reed
    country['States']['OR']['Senator 2'] = Jeff_Merkley
    country['States']['MT']['Senator 2'] = Steve_Daines
    country['States']['MS']['Senator 2'] = Cindy_Smith
    country['States']['IL']['Senator 1'] = Tammy_Duckworth
    country['States']['OR']['Senator 1'] = Ron_Wyden
    country['States']['WI']['Senator 1'] = Ron_Johnson
    country['States']['WA']['Senator 1'] = Patty_Murray
    country['States']['PA']['Senator 1'] = Pat_Toomey
    country['States']['NH']['Senator 1'] = Maggie_Hassan
    country['States']['FL']['Senator 1'] = Marco_Rubio
    country['States']['FL']['Senator 2'] = Rick_Scott
    country['States']['AZ']['Senator 1'] = Martha_McSally
    country['States']['NV']['Senator 1'] = Catherine_Masto
    country['States']['CO']['Senator 1'] = Michael_Bennet
    country['States']['IA']['Senator 1'] = Chuck_Grassley
    country['States']['CT']['Senator 1'] = Richard_Blumenthal
    country['States']['NC']['Senator 1'] = Richard_Burr
    country['States']['GA']['Senator 1'] = Johnny_Isakson
    country['States']['OH']['Senator 1'] = Rob_Portman
    country['States']['AK']['Senator 1'] = Lisa_Murkowski
    country['States']['AK']['Senator 2'] = Dan_Sullivan
    country['States']['SC']['Senator 1'] = Tim_Scott
    country['States']['SC']['Senator 2'] = Lindsey_Graham
    country['States']['MS']['Senator 1'] = Roger_Wicker
    country['States']['MO']['Senator 1'] = Roy_Blount
    country['States']['MO']['Senator 2'] = Josh_Hawley
    country['States']['IN']['Senator 1'] = Todd_Young
    country['States']['IN']['Senator 2'] = Mike_Braun
    country['States']['NY']['Senator 2'] = Kirsten_Gillibrand
    country['States']['LA']['Senator 1'] = John_Kennedy
    country['States']['LA']['Senator 2'] = Bill_Cassidy
    country['States']['KY']['Senator 1'] = Rand_Paul
    country['States']['KY']['Senator 2'] = Mitch_McConnell
    country['States']['UT']['Senator 1'] = Mike_Lee
    country['States']['UT']['Senator 2'] = Mitt_Romney


def district_facts(district, state):
    rep_id = 0
    dem_id = 0
    non_white = 0
    col_education = 0
    total = 0
    for n in range(0, len(state['Districts'][district]),5):
        total += 1
        if state['Districts'][district][n]['Race'] != 'White':
            non_white += 1
        if state['Districts'][district][n]['Party ID'] == 'Republican':
            rep_id += 1
        elif state['Districts'][district][n]['Party ID'] == 'Democrat':
            dem_id += 1
        if state['Districts'][district][n]['Education'] == 'Degree':
            col_education += 1
    PID = round((dem_id / total - rep_id / total) * 100, 1)
    if dem_id > rep_id:
        P_ID = color.BLUE + "D+" + str(round((dem_id / total - rep_id / total) * 100, 1)) + color.END
    else:
        P_ID = color.RED + "R+" + str(round((rep_id / total - dem_id / total) * 100, 1)) + color.END
    generic_d = 0
    generic_r = 0
    for i in range(0, 3):
        s = district_election({'Generic R': Generic_R, 'Generic D': Generic_D}, 1, Parties, state, district, 0)
        generic_d += s[0]['Generic D']
        generic_r += s[0]['Generic R']
    total2 = generic_d + generic_r
    if generic_d > generic_r:
        PVI = color.BLUE + "D+" + str(round((generic_d / total2 - generic_r / total2) * 100, 1)) + color.END
    else:
        PVI = color.RED + "R+" + str(round((generic_r / total2 - generic_d / total2) * 100, 1)) + color.END
    state['District Facts'][district]['Party ID'] = P_ID
    state['District Facts'][district]['PVI'] = PVI
    state['District Facts'][district]['PID'] = PID
    state['District Facts'][district]['NW'] = round(non_white / total * 100, 1)
    state['District Facts'][district]['Partisan Lean'] = round((generic_d / total2 - generic_r / total2) * 100, 1)
    state['District Facts'][district]['Degree'] = str(round(col_education / total * 100, 1)) + "%"
    state['District Facts'][district]['Non-White'] = str(round(non_white / total * 100, 1)) + "%"


def quick_facts(state):
    print(color.BOLD + state['Name'] + " Facts" + color.END)
    print("Party ID: " + state['Party ID'])
    print("538 PVI: " + state['PVI'])
    print("College Degree: " + state['Degree'])
    print("Non-White: " + state['Non-White'])


def dist_facts(state, district):
    print(color.BOLD + district + " Facts" + color.END)
    print("Party ID: " + state['District Facts'][district]['Party ID'])
    print("538 PVI: " + state['District Facts'][district]['PVI'])
    print("College Degree: " + state['District Facts'][district]['Degree'])
    print("Non-White: " + state['District Facts'][district]['Non-White'])


def state_facts(state):
    # rep_id = 0
    # dem_id = 0
    PL = 0
    PID = 0
    non_white = 0
    col_education = str(round(state['Education'] * 100, 1)) + "%"
    for i in state['District Facts']:
        non_white += state['District Facts'][i]['NW']
        PL += state['District Facts'][i]['Partisan Lean']
        PID += state['District Facts'][i]['PID']
    PL /= len(state['District Facts'])
    non_white /= len(state['District Facts'])
    PID /= len(state['District Facts'])
    if PID > 0:
        P_ID = color.BLUE + "D+" + str(round(PID, 1)) + color.END
    else:
        P_ID = color.RED + "R+" + str(round(-PID, 1)) + color.END
    # generic_d = 0
    # generic_r = 0
    # for i in range(0, 10):
    #     s = state_election(state, {'Generic D': Generic_D, 'Generic R': Generic_R}, 1, Parties, 0)
    #     generic_d += s[0]['Generic D']
    #     generic_r += s[0]['Generic R']
    # total2 = generic_d + generic_r
    # state['PVI'] = round((generic_d / total2 - generic_r / total2) * 100, 1)
    if PL > 0:
        PVI = color.BLUE + "D+" + str(round(PL, 1)) + color.END
    else:
        PVI = color.RED + "R+" + str(round(-PL, 1)) + color.END
    state['PVI'] = PVI
    state['Party ID'] = P_ID
    state['Degree'] = col_education
    state['Non-White'] = str(round(non_white, 1)) + "%"
    state['Partisan Lean'] = round(PL, 1)


def long_form(state):
    quick_facts(state)
    for i in state['Districts']:
        print()
        dist_facts(state, i)


def turnout(voter, ballot, natenv, state, district, modifier):
    base_percentage = (0.7 * Races[voter['Race']]['Turnout'] + 0.3 * Educations[voter['Education']]['Turnout']) / 100
    base_x = -20 * (np.log(1/base_percentage - 1)) + modifier
    for i in ballot:
        scores = []
        for n in ballot[i]:
            score = 0
            for x in voter:
                score += ballot[i][n][voter[x]] * 0.5 + natenv[ballot[i][n]['Party']][voter[x]] * 0.1
            if state == ballot[i][n]['State']:
                score += ballot[i][n]['S+'] * 0.5
            if district == ballot[i][n]['District']:
                score += ballot[i][n]['D+'] * 0.5
            scores.append(score)
        base_x += max(scores) * Turnout[i]
    probs = 1 / (1 + np.e ** (-1/20 * base_x))
    z = randint(0, 100) / 100
    if z <= probs:
        t = True
    else:
        t = False
    return t


def primary_summary(candidates, votes, state, party):
    winner = max(votes, key=votes.get)
    total = sum(list(votes.values()))
    print(Parties[party]['Color'] + winner + " won the " + state + " " + party + " primary with " + str(round((votes[winner] / total) * 100, 1)) + "% of the vote" + color.END)
    return candidates[winner]


def presprimary_summary(candidates, delegates, total_votes, votes, state, party, momentum):
    winner = max(votes, key=votes.get)
    momentum[winner] += state['CDs'] ** (1/3) / 2
    candidates[winner]['Nat Name Rec'] += (100 - candidates[winner]['Nat Name Rec']) * 0.5
    print(color.BOLD + winner + " won the " + party + " " + state['Name'] + " primary with " + str(round(votes[winner] / sum(votes.values()) * 100, 1)) + "% of the vote" + color.END)
    for n in votes:
        prop = votes[n] / sum(votes.values())
        momentum[n] += (prop ** 3) * state['CDs'] / 2
        d = int(prop * state['Delegates'])
        delegates[party][candidates[n]['Name']] += d
        total_votes[party][candidates[n]['Name']] += votes[n]
        candidates[n]['Nat Name Rec'] += (100 - candidates[n]['Nat Name Rec']) * prop
        print(candidates[n]['Name'] + " got " + str(round(prop*100, 1)) + "% of the vote, and is now at " + str(delegates[party][n]) + " delegates (+" + str(d) + ")")


def jungle_summary(candidates, votes, state):
    winner = max(votes, key=votes.get)
    max2 = 0
    m = votes[winner]
    for v in votes:
        if (votes[v] > max2 and votes[v] <= m) and v != winner:
            max2 = votes[v]
            second = v
    #second = list(votes.keys())[list(votes.values()).index(max2)]
    total = sum(list(votes.values()))
    print(Parties[candidates[winner]['Party']]['Color'] + winner + " [" + Parties[candidates[winner]['Party']]['Letter'] + "]" + color.END + " won the " + state + " jungle primary with " + str(round((votes[winner] / total) * 100, 1)) + "% of the vote," + " with " + Parties[candidates[second]['Party']]['Color']  + second + " [" + Parties[candidates[second]['Party']]['Letter'] + "]" + color.END + " coming second at " + str(round((votes[second] / total) * 100, 1)) + "% of the vote.")
    return {winner: candidates[winner], second: candidates[second]}


def primary(state, year, prescands, natenv, delegates, total_votes, momentum):
    test = False
    if year % 2 == 0:
        test = True
    if year % 6 in state['Senate Seats'] or year % 4 in state['Mansion Years']:
        test = True
    if prescands != 0:
        test = True
    if test == True:
        if year % 4 in state['Mansion Years']:
            g_primary = {}
            g_primary_votes = {}
            if state['Primary Type'] == 'Regular':
                for i in state['Parties']:
                    if i != 'Independent':
                        g_primary[i] = {}
                        g_primary_votes[i] = {}
        if year % 6 in state['Senate Seats']:
            s_primary = {}
            s_primary_votes = {}
            if state['Primary Type'] == 'Regular':
                for i in state['Parties']:
                    if i != 'Independent':
                        s_primary[i] = {}
                        s_primary_votes[i] = {}
        if year % 2 == 0:
            for x in state['District Facts']:
                state['District Facts'][x]['Primary'] = {}
                state['District Facts'][x]['Primary Votes'] = {}
                if state['Primary Type'] == 'Regular':
                    for i in state['Parties']:
                        if i != 'Independent':
                            state['District Facts'][x]['Primary'][i] = {}
                            state['District Facts'][x]['Primary Votes'][i] = {}
        if prescands != 0:
            prescands_votes = {}
            for i in state['Parties']:
                if i != 'Independent':
                    prescands_votes[i] = {}
                    for n in prescands[i]:
                        prescands_votes[i][n] = 0
        if state['Primary Type'] == 'Regular':
            for i in state['Parties']:
                if i != 'Independent':
                    if year % 4 in state['Mansion Years']:
                        if state['Governor']['Party'] == i and state['Governor']['Incumbent'] is True:
                            g_primary[i][state['Governor']['Name']] = state['Governor']
                            g_primary_votes[i][state['Governor']['Name']] = 0
                            if state['Governor'][state['Governor']['Party']] < 2:
                                threshold = 90
                            elif state['Governor'][state['Governor']['Party']] < 6:
                                threshold = 50
                            else:
                                threshold = 10
                            if randint(0, 100) < threshold:
                                cand = generate_candidate(i, state, 'RNG')
                                g_primary[i][cand['Name']] = cand
                                g_primary_votes[i][cand['Name']] = 0
                        else:
                            if state['Governor']['Party'] == i:
                                g_primary[i][state['Governor']['Name']] = state['Governor']
                                g_primary_votes[i][state['Governor']['Name']] = 0
                            for z in state['District Facts']:
                                if state['District Facts'][z]['MC']['Party'] == i:
                                    r = randint(0, 5)
                                    r *= state['CDs'] ** (1/2)
                                    if state['District Facts'][z]['MC']['Profile'] > r:
                                        mem = state['District Facts'][z]['MC']
                                        g_primary[i][mem['Name']] = mem
                                        g_primary_votes[i][mem['Name']] = 0
                                        state['District Facts'][z]['MC'] = generate_candidate(i, state, z)
                            if len(g_primary[i]) < 3:
                                for x in range(0, randint(1, 4)):
                                    cand = generate_candidate(i, state, 'RNG')
                                    g_primary[i][cand['Name']] = cand
                                    g_primary_votes[i][cand['Name']] = 0
                            else:
                                for x in range(0, randint(0, 2)):
                                    cand = generate_candidate(i, state, 'RNG')
                                    g_primary[i][cand['Name']] = cand
                                    g_primary_votes[i][cand['Name']] = 0
                    if year % 6 in state['Senate Seats']:
                        if year % 6 == state['Senate Seats'][0]:
                            sen = 'Senator 1'
                        else:
                            sen = 'Senator 2'
                        if state[sen]['Party'] == i and state[sen]['Incumbent'] is True:
                            s_primary[i][state[sen]['Name']] = state[sen]
                            s_primary_votes[i][state[sen]['Name']] = 0
                            if state[sen][state[sen]['Party']] < 2:
                                threshold = 90
                            elif state[sen][state[sen]['Party']] < 6:
                                threshold = 50
                            else:
                                threshold = 10
                            if randint(0, 100) < threshold:
                                cand = generate_candidate(i, state, 'RNG')
                                s_primary[i][cand['Name']] = cand
                                s_primary_votes[i][cand['Name']] = 0
                        else:
                            if state[sen]['Party'] == i:
                                s_primary[i][state[sen]['Name']] = state[sen]
                                s_primary_votes[i][state[sen]['Name']] = 0
                            for z in state['District Facts']:
                                if state['District Facts'][z]['MC']['Party'] == i:
                                    r = randint(0, 5)
                                    r *= state['CDs'] ** (1/2)
                                    if state['District Facts'][z]['MC']['Profile'] > r:
                                        mem = state['District Facts'][z]['MC']
                                        s_primary[i][mem['Name']] = mem
                                        s_primary_votes[i][mem['Name']] = 0
                                        state['District Facts'][z]['MC'] = generate_candidate(i, state, z)
                            if len(s_primary[i]) < 3:
                                for x in range(0, randint(1, 4)):
                                    cand = generate_candidate(i, state, 'RNG')
                                    s_primary[i][cand['Name']] = cand
                                    s_primary_votes[i][cand['Name']] = 0
                            else:
                                for x in range(0, randint(0, 2)):
                                    cand = generate_candidate(i, state, 'RNG')
                                    s_primary[i][cand['Name']] = cand
                                    s_primary_votes[i][cand['Name']] = 0
                    if year % 2 == 0 and state['Name'] != "Washington DC":
                        for z in state['District Facts']:
                            MC = state['District Facts'][z]['MC']
                            prim = state['District Facts'][z]['Primary'][i]
                            prim_votes = state['District Facts'][z]['Primary Votes'][i]
                            if MC['Party'] == i and MC['Incumbent'] is True:
                                prim[MC['Name']] = MC
                                prim_votes[MC['Name']] = 0
                                if randint(0, 100) < 10:
                                    cand = generate_candidate(i, state, z)
                                    prim[cand['Name']] = cand
                                    prim_votes[cand['Name']] = 0
                            else:
                                if MC['Party'] == i:
                                    prim[MC['Name']] = MC
                                    prim_votes[MC['Name']] = 0
                                if len(prim) < 3:
                                    for x in range(0, randint(1, 4)):
                                        cand = generate_candidate(i, state, z)
                                        prim[cand['Name']] = cand
                                        prim_votes[cand['Name']] = 0
                                else:
                                    for x in range(0, randint(0, 2)):
                                        cand = generate_candidate(i, state, z)
                                        prim[cand['Name']] = cand
                                        prim_votes[cand['Names']] = 0
        elif state['Primary Type'] == 'Jungle':
            for i in state['Parties']:
                if year % 4 in state['Mansion Years']:
                    if state['Governor']['Party'] == i and state['Governor']['Incumbent'] is True:
                        g_primary[state['Governor']['Name']] = state['Governor']
                        g_primary_votes[state['Governor']['Name']] = 0
                        if randint(0, 100) < 10:
                            cand = generate_candidate(i, state, 'RNG')
                            g_primary[cand['Name']] = cand
                            g_primary_votes[cand['Name']] = 0
                    else:
                        amount = 0
                        if state['Governor']['Party'] == i:
                            g_primary[state['Governor']['Name']] = state['Governor']
                            g_primary_votes[state['Governor']['Name']] = 0
                            amount += 1
                        for z in state['District Facts']:
                            if state['District Facts'][z]['MC']['Party'] == i:
                                r = randint(0, 5)
                                r *= state['CDs'] ** (1/2)
                                if state['District Facts'][z]['MC']['Profile'] > r:
                                    mem = state['District Facts'][z]['MC']
                                    g_primary[mem['Name']] = mem
                                    g_primary_votes[mem['Name']] = 0
                                    state['District Facts'][z]['MC'] = generate_candidate(i, state, z)
                                    amount += 1
                        if amount < 2:
                            for x in range(0, randint(1,2)):
                                cand = generate_candidate(i, state, 'RNG')
                                g_primary[cand['Name']] = cand
                                g_primary_votes[cand['Name']] = 0
                        else:
                            for x in range(0, randint(0,1)):
                                cand = generate_candidate(i, state, 'RNG')
                                g_primary[cand['Name']] = cand
                                g_primary_votes[cand['Name']] = 0
                if year % 6 in state['Senate Seats']:
                    if year % 6 == state['Senate Seats'][0]:
                        sen = 'Senator 1'
                    else:
                        sen = 'Senator 2'
                    if state[sen]['Party'] == i and state[sen]['Incumbent'] is True:
                        s_primary[state[sen]['Name']] = state[sen]
                        s_primary_votes[state[sen]['Name']] = 0
                        if randint(0, 100) < 10:
                            cand = generate_candidate(i, state, 'RNG')
                            s_primary[cand['Name']] = cand
                            s_primary_votes[cand['Name']] = 0
                    else:
                        amount = 0
                        if state[sen]['Party'] == i:
                            s_primary[state[sen]['Name']] = state[sen]
                            s_primary_votes[state[sen]['Name']] = 0
                            amount += 1
                        for z in state['District Facts']:
                            if state['District Facts'][z]['MC']['Party'] == i:
                                r = randint(0, 5)
                                r *= state['CDs'] ** (1/2)
                                if state['District Facts'][z]['MC']['Profile'] > r:
                                    mem = state['District Facts'][z]['MC']
                                    s_primary[mem['Name']] = mem
                                    s_primary_votes[mem['Name']] = 0
                                    state['District Facts'][z]['MC'] = generate_candidate(i, state, z)
                                    amount += 1
                        if amount < 2:
                            for x in range(0, randint(1,2)):
                                cand = generate_candidate(i, state, 'RNG')
                                s_primary[cand['Name']] = cand
                                s_primary_votes[cand['Name']] = 0
                        else:
                            for x in range(0, randint(0,1)):
                                cand = generate_candidate(i, state, 'RNG')
                                s_primary[cand['Name']] = cand
                                s_primary_votes[cand['Name']] = 0
                if year % 2 == 0 and state['Name'] != "Washington DC":
                    for z in state['District Facts']:
                        MC = state['District Facts'][z]['MC']
                        prim = state['District Facts'][z]['Primary']
                        prim_votes = state['District Facts'][z]['Primary Votes']
                        if MC['Party'] == i and MC['Incumbent'] is True:
                            prim[MC['Name']] = MC
                            prim_votes[MC['Name']] = 0
                            if randint(0, 100) < 10:
                                cand = generate_candidate(i, state, z)
                                prim[cand['Name']] = cand
                                prim_votes[cand['Name']] = 0
                        else:
                            amount = 0
                            if MC['Party'] == i:
                                prim[MC['Name']] = MC
                                prim_votes[MC['Name']] = 0
                                amount += 1
                            if amount == 0:
                                for x in range(0, randint(1,2)):
                                    cand = generate_candidate(i, state, z)
                                    prim[cand['Name']] = cand
                                    prim_votes[cand['Name']] = 0
                            else:
                                for x in range(0, randint(0,1)):
                                    cand = generate_candidate(i, state, z)
                                    prim[cand['Name']] = cand
                                    prim_votes[cand['Name']] = 0
        if state['Primary Type'] == 'Regular':
            ballot = {}
            a = 0
            b = 0
            for n in state['Districts']:
                for i in state['Districts'][n]:
                    if i['Party ID'] != 'Independent':
                        party = i['Party ID']
                    else:
                        party = vote(i, {'Republican': Generic_R, 'Democrat': Generic_D}, 1, Parties, state, n, Modifier)
                        if party == 'Generic D':
                            party = 'Democrat'
                        else:
                            party = 'Republican'
                    if i['Party ID'] != 'Independent' or state['Open Primary'] is True:
                        if prescands != 0:
                            ballot['President'] = prescands[party]
                        if year % 4 in state['Mansion Years']:
                            ballot['Governor'] = g_primary[party]
                        if year % 6 in state['Senate Seats']:
                            ballot['Senator'] = s_primary[party]
                        if year % 2 == 0 and state['Name'] != "Washington DC":
                            ballot['MC'] = state['District Facts'][n]['Primary'][party]
                        t = turnout(i, ballot, natenv, state['Name'], n, -30)
                        b += 1
                        if t is True:
                            a += 1
                            if year % 2 == 0 and state['Name'] != "Washington DC":
                                v = vote(i, state['District Facts'][n]['Primary'][party], 0, natenv, state['Name'], n, Modifier)
                                state['District Facts'][n]['Primary Votes'][party][v] += 1
                            if year % 4 in state['Mansion Years']:
                                v = vote(i, g_primary[party], 0, natenv, state['Name'], n, Modifier)
                                g_primary_votes[party][v] += 1
                            if year % 6 in state['Senate Seats']:
                                v = vote(i, s_primary[party], 0, natenv, state['Name'], n, Modifier)
                                s_primary_votes[party][v] += 1
                            if prescands != 0:
                                v = vote(i, prescands[party], 0, natenv, state['Name'], n, Modifier)
                                prescands_votes[party][v] += 1
        elif state['Primary Type'] == 'Jungle':
            ballot = {}
            a = 0
            b = 0
            for n in state['Districts']:
                for i in state['Districts'][n]:
                    if prescands != 0 and i['Party ID'] != 'Independent':
                        ballot['President'] = prescands[i['Party ID']]
                    if year % 4 in state['Mansion Years']:
                        ballot['Governor'] = g_primary
                    if year % 6 in state['Senate Seats']:
                        ballot['Senator'] = s_primary
                    if year % 2 == 0 and state['Name'] != "Washington DC":
                        ballot['MC'] = state['District Facts'][n]['Primary']
                    t = turnout(i, ballot, natenv, state['Name'], n, -30)
                    b += 1
                    if t is True:
                        a += 1
                        if year % 2 == 0 and state['Name'] != "Washington DC":
                            v = vote(i, state['District Facts'][n]['Primary'], 1, natenv, state['Name'], n, Modifier)
                            state['District Facts'][n]['Primary Votes'][v] += 1
                        if year % 4 in state['Mansion Years']:
                            v = vote(i, g_primary, 0.5, natenv, state['Name'], n, Modifier)
                            g_primary_votes[v] += 1
                        if year % 6 in state['Senate Seats']:
                            v = vote(i, s_primary, 0.75, natenv, state['Name'], n, Modifier)
                            s_primary_votes[v] += 1
                        if prescands != 0 and i['Party ID'] != 'Independent':
                            v = vote(i, prescands[i['Party ID']], 0, natenv, state['Name'], n, Modifier)
                            prescands_votes[i['Party ID']][v] += 1
        print()
        print(color.BOLD + state['Name'] + " Primary Results" + color.END)
        if state['Primary Type'] == 'Regular':
            if year % 2 == 0 and state['Name'] != "Washington DC":
                print()
                print("House Results")
                for n in state['Districts']:
                    print()
                    state['District Facts'][n]['House'] = {}
                    for i in state['Parties']:
                        if i != 'Independent':
                            w = primary_summary(state['District Facts'][n]['Primary'][i], state['District Facts'][n]['Primary Votes'][i], n, i)
                            state['District Facts'][n]['House'][w['Name']] = w
                    if state['District Facts'][n]['MC']['Party'] == 'Independent':
                        MC = state['District Facts'][n]['MC']
                        state['District Facts'][n]['House'][MC['Name']] = MC
                    for i in state['District Facts'][n]['House']:
                        state['District Facts'][n]['House'][i]['District Name Rec'] += (100 - state['District Facts'][n]['House'][i]['District Name Rec']) * 0.5
                        state['District Facts'][n]['House'][i]['State Name Rec'] += (100 - state['District Facts'][n]['House'][i]['State Name Rec']) * 0.2
                        state['District Facts'][n]['House'][i]['Nat Name Rec'] += (100 - state['District Facts'][n]['House'][i]['Nat Name Rec']) * 0.05
                        shift = np.random.normal(0, 3)
                        if shift > 6:
                            print(color.BOLD + state['District Facts'][n]['House'][i]['Name'] + " is experiencing a surge of support." + color.END)
                        elif shift < -6:
                            print(color.BOLD + state['District Facts'][n]['House'][i]['Name'] + " has been hit by a major scandal." + color.END)
                        state['District Facts'][n]['House'][i]['Degree'] += shift / 2
                        state['District Facts'][n]['House'][i]['No Degree'] += shift / 2
                        state['District Facts'][n]['House'][i]['S+'] += shift
                        state['District Facts'][n]['House'][i]['D+'] += shift
            if year % 4 in state['Mansion Years']:
                print()
                print("Gubernatorial Results")
                print()
                state['Governor Candidates'] = {}
                for i in state['Parties']:
                    if i != 'Independent':
                        w = primary_summary(g_primary[i],g_primary_votes[i], state['Name'], i)
                        if w != state['Governor']:
                            w['Governor Terms'] = 0
                        state['Governor Candidates'][w['Name']] = w
                if state['Governor']['Party'] == 'Independent':
                    state['Governor Candidates'][state['Governor']['Name']] = state['Governor']
                for i in state['Governor Candidates']:
                    state['Governor Candidates'][i]['District Name Rec'] += (100 - state['Governor Candidates'][i]['District Name Rec']) * 0.75
                    state['Governor Candidates'][i]['State Name Rec'] += (100 - state['Governor Candidates'][i]['State Name Rec']) * 0.75
                    state['Governor Candidates'][i]['Nat Name Rec'] += (100 - state['Governor Candidates'][i]['Nat Name Rec']) * 0.1
                    shift = np.random.normal(0, 3)
                    if shift > 6:
                        print(color.BOLD + state['Governor Candidates'][i][
                            'Name'] + " is experiencing a surge of support." + color.END)
                    elif shift < -6:
                        print(color.BOLD + state['Governor Candidates'][i][
                            'Name'] + " has been hit by a major scandal." + color.END)
                    state['Governor Candidates'][i]['Degree'] += shift / 2
                    state['Governor Candidates'][i]['No Degree'] += shift / 2
                    state['Governor Candidates'][i]['S+'] += shift
                    state['Governor Candidates'][i]['D+'] += shift
            if year % 6 in state['Senate Seats']:
                print()
                print('Senate Results')
                print()
                state['Senate Candidates'] = {}
                for i in state['Parties']:
                    if i != 'Independent':
                        w = primary_summary(s_primary[i], s_primary_votes[i], state['Name'], i)
                        if w != state[sen]:
                            w['Senate Terms'] = 0
                        state['Senate Candidates'][w['Name']] = w
                if state[sen]['Party'] == 'Independent':
                    state['Senate Candidates'][state[sen]['Name']] = state[sen]
                for i in state['Senate Candidates']:
                    state['Senate Candidates'][i]['District Name Rec'] += (100 - state['Senate Candidates'][i]['District Name Rec']) * 0.75
                    state['Senate Candidates'][i]['State Name Rec'] += (100 - state['Senate Candidates'][i]['State Name Rec']) * 0.75
                    state['Senate Candidates'][i]['Nat Name Rec'] += (100 - state['Senate Candidates'][i]['Nat Name Rec']) * 0.1
                    shift = np.random.normal(0, 3)
                    if shift > 6:
                        print(color.BOLD + state['Senate Candidates'][i][
                            'Name'] + " is experiencing a surge of support." + color.END)
                    elif shift < -6:
                        print(color.BOLD + state['Senate Candidates'][i][
                            'Name'] + " has been hit by a major scandal." + color.END)
                    state['Senate Candidates'][i]['Degree'] += shift / 2
                    state['Senate Candidates'][i]['No Degree'] += shift / 2
                    state['Senate Candidates'][i]['S+'] += shift
                    state['Senate Candidates'][i]['D+'] += shift
            if prescands != 0:
                print()
                print('Presidential Primary Results')
                print()
                for i in state['Parties']:
                    if i != 'Independent':
                        presprimary_summary(prescands[i], delegates, total_votes, prescands_votes[i], state, i, momentum[i])
            print()
            print("Turnout: " + str(round(a/b * 100, 1)) + "%")
        elif state['Primary Type'] == 'Jungle':
            if year % 2 == 0 and state['Name'] != "Washington DC":
                print()
                print("House Results")
                print()
                for n in state['Districts']:
                    state['District Facts'][n]['House'] = jungle_summary(state['District Facts'][n]['Primary'], state['District Facts'][n]['Primary Votes'], n)
                    for i in state['District Facts'][n]['House']:
                        state['District Facts'][n]['House'][i]['District Name Rec'] += (100 - state['District Facts'][n]['House'][i]['District Name Rec']) * 0.75
                        state['District Facts'][n]['House'][i]['State Name Rec'] += (100 - state['District Facts'][n]['House'][i]['State Name Rec']) * 0.2
                        state['District Facts'][n]['House'][i]['Nat Name Rec'] += (100 - state['District Facts'][n]['House'][i]['Nat Name Rec']) * 0.05
                        shift = np.random.normal(0, 3)
                        if shift > 6:
                            print(color.BOLD + state['District Facts'][n]['House'][i][
                                'Name'] + " is experiencing a surge of support." + color.END)
                        elif shift < -6:
                            print(color.BOLD + state['District Facts'][n]['House'][i][
                                'Name'] + " has been hit by a major scandal." + color.END)
                        state['District Facts'][n]['House'][i]['Degree'] += shift / 2
                        state['District Facts'][n]['House'][i]['No Degree'] += shift / 2
                        state['District Facts'][n]['House'][i]['S+'] += shift
                        state['District Facts'][n]['House'][i]['D+'] += shift
            if year % 4 in state['Mansion Years']:
                print()
                print("Gubernatorial Results")
                print()
                state['Governor Candidates'] = jungle_summary(g_primary, g_primary_votes, state['Name'])
                for i in state['Governor Candidates']:
                    state['Governor Candidates'][i]['District Name Rec'] += (100 - state['Governor Candidates'][i]['District Name Rec']) * 0.75
                    state['Governor Candidates'][i]['State Name Rec'] += (100 - state['Governor Candidates'][i]['State Name Rec']) * 0.75
                    state['Governor Candidates'][i]['Nat Name Rec'] += (100 - state['Governor Candidates'][i]['Nat Name Rec']) * 0.1
                    shift = np.random.normal(0, 3)
                    if shift > 6:
                        print(color.BOLD + state['Governor Candidates'][i][
                            'Name'] + " is experiencing a surge of support." + color.END)
                    elif shift < -6:
                        print(color.BOLD + state['Governor Candidates'][i][
                            'Name'] + " has been hit by a major scandal." + color.END)
                    state['Governor Candidates'][i]['Degree'] += shift / 2
                    state['Governor Candidates'][i]['No Degree'] += shift / 2
                    state['Governor Candidates'][i]['S+'] += shift
                    state['Governor Candidates'][i]['D+'] += shift
            if year % 6 in state['Senate Seats']:
                print()
                print('Senate Results')
                print()
                state['Senate Candidates'] = jungle_summary(s_primary, s_primary_votes, state['Name'])
                for i in state['Senate Candidates']:
                    state['Senate Candidates'][i]['District Name Rec'] += (100 - state['Senate Candidates'][i]['District Name Rec']) * 0.75
                    state['Senate Candidates'][i]['State Name Rec'] += (100 - state['Senate Candidates'][i]['State Name Rec']) * 0.75
                    state['Senate Candidates'][i]['Nat Name Rec'] += (100 - state['Senate Candidates'][i]['Nat Name Rec']) * 0.1
                    shift = np.random.normal(0, 3)
                    if shift > 6:
                        print(color.BOLD + state['Senate Candidates'][i][
                            'Name'] + " is experiencing a surge of support." + color.END)
                    elif shift < -6:
                        print(color.BOLD + state['Senate Candidates'][i][
                            'Name'] + " has been hit by a major scandal." + color.END)
                    state['Senate Candidates'][i]['Degree'] += shift / 2
                    state['Senate Candidates'][i]['No Degree'] += shift / 2
                    state['Senate Candidates'][i]['S+'] += shift
                    state['Senate Candidates'][i]['D+'] += shift
            if prescands != 0:
                print()
                print('Presidential Primary Results')
                print()
                for i in state['Parties']:
                    if i != 'Independent':
                        presprimary_summary(prescands[i], delegates, total_votes, prescands_votes[i], state, i, momentum[i])
            print()
            print("Turnout: " + str(round(a/b * 100, 1)) + "%")


def results_summary(state, district, cands, votes, type):
    winner = max(votes, key=votes.get)
    x = votes[winner]
    total = sum(list(votes.values()))
    first = str(round(votes[winner] / total * 100, 1)) + "% " + color.END + "- " + Parties[cands[winner]['Party']]['Color']
    votes[winner] = 0
    loss = max(votes, key=votes.get)
    margin = x - votes[loss]
    second = Parties[cands[loss]['Party']]['Color'] + str(round(votes[loss] / total * 100, 1)) + "% " + color.END + "("
    if type == 'MC':
        incumbent = state['District Facts'][district][type]
        if incumbent['Party'] != cands[winner]['Party']:
            print(Parties[cands[winner]['Party']]['Color'] + cands[winner]['Name'] + " won the " + district + " election, " + first + second + color.END + Parties[incumbent['Party']]['Color'] + Parties[incumbent['Party']]['Letter'] + color.END + ">" + Parties[cands[winner]['Party']]['Color'] + Parties[cands[winner]['Party']]['Letter'] + color.END + ")")
        else:
            print(Parties[cands[winner]['Party']]['Color'] + cands[winner]['Name'] + " won the " + district + " election, " + first + second + Parties[incumbent['Party']]['Color'] + Parties[incumbent['Party']]['Letter'] + " Hold" + color.END + ")")
        state['District Facts'][district]['MC'] = cands[winner]
        state['District Facts'][district]['MC']['Terms'] += 1
        state['District Facts'][district]['MC']['D+'] += 2 / (state['District Facts'][district]['MC']['Terms'] ** 2)
        state['District Facts'][district]['MC']['S+'] += (3 / np.sqrt(state['CDs'])) / (state['District Facts'][district]['MC']['Terms'] ** 2)
        state['District Facts'][district]['MC']['Profile'] += 3
        state['District Facts'][district]['MC']['District Name Rec'] += (100 - state['District Facts'][district]['MC']['District Name Rec']) * 0.75
        state['District Facts'][district]['MC']['State Name Rec'] += (100 - state['District Facts'][district]['MC']['State Name Rec']) * 0.5
        state['District Facts'][district]['MC']['Nat Name Rec'] += (100 - state['District Facts'][district]['MC']['Nat Name Rec']) * 0.1
        cands[winner]['Incumbent'] = True
    else:
        incumbent = state[type]
        if type == 'Senator 1' or type == 'Senator 2':
            office = 'Senate'
        else:
            office = type
        if incumbent['Party'] != cands[winner]['Party']:
            print(Parties[cands[winner]['Party']]['Color'] + cands[winner]['Name'] + " won the " + state['Name'] + " (" + office + ")" + " election, " + first + second + color.END + Parties[incumbent['Party']]['Color'] + Parties[incumbent['Party']]['Letter'] + color.END + ">" + Parties[cands[winner]['Party']]['Color'] + Parties[cands[winner]['Party']]['Letter'] + color.END + ")")
        else:
            print(Parties[cands[winner]['Party']]['Color'] + cands[winner]['Name'] + " won the " + state['Name'] + " (" + office + ")" + " election, " + first + second + Parties[incumbent['Party']]['Color'] + Parties[incumbent['Party']]['Letter'] + " Hold" + color.END + ")")
        state[type] = cands[winner]
        if office == 'Senate':
            state[type]['Senate Terms'] += 1
            state[type]['S+'] += 4 / (state[type]['Senate Terms'] ** 2)
            state[type]['Profile'] += 8
            state[type]['District Name Rec'] += (100 - state[type]['District Name Rec']) * 0.8
            state[type]['State Name Rec'] += (100 - state[type]['State Name Rec']) * 0.8
            state[type]['Nat Name Rec'] += (100 - state[type]['Nat Name Rec']) * 0.25
        elif office == 'Governor':
            state[type]['Governor Terms'] += 1
            state[type]['S+'] += 6 / (state[type]['Governor Terms'] ** 2)
            state[type]['Profile'] += 5 + state['CDs'] / 10
            state[type]['District Name Rec'] += (100 - state[type]['District Name Rec']) * 0.8
            state[type]['State Name Rec'] += (100 - state[type]['State Name Rec']) * 0.8
            state[type]['Nat Name Rec'] += (100 - state[type]['Nat Name Rec']) * 0.15
        cands[winner]['Incumbent'] = True
    return cands[winner]


def general(state, year, prescands, natenv, results):
    test = False
    if year % 2 == 0 and state['Name'] != "Washington DC":
        test = True
    if year % 6 in state['Senate Seats'] or year % 4 in state['Mansion Years']:
        test = True
    if prescands != 0:
        test = True
    if test == True:
        ballot = {}
        if year % 2 == 0:
            c_votes = {}
            c_seats = {}
            for i in state['Parties']:
                c_votes[i] = 0
                c_seats[i] = 0
        a = 0
        b = 0
        rep_tot = 0
        rep_in = 0
        dem_tot = 0
        dem_in = 0
        ind_tot = 0
        ind_in = 0
        if prescands != 0:
            ballot['President'] = prescands
            pres_votes = {}
            for i in prescands:
                pres_votes[i] = 0
        if year % 4 in state['Mansion Years']:
            ballot['Governor'] = state['Governor Candidates']
            g_votes = {}
            for i in state['Governor Candidates']:
                g_votes[i] = 0
        if year % 6 in state['Senate Seats']:
            ballot['Senator'] = state['Senate Candidates']
            s_votes = {}
            for i in state['Senate Candidates']:
                s_votes[i] = 0
        if year % 2 == 0 and state['Name'] != "Washington DC":
            for x in state['District Facts']:
                state['District Facts'][x]['MC Votes'] = {}
                for i in state['District Facts'][x]['House']:
                        state['District Facts'][x]['MC Votes'][i] = 0
        for n in state['Districts']:
            if year % 2 == 0 and state['Name'] != "Washington DC":
                ballot['MC'] = state['District Facts'][n]['House']
            for i in state['Districts'][n]:
                if i['Party ID'] == 'Democrat':
                    dem_tot += 1
                elif i['Party ID'] == 'Republican':
                    rep_tot += 1
                else:
                    ind_tot += 1
                a += 1
                if year % 4 == 0:
                    t = turnout(i, ballot, natenv, state['Name'], state['Districts'][n], -10)
                else:
                    t = turnout(i, ballot, natenv, state['Name'], state['Districts'][n], -15)
                if t is True:
                    mod = copy.copy(Modifier)
                    if i['Party ID'] == 'Democrat':
                        dem_in += 1
                    elif i['Party ID'] == 'Republican':
                        rep_in += 1
                    else:
                        ind_in += 1
                    b += 1
                    if prescands != 0:
                        v = vote(i, prescands, 1, natenv, state['Name'], n, mod)
                        mod[prescands[v]['Party']] += 35
                        pres_votes[v] += 1
                        results['Popular Vote'][v] += 1
                    if year % 4 in state['Mansion Years']:
                        v = vote(i, state['Governor Candidates'], 0.5, natenv, state['Name'], n, mod)
                        mod[state['Governor Candidates'][v]['Party']] += 10
                        g_votes[v] += 1
                    if year % 6 in state['Senate Seats']:
                        v = vote(i, state['Senate Candidates'], 0.75, natenv, state['Name'], n, mod)
                        mod[state['Senate Candidates'][v]['Party']] += 5
                        s_votes[v] += 1
                    if year % 2 == 0 and state['Name'] != "Washington DC":
                        v = vote(i, ballot['MC'], 1, natenv, state['Name'], n, mod)
                        state['District Facts'][n]['MC Votes'][v] += 1
                        results['Generic Congressional Ballot'][ballot['MC'][v]['Party']] += 1
                        c_votes[ballot['MC'][v]['Party']] += 1
        print()
        print("Election Results for " + state['Name'])
        if year % 2 == 0 and state['Name'] != "Washington DC":
            print()
            for i in state['District Facts']:
                results_summary(state, i, state['District Facts'][i]['House'], state['District Facts'][i]['MC Votes'], 'MC')
                c_seats[state['District Facts'][i]['MC']['Party']] += 1
        if year % 4 in state['Mansion Years']:
            print()
            print("Gubernatorial Results (" + state['Name'] + ")")
            results_summary(state, 0, state['Governor Candidates'], g_votes, 'Governor')
        if state['Name'] != "Washington DC" and year % 6 == state['Senate Seats'][0]:
            print()
            print("Senate Results (" + state['Name'] + ")")
            results_summary(state, 0, state['Senate Candidates'], s_votes, 'Senator 1')
        elif state['Name'] != "Washington DC" and year % 6 == state['Senate Seats'][1]:
            print()
            print("Senate Results (" + state['Name'] + ")")
            results_summary(state, 0, state['Senate Candidates'], s_votes, 'Senator 2')
        if year % 2 == 0 and state['Name'] != "Washington DC":
            print()
            print("House Results (" + state['Name'] + ")")
            string = ''
            string2 = ''
            y = 0
            total = sum(list(c_votes.values()))
            for i in c_seats:
                if y + 1 < len(c_seats):
                    string += Parties[i]['Color'] + str(c_seats[i]) + " Seats " + color.END + "to "
                    string2 += Parties[i]['Color'] + str(round(c_votes[i] / total * 100, 1)) + "% " + color.END + "to "
                    y += 1
                else:
                    string += Parties[i]['Color'] + str(c_seats[i]) + " Seats" + color.END
                    string2 += Parties[i]['Color'] + str(round(c_votes[i] / total * 100, 1)) + "%" + color.END
            print(string)
            print(string2)
        if prescands != 0:
            print()
            print('Presidential Vote (' + state['Name'] + ')')
            winner = max(pres_votes, key=pres_votes.get)
            results['Electoral Votes'][winner] += state['Electoral Votes']
            for i in pres_votes:
                results['Popular Vote'][i] += pres_votes[i]
            total = sum(list(pres_votes.values()))
            string1 = ''
            y = 0
            for i in pres_votes:
                if y + 1 < len(prescands):
                    string1 += Parties[prescands[i]['Party']]['Color'] + prescands[i]['Name'] + color.END + " - "
                    y += 1
                else:
                    string1 += Parties[prescands[i]['Party']]['Color'] + prescands[i]['Name'] + color.END
            string = ''
            y = 0
            for i in pres_votes:
                if y + 1 < len(pres_votes):
                    string += Parties[prescands[i]['Party']]['Color'] + str(round(pres_votes[i] / 1000, 2)) + " million " + color.END + "to "
                    y += 1
                else:
                    string += Parties[prescands[i]['Party']]['Color'] + str(round(pres_votes[i] / 1000, 2)) + " million" + color.END
            y = 0
            string2 = ''
            for i in pres_votes:
                if y + 1 < len(pres_votes):
                    string2 += Parties[prescands[i]['Party']]['Color'] + str(round(pres_votes[i] / total * 100, 1)) + "% " + color.END + "to "
                    y += 1
                else:
                    string2 += Parties[prescands[i]['Party']]['Color'] + str(round(pres_votes[i] / total * 100, 1)) + "%" + color.END
            print(string1)
            print(string)
            print(string2)
        print()
        print("Turnout: " + str(round(b/a * 100, 1)) + "%")
        print("Dem Turnout: " + str(round(dem_in / dem_tot * 100, 1)) + "%")
        print("Rep Turnout: " + str(round(rep_in / rep_tot * 100, 1)) + "%")
        print("Ind Turnout: " + str(round(ind_in / ind_tot * 100, 1)) + "%")
    else:
        print()
        print('No elections in ' + state['Name'])


def retirement(prescands, state, candidate, type, presidency, term_min, term_max, presparty, year):
    candidate['Age'] += 1
    chance = randint(0, 110 ** 12)
    if chance < candidate['Age'] ** 12:
        print(candidate['Name'] + " has died.")
        if type in ['Senator 1', 'Senator 2', 'Governor']:
            state[type] = generate_candidate(candidate['Party'], state, 'RNG')
            if type in ['Senator 1', 'Senator 2']:
                state[type]['Senate Terms'] = 0
            else:
                state[type]['Governor Terms'] = 0
        else:
            state['District Facts'][candidate['District']]['MC'] = generate_candidate(candidate['Party'], state, candidate['District'])
            state['District Facts'][candidate['District']]['MC']['Terms'] = 0
    up = False
    if type in ['Senator 1', 'Senator 2']:
        terms = 'Senate Terms'
        if type == 'Senator 1':
            n = 0
        else: n = 1
        if year % 6 == state['Senate Seats'][n]:
            up = True
    elif type == 'Governor':
        terms = 'Governor Terms'
        if year % 4 in state['Mansion Years']:
            up = True
    else:
        terms = 'Terms'
        if year % 2 == 0:
            up = True
    if up == True:
        if type == 'Governor' and state['Term Limits'] is True and candidate['Governor Terms'] == 2:
            print(candidate['Name'] + " is term-limited and cannot seek re-election.")
            state['Governor'] = generate_candidate(candidate['Party'], state, 'RNG')
        elif randint(term_min, term_max) < candidate[terms]:
            print(candidate['Name'] + " has retired.")
            if type in ['Senator 1', 'Senator 2', 'Governor']:
                state[type] = generate_candidate(candidate['Party'], state, 'RNG')
                if type in ['Senator 1', 'Senator 2']:
                    state[type]['Senate Terms'] = 0
                else:
                    state[type]['Governor Terms'] = 0
            else:
                state['District Facts'][candidate['District']]['MC'] = generate_candidate(candidate['Party'], state, candidate['District'])
                state['District Facts'][candidate['District']]['MC']['Terms'] = 0
    if prescands != 0:
        if candidate['Party'] != 'Independent':
            if candidate['Party'] == presparty:
                presidency *= 30
            chance = randint(0, presidency)
            if chance < candidate['Profile']:
                print(candidate['Name'] + ' is running for president.')
                prescands[candidate['Party']][candidate['Name']] = candidate
                candidate['Nat Name Rec'] += (100 - candidate['Nat Name Rec'] ) * 0.3


def dropouts(number, candidates, delegates):
    lst = []
    for n in candidates:
        if n != 'Independent':
            top = max(delegates[n].values())
            for i in candidates[n]:
                if top - (candidates[n][i]['Profile'] / 5) > delegates[n][i] * 2 - number ** 2 / 10 + 15:
                    print(candidates[n][i]['Name'] + " has dropped out of the primary.")
                    lst.append([n, i])
    for i in lst:
        del candidates[i[0]][i[1]]


def final_prim_summary(cands, votes, delegates):
    general_cands = {}
    general_evs = {}
    general_votes = {}
    for i in cands:
        winner = max(delegates[i], key=delegates[i].get)
        total = sum(list(votes[i].values()))
        leader_percent = round(votes[i][winner] / total * 100, 1)
        print(Parties[i]['Color'] + cands[i][winner]['Name'] + " has won the " + i + " primary with " + str(delegates[i][winner]) + " delegates and " + str(leader_percent) + "% of the vote " + color.END)
        general_cands[winner] = cands[i][winner]
        general_evs[winner] = 0
        general_votes[winner] = 0
        cands[i][winner]['Momentum'] = 0
        if 'Pres Terms' in cands[i][winner].keys():
            cands[i][winner][cands[i][winner]['Party']] += 7
        else:
            cands[i][winner][cands[i][winner]['Party']] += 10
        cands[i][winner]['Nat Name Rec'] += (100 - cands[i][winner]['Nat Name Rec']) * 0.9
    return [general_cands, general_evs, general_votes]


def presidential_approval(president, country):
    approve = 0
    disapprove = 0
    if president['Party'] == 'Democrat':
        opponent = Generic_R
    elif president['Party'] == 'Republican':
        opponent = Generic_D
    else:
        opponent = [Generic_D, Generic_R]
    for i in country['States']:
        population = int(country['States'][i]['Population'] / (10000 * country['States'][i]['CDs']))
        for n in country['States'][i]['Districts']:
            for x in range(0, population):
                c = randint(0, len(country['States'][i]['Districts'][n]) - 1)
                vtr = country['States'][i]['Districts'][n][c]
                if randint(0, 100) < Races[vtr['Race']]['Turnout']:
                    if president['Party'] == 'Independent':
                        v = vote(vtr, {opponent[randint(0,1)]['Name']: opponent, president['Name']: president}, 1, Parties, country['States'][i], n, Modifier)
                    else:
                        v = vote(vtr, {opponent['Name']: opponent, president['Name']: president}, 1, Parties, country['States'][i], n, Modifier)
                    if v == president['Name']:
                        approve += 1
                    else:
                        disapprove += 1
    if approve > disapprove:
        s = "President " + president['Name'] + "'s approval rating: " + color.BOLD + str(round(approve/(approve + disapprove) * 100, 1)) + "%" + color.END + "-" + str(round(disapprove/(approve + disapprove) * 100, 1)) + "%"
    else:
        s = "President " + president['Name'] + "'s approval rating: " + str(round(approve/(approve + disapprove) * 100, 1)) + "%" + "-" + color.BOLD + str(round(disapprove/(approve + disapprove) * 100, 1)) + "%" + color.END
    plusminus = int(approve/(approve + disapprove) * 100 - disapprove/(approve + disapprove) * 100)
    return [s, plusminus]


def indie_bids(current_candidates, country, year):
    for n in country['States']:
        if year % 4 == 0 and country['States'][n]['Name'] != "Washington DC":
            for z in ['Senator 1', 'Senator 2', 'Governor']:
                if country['States'][n][z]['Party'] == 'Independent':
                    chance = randint(0, 500)
                    if chance < country['States'][n][z]['Profile']:
                        print(country['States'][n][z]['Name'] + " has launched an independent bid for president.")
                        current_candidates[0][country['States'][n][z]['Name']] = country['States'][n][z]
                        current_candidates[1][country['States'][n][z]['Name']] = 0
                        current_candidates[2][country['States'][n][z]['Name']] = 0
                        country['States'][n][z] = generate_candidate(country['States'][n]['Governor']['Party'], country['States'][n], 'RNG')
                else:
                    for i in current_candidates[0]:
                        if current_candidates[0][i]['Name'] == country['States'][n][z]['Name']:
                            replacement = generate_candidate(country['States'][n][z]['Party'], country['States'][n], 'RNG')
                            country['States'][n][z] = replacement
                            if z in ['Senator 1', 'Senator 2'] and year % 6 in country['States'][n]['Senate Seats']:
                                for y in country['States'][n]['Senate Candidates']:
                                    if y == current_candidates[0][i]['Name']:
                                        del country['States'][n]['Senate Candidates'][y]
                                        country['States'][n]['Senate Candidates'][replacement['Name']] = replacement
                                        replacement['Senate Terms'] = 0
                            elif year % 4 in country['States'][n]['Mansion Years']:
                                for y in country['States'][n]['Governor Candidates']:
                                    if y == current_candidates[0][i]['Name']:
                                        del country['States'][n]['Governor Candidates'][y]
                                        country['States'][n]['Governor Candidates'][replacement['Name']] = replacement
                                        replacement['Governor Terms'] = 0
        if country['States'][n]['Name'] != "Washington DC":
            senate = False
            governor = False
            for i in country['States'][n]['District Facts']:
                if country['States'][n]['Primary Type'] == 'Regular':
                    if year % 2 == 0:
                        for l in range(0, randint(0, 1)):
                            indie = generate_candidate('Independent', country['States'][n], i)
                            country['States'][n]['District Facts'][i]['House'][indie['Name']] = indie
                MC = country['States'][n]['District Facts'][i]['MC']
                if MC['Party'] == 'Independent':
                    chance = randint(0, 500)
                    r = randint(0, 5)
                    r *= country['States'][n]['CDs'] ** (1/2)
                    t = randint(0, 5)
                    t *= country['States'][n]['CDs'] ** (1/2)
                    if chance < MC['Profile'] and year % 4 == 0:
                        print(MC['Name'] + " has launched an independent bid for president.")
                        summary(MC)
                        current_candidates[0][MC['Name']] = MC
                        current_candidates[1][MC['Name']] = 0
                        current_candidates[2][MC['Name']] = 0
                        country['States'][n]['District Facts'][i]['MC'] = generate_candidate(country['States'][n]['Governor']['Party'], country['States'][n], i)
                        new_MC = country['States'][n]['District Facts'][i]['MC']
                        if MC['Name'] in country['States'][n]['District Facts'][i]['House']:
                            del country['States'][n]['District Facts'][i]['House'][MC['Name']]
                            country['States'][n]['District Facts'][i]['House'][new_MC['Name']] = new_MC
                    elif r < MC['Profile'] and year % 4 in country['States'][n]['Mansion Years'] and country['States'][n]['Primary Type'] == 'Regular':
                        print(MC['Name'] + " has launched an independent bid for " + country['States'][n]['Name'] + " Governor")
                        country['States'][n]['District Facts'][i]['MC'] = generate_candidate(country['States'][n]['Governor']['Party'], country['States'][n], i)
                        new_MC = country['States'][n]['District Facts'][i]['MC']
                        if MC['Name'] in country['States'][n]['District Facts'][i]['House']:
                            del country['States'][n]['District Facts'][i]['House'][MC['Name']]
                            country['States'][n]['District Facts'][i]['House'][new_MC['Name']] = new_MC
                        country['States'][n]['Governor Candidates'][MC['Name']] = MC
                        governor = True
                    elif t < MC['Profile'] and year % 6 in country['States'][n]['Senate Seats'] and country['States'][n]['Primary Type'] == 'Regular':
                        print(MC['Name'] + " has launched an independent bid for " + country['States'][n]['Name'] + " Senate")
                        country['States'][n]['Senate Candidates'][MC['Name']] = MC
                        country['States'][n]['District Facts'][i]['MC'] = generate_candidate(country['States'][n]['Governor']['Party'], country['States'][n], i)
                        new_MC = country['States'][n]['District Facts'][i]['MC']
                        if MC['Name'] in country['States'][n]['District Facts'][i]['House']:
                            del country['States'][n]['District Facts'][i]['House'][MC['Name']]
                            country['States'][n]['District Facts'][i]['House'][new_MC['Name']] = new_MC
                        senate = True
                elif year % 4 == 0:
                    for q in current_candidates[0]:
                        if q == MC['Name']:
                            replacement = generate_candidate(current_candidates[0][q]['Party'], country['States'][n], i)
                            country['States'][n]['District Facts'][i]['MC'] = replacement
                            for r in country['States'][n]['District Facts'][i]['House']:
                                if r == q:
                                    del country['States'][n]['District Facts'][i]['House'][r]
                                    country['States'][n]['District Facts'][i]['House'][replacement['Name']] = replacement
                                    replacement['Terms'] = 0
            if country['States'][n]['Primary Type'] == 'Regular':
                if year % 4 in country['States'][n]['Mansion Years'] and governor is False:
                    for z in range(0, randint(0, 1)):
                        indie = generate_candidate('Independent', country['States'][n], 'RNG')
                        country['States'][n]['Governor Candidates'][indie['Name']] = indie
                if year % 6 in country['States'][n]['Senate Seats'] and senate is False:
                    for z in range(0, randint(0, 1)):
                        indie = generate_candidate('Independent', country['States'][n], 'RNG')
                        country['States'][n]['Senate Candidates'][indie['Name']] = indie
    if year % 4 == 0:
        other_bids = randint(0, 2)
        for i in range(0, other_bids):
            c = generate_candidate('Independent', 'RNG', 'RNG')
            current_candidates[0][c['Name']] = c
            current_candidates[1][c['Name']] = 0
            current_candidates[2][c['Name']] = 0


def summary(candidate):
    if candidate['Terms'] > 0 or candidate['Senate Terms'] > 0 or candidate['Governor Terms'] > 0:
        start = "("
        end = ")"
    else:
        start = ''
        end = ''
    if candidate['Terms'] > 0:
        rid = str(candidate['Terms']) + "-Term Congressman for " + candidate['District']
    else:
        rid = ''
    if candidate['Senate Terms'] > 0 and candidate['Terms'] > 0:
        sen = ", " + str(candidate['Senate Terms']) + "-Term Senator for " + candidate['State']
    elif candidate['Senate Terms'] > 0:
        sen = str(candidate['Senate Terms']) + "-Term Senator for " + candidate['State']
    else:
        sen = ''
    if (candidate['Senate Terms'] > 0 or candidate['Terms'] > 0) and candidate['Governor Terms'] > 0:
        gov = ", " + str(candidate['Governor Terms']) + "-Term Governor for " + candidate['State']
    elif candidate['Governor Terms'] > 0:
        gov = str(candidate['Governor Terms']) + "-Term Governor for " + candidate['State']
    else:
        gov = ''
    lst = {}
    for i in Races:
        lst[i] = candidate[i] + Parties[candidate['Party']][i] * 0.5
    rac = max(lst, key=lst.get)
    rac += 's'
    lst = {}
    for i in Educations:
        lst[i] = candidate[i] + Parties[candidate['Party']][i] * 0.5
    edu = max(lst, key=lst.get)
    if edu == 'Degree':
        edu = ' voters with a college degree.'
    else:
        edu = ' voters without a college degree.'
    lst = {}
    for i in Ideologies:
        lst[i] = candidate[i] + Parties[candidate['Party']][i] * 0.5
    ide = max(lst, key=lst.get)
    ide += 's'
    age = str(candidate['Age'])
    return candidate['Name'] + ", " + age + " [" + Parties[candidate['Party']]['Letter'] + "] is popular with " + rac.lower() + ", " + ide.lower() + ", and" + edu + " " + start + rid + sen + gov + end


def approval_changes(country, natenv, year):
    trend = np.random.normal(0, 1)
    for i in Parties:
        if i == country['President']['Party']:
            country['President'][i] += np.random.normal(trend + 2 - country['President'][i] * 0.7, 2)
        else:
            country['President'][i] += np.random.normal(trend - 1 - country['President'][i] * 0.7, 2)
    for i in Races:
        country['President'][i] += np.random.normal(trend, 2)
    for i in Educations:
        country['President'][i] += np.random.normal(trend, 2)
    for i in Ideologies:
        country['President'][i] += np.random.normal(trend, 2)
    if year % 4 != 0:
        for q in Races:
            if country['President'][q] < 0:
                x = -1
            else:
                x = 1
            natenv[country['President']['Party']][q] += round(abs(country['President'][q]) ** (1/3) * x - randint(1,3), 1)
        for q in Educations:
            if country['President'][q] < 0:
                x = -1
            else:
                x = 1
            natenv[country['President']['Party']][q] += round(abs(country['President'][q]) ** (1/3) * x - randint(1,3), 1)
        for q in Ideologies:
            if country['President'][q] < 0:
                x = -1
            else:
                x = 1
            natenv[country['President']['Party']][q] += round(abs(country['President'][q]) ** (1/3) * x - randint(1,3), 1)
        for q in Parties:
            if country['President'][q] < 0:
                x = -1
            else:
                x = 1
            natenv[country['President']['Party']][q] += round(abs(country['President'][q]) ** (1/2) * x - randint(1,3), 1)
    for i in natenv:
        for q in Races:
            natenv[i][q] += np.random.normal(0, 2)
        for q in Educations:
            natenv[i][q] += np.random.normal(0, 2)
        for q in Ideologies:
            natenv[i][q] += np.random.normal(0, 2)
        for q in Parties:
            natenv[i][q] += np.random.normal(0, 2)
    presapp = presidential_approval(country['President'], country)
    print()
    print(presapp[0])
    return presapp[1]


def run_game(country, year):
    print(color.BOLD + "THE YEAR IS " + str(year) + color.END)
    if year % 10 == 2:
        print("REDISTRICTING YEAR: Districts redrawn by governors and state legislatures")
        pop = 0
        for i in country['States']:
            pop += country['States'][i]['Population']
        total = 0
        point = 0.1
        for i in country['States']:
            if country['States'][i]['CDs'] > 1:
                if country['States'][i]['Redistricting'] == 'Nonpartisan':
                    country['States'][i]['Redistricting'] = 'Nonpartisan'
                else:
                    country['States'][i]['Redistricting'] = country['States'][i]['Governor']['Party']
                redistricting(country['States'][i])
            total += country['States'][i]['Population']
            if total / pop > point:
                print("loading... " + str(int(point * 100)) + "%")
                point += 0.1
    natenv = copy.deepcopy(Parties)
    approval = approval_changes(country, natenv, year)
    p = 'NULL'
    ohouse_seats = {}
    osenate_seats = {}
    ogovernors = {}
    for i in Parties:
        ohouse_seats[i] = 0
        osenate_seats[i] = 0
        ogovernors[i] = 0
    for n in country['States']:
        if country['States'][n]['Name'] != 'Washington DC':
            osenate_seats[country['States'][n]['Senator 1']['Party']] += 1
            osenate_seats[country['States'][n]['Senator 2']['Party']] += 1
            ogovernors[country['States'][n]['Governor']['Party']] += 1
            for i in country['States'][n]['District Facts']:
                ohouse_seats[country['States'][n]['District Facts'][i]['MC']['Party']] += 1
    if year % 4 == 0:
        prescands = {}
        prescands_votes = {}
        prescands_delegates = {}
        momentum = {}
        for i in Parties:
            if i != 'Independent':
                prescands[i] = {}
                prescands_votes[i] = {}
                prescands_delegates[i] = {}
                momentum[i] = {}
        if country['President']['Pres Terms'] < 2:
            p = country['President']['Party']
            if p != 'Independent':
                prescands[p][country['President']['Name']] = country['President']
    else:
        prescands = 0
        prescands_votes = 0
        prescands_delegates = 0
        momentum = 0
    for n in country['States']:
        if country['States'][n]['Name'] != "Washington DC":
            retirement(prescands, country['States'][n], country['States'][n]['Senator 1'], 'Senator 1', 300, 2, 6, p, year)
            retirement(prescands, country['States'][n], country['States'][n]['Senator 2'], 'Senator 2', 300, 2, 6, p, year)
            retirement(prescands, country['States'][n], country['States'][n]['Governor'], 'Governor', 300, 2, 6, p, year)
            for i in country['States'][n]['District Facts']:
                retirement(prescands, country['States'][n], country['States'][n]['District Facts'][i]['MC'], 'MC', 3000, 2, 10, p, year)
    if year % 4 == 0:
        for i in Parties:
            if i != 'Independent' and len(prescands[i].values()) == 0:
                for n in range(0,randint(2,4)):
                    c = generate_candidate(i, 'RNG', 'RNG')
                    prescands[i][c['Name']] = c
            elif i != 'Independent' and i != p:
                for n in range(0,randint(0,3)):
                    c = generate_candidate(i, 'RNG', 'RNG')
                    prescands[i][c['Name']] = c
    if year == 2020:
        prescands['Democrat'] = {'Pete Buttigieg': Pete_Buttigieg, 'Julian Castro': Julian_Castro, 'Cory Booker': Cory_Booker, 'Andrew Yang': Andrew_Yang, 'Elizabeth Warren': Elizabeth_Warren, "Beto O'Rourke": Beto_ORourke, 'Joe Biden': Joe_Biden, 'Bernie Sanders': Bernie_Sanders, 'Amy Klobuchar': Amy_Klobuchar, 'Kamala Harris': Kamala_Harris}
    if year % 4 == 0:
        for i in prescands:
            if i != 'Independent':
                print()
                print(color.BOLD + i + ' Candidates for President' + color.END)
                for n in prescands[i]:
                    prescands_votes[i][n] = 0
                    prescands_delegates[i][n] = 0
                    momentum[i][n] = 0
                    print()
                    print(summary(prescands[i][n]))
    k = 1
    u = 1
    for i in Primary:
        y = 0
        if prescands != 0:
            if k % 3 == 1:
                for z in prescands:
                    if len(prescands[z]) > 1:
                        print()
                        print(Parties[z]['Color'] + z + " Debate" + color.END)
                        debate(prescands[z])
        for n in Primary[i]:
            test = False
            if year % 2 == 0 and country['States'][n]['Name'] != "Washington DC":
                test = True
            if year % 6 in country['States'][n]['Senate Seats'] or year % 4 in country['States'][n]['Mansion Years']:
                test = True
            if prescands != 0:
                test = True
            if test == True:
                if y == 0:
                    print()
                    print(color.BOLD + i + ", " + str(year) + color.END)
                    y = 1
                print()
                input("Would you like to count " + USA['States'][n]['Name'] + "?")
                primary(country['States'][n], year, prescands, natenv, prescands_delegates, prescands_votes, momentum)
                u += 1
        k += 1
        if year % 4 == 0:
            for z in prescands:
                for g in prescands[z]:
                    prescands[z][g]['Momentum'] *= 0.5
                    prescands[z][g]['Momentum'] += momentum[z][g]
                    if prescands[z][g]['Momentum'] > 15:
                        prescands[z][g]['Momentum'] = 15
                    momentum[z][g] = 0
            print()
            dropouts(u, prescands, prescands_delegates)
    x = [0,0,0]
    if year % 4 == 0:
        x = final_prim_summary(prescands, prescands_votes, prescands_delegates)
        if country['President']['Party'] == 'Independent' and country['President']['Pres Terms'] < 2:
            x[0][country['President']['Name']] = country['President']
            x[1][country['President']['Name']] = 0
            x[2][country['President']['Name']] = 0
    indie_bids(x, country, year)
    results = {}
    if year % 2 == 0:
        GCB = {}
        for i in Parties:
            GCB[i] = 0
        results['Generic Congressional Ballot'] = GCB
    if year % 4 == 0:
        results['Electoral Votes'] = x[1]
        results['Popular Vote'] = x[2]
    print()
    print(color.BOLD + 'General Election ' + str(year) + color.END)
    print()
    for n in GE_Order:
        test = False
        if year % 2 == 0 and country['States'][n]['Name'] != "Washington DC":
            test = True
        if year % 6 in country['States'][n]['Senate Seats'] or year % 4 in country['States'][n]['Mansion Years']:
            test = True
        if prescands != 0:
            test = True
        if test == True:
            input("Would you like to count " + USA['States'][n]['Name'] + "?")
            general(country['States'][n], year, x[0], natenv, results)
            print()
    house_seats = {}
    senate_seats = {}
    governors = {}
    for i in Parties:
        house_seats[i] = 0
        senate_seats[i] = 0
        governors[i] = 0
    for n in country['States']:
        if country['States'][n]['Name'] != 'Washington DC':
            senate_seats[country['States'][n]['Senator 1']['Party']] += 1
            senate_seats[country['States'][n]['Senator 2']['Party']] += 1
            governors[country['States'][n]['Governor']['Party']] += 1
            for i in country['States'][n]['District Facts']:
                house_seats[country['States'][n]['District Facts'][i]['MC']['Party']] += 1
    print(color.BOLD + "Final Results" + color.END)
    if year % 4 == 0:
        print()
        print('Presidential Results')
        total = sum(list(results['Popular Vote'].values()))
        string = ''
        string2 = ''
        z = 0
        for i in x[0]:
            if z < len(x[0]) - 1:
                string += Parties[x[0][i]['Party']]['Color'] + str(results['Electoral Votes'][i]) + " EV " + color.END + "to "
                string2 += Parties[x[0][i]['Party']]['Color'] + str(round(results['Popular Vote'][i] / total * 100, 1)) + "% " + color.END + "to "
                z += 1
            else:
                string += Parties[x[0][i]['Party']]['Color'] + str(results['Electoral Votes'][i]) + " EV" + color.END
                string2 += Parties[x[0][i]['Party']]['Color'] + str(round(results['Popular Vote'][i] / total * 100, 1)) + "%" + color.END
        print(string)
        print(string2)
    if year % 2 == 0:
        print()
        print('House Results')
        total = sum(list(results['Generic Congressional Ballot'].values()))
        string = ''
        string2 = ''
        z = 0
        for i in Parties:
            if ohouse_seats[i] > house_seats[i]:
                change = "(-" + str(ohouse_seats[i] - house_seats[i]) + ")"
            else:
                change = "(+" + str(house_seats[i] - ohouse_seats[i]) + ")"
            if z < len(Parties) - 1:
                string += Parties[i]['Color'] + str(house_seats[i]) + " Seats " + change + color.END + " to "
                string2 += Parties[i]['Color'] + str(round(results['Generic Congressional Ballot'][i] / total * 100, 1)) + "% " + color.END + "to "
                z += 1
            else:
                string += Parties[i]['Color'] + str(house_seats[i]) + " Seats " + change + color.END
                string2 += Parties[i]['Color'] + str(round(results['Generic Congressional Ballot'][i] / total * 100, 1)) + "%" + color.END
        print(string)
        print(string2)
    print()
    if year % 2 == 0:
        print('Senate Results')
        string = ''
        z = 0
        for i in Parties:
            if osenate_seats[i] > senate_seats[i]:
                change = "(-" + str(osenate_seats[i] - senate_seats[i]) + ")"
            else:
                change = "(+" + str(senate_seats[i] - osenate_seats[i]) + ")"
            if z < len(Parties) - 1:
                string += Parties[i]['Color'] + str(senate_seats[i]) + " Seats " + change + color.END + " to "
                z += 1
            else:
                string += Parties[i]['Color'] + str(senate_seats[i]) + " Seats " + change + color.END
        print(string)
        print()
    print('Governor Results')
    string = ''
    z = 0
    for i in Parties:
        if ogovernors[i] > governors[i]:
            change = "(-" + str(ogovernors[i] - governors[i]) + ")"
        else:
            change = "(+" + str(governors[i] - ogovernors[i]) + ")"
        if z < len(Parties) - 1:
            string += Parties[i]['Color'] + str(governors[i]) + " States " + change + color.END + " to "
            z += 1
        else:
            string += Parties[i]['Color'] + str(governors[i]) + " States " + change + color.END
    print(string)
    if year % 4 == 0:
        winner = max(results['Electoral Votes'], key=results['Electoral Votes'].get)
        lst = list(results['Electoral Votes'].values())
        print()
        if max(lst) < 270:
            print("Due to no candidate receiving 270 electoral votes, the house has decided the president.")
            party = max(house_seats, key=house_seats.get)
            for i in x[0]:
                if x[0][i]['Party'] == party:
                    winner = i
        if country['President'] == x[0][winner]:
            country['President']['Pres Terms'] += 1
            print(color.BOLD + winner + " is re-elected President of the United States" + color.END)
        else:
            country['President'] = x[0][winner]
            country['President']['Pres Terms'] = 1
            print(color.BOLD + winner + " is elected President of the United States" + color.END)
        country['President'][country['President']['Party']] += 5
    return approval


def debate(cands):
    print()
    for i in cands:
        r = np.random.normal(0,3)
        cands[i]['Momentum'] += r
        for x in Parties:
            cands[i][x] += np.random.normal(r/4, 0.5)
        for x in Races:
            cands[i][x] += np.random.normal(r/4, 0.5)
        for x in Educations:
            cands[i][x] += np.random.normal(r/4, 0.5)
        for x in Ideologies:
            cands[i][x] += np.random.normal(r/4, 0.5)
        if r >= 6:
            print(color.BOLD + cands[i]['Name'] + " had a great performance in the debate" + color.END)
        elif r >= 2:
            print(cands[i]['Name'] + " had a good performance in the debate")
        elif r <= -2:
            print(cands[i]['Name'] + " had a weak performance in the debate")
        elif r <= -4:
            print(cands[i]['Name'] + " had an awful showing in the debate")
        else:
            print(cands[i]['Name'] + " had a decent debate")




prep(USA)
print("DONE PREP")
year = 2019
for n in range(0, 200):
    print()
    pres = run_game(USA, year)
    year += 1

# c = generate_candidate('Independent', West_Virginia, 'WV-03')
# results = {'Generic Congressional Ballot': {'Republican': 0, 'Democrat': 0, 'Independent': 0}, 'Electoral Votes': {'Joe Manchin': 0, 'Donald Trump': 0, c['Name']: 0}, 'Popular Vote': {'Joe Manchin': 0, 'Donald Trump': 0, c['Name']: 0}}
# general(USA['States']['WV'], 2016, {'Joe Manchin': Joe_Manchin, c['Name']: c, 'Donald Trump': Donald_Trump}, Parties, results)
# general(USA['States']['CA'], 2016, {'Joe Manchin': Joe_Manchin, c['Name']: c, 'Donald Trump': Donald_Trump}, Parties, results)

# districts(West_Virginia)
#prep(USA)
# for i in USA['States']:
#      print()
#      long_form(USA['States'][i])
# s = state_election(West_Virginia, [Patrick_Morrisey, Joe_Manchin, generate_candidate('Independent', West_Virginia, 'RNG')], 1, Parties)
# print()
# vote_summary(s[0])
# summarize(s[1])
# long_form(West_Virginia)
# print()
# s = state_election(West_Virginia, [Joe_Manchin, Patrick_Morrisey], 0.75, Parties)
# vote_summary(s[0])
# summarize(s[1])
# # print()
# dist_facts(West_Virginia, 'WV-01')
# for n in range(0,20):
#     print()
#     d1 = district_election([generate_candidate('Democrat', West_Virginia, "WV-01"), generate_candidate('Republican', West_Virginia, "WV-01")], 1, Parties, West_Virginia, 'WV-01')
#     # d2 = district_election([Generic_D, Generic_R], 1, Parties, West_Virginia, 'WV-02')
#     # d3 = district_election([Generic_D, Generic_R], 1, Parties, West_Virginia, 'WV-03')
#     vote_summary(d1[0])
#     # summarize(d1[1])
# vote_summary(d2[0])
# vote_summary(d3[0])
