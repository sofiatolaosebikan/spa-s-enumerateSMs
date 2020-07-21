#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sofiat
"""

class SPAS:
    def __init__(self):
        self.students = 0       # keeps track of number of students
        self.projects = 0       # keeps track of number of projects
        self.lecturers = 0      # keeps track of number of lecturers
        self.sp = dict()        # {student: [ordered_preference_list, dictionary pointing each project to its rank]}
        self.plc = dict()       # {project: [lecturer, project_capacity]}
        self.lp = dict()        # {lecturer; [lecturer_capacity, ordered_preference_list_Lk, dictionary pointing each project to Lkj]}
        self.lp_rank = dict()   # {lecturer: a dictionary pointing each student to her rank in Lk}
        self.proj_rank = dict() # {project: a dictionary pointing each student to her rank in Lkj}

    def read_file(self, filename):  # reads the SPA instance
        """
        Output below corresponds to input2.txt
        
            self.sp = {'s1': [['p1', 'p2'], {'p1': 0, 'p2': 1}], 's2': [['p2', 'p3'], {'p2': 0, 'p3': 1}], 's3': [['p3', 'p1'], {'p3': 0, 'p1': 1}], 's4': [['p4', 'p1'], {'p4': 0, 'p1': 1}]}
            
            self.plc = {'p1': ['l1', 1], 'p2': ['l1', 1], 'p3': ['l2', 1], 'p4': ['l2', 1]}
            
            self.lp = {'l1': [2, ['s3', 's1', 's2', 's4'], {'p1': ['s3', 's1', 's4'], 'p2': ['s1', 's2']}], 'l2': [2, ['s2', 's4', 's3'], {'p3': ['s2', 's3'], 'p4': ['s4']}]}
            
            self.lp_rank = {'l1': {'s3': 0, 's1': 1, 's2': 2, 's4': 3}, 'l2': {'s2': 0, 's4': 1, 's3': 2}}
            
            self.proj_rank = {'p1': {'s3': 0, 's1': 1, 's4': 2}, 'p2': {'s1': 0, 's2': 1}, 'p3': {'s2': 0, 's3': 1}, 'p4': {'s4': 0}}
        """

        with open(filename) as t:
            t = t.readlines()
        entry1 = t[0].rstrip(' \n').split(' ')
        #entry1 = list(map(int, entry1)) #converts each element to an integer
        self.students, self.projects, self.lecturers = int(entry1[0]), int(entry1[1]), int(entry1[2])

        # -------------------------------------------------------------------------------------------------------------------
        #  we build the student's dictionary

        for i in range(1, self.students+1):
            entry = t[i].rstrip(' \n').split(' ')
            student = 's' + str(entry[0])
            preferencelist = ['p'+str(k) for k in entry[1:]]
            length = len(preferencelist)
            rank = {preferencelist[i]:i for i in range(length)}  # store the index of each project on each student's preference list
            self.sp[student] = [preferencelist, rank]  
        # -------------------------------------------------------------------------------------------------------------------


        # -------------------------------------------------------------------------------------------------------------------
        #  we build the projects's dictionary

        for i in range(self.students+1, self.students+1+self.projects):
            entry = t[i].rstrip(' \n').split(' ')
            # project = [lecturer, project_capacity_yet_to_be_filled, full(project) = False, keep track of students that was rejected from project]
            # length of the preferred students for p_j according to l_k to be appended when we have more information..
            self.plc['p'+str(entry[0])] = ['l'+str(entry[2]), int(entry[1])]
        # -------------------------------------------------------------------------------------------------------------------


        # -------------------------------------------------------------------------------------------------------------------
        #  we build the lecturer's dictionary

        for i in range(self.students+1+self.projects, self.students+1+self.projects+self.lecturers):
            entry = t[i].rstrip(' \n').split(' ')
            lecturer = 'l' + str(entry[0])
            
            lecturerpreferencelist = ['s' + str(k) for k in entry[2:] ]
            length = len(lecturerpreferencelist)
            self.lp_rank[lecturer] = {lecturerpreferencelist[i]:i for i in range(length)} # stores rank of each student in L_k
            
            # -------------------------------------------------------------------------------------------------------------------
            #  another useful dictionary is created here and attached to the lecturer's dictionary - L_k_j
            #  the lecturer's ranked preference list according to each project they offer
            d = {}
            for project in self.plc:
                if self.plc[project][0] == lecturer:
                    d[project] = []
                    for student in lecturerpreferencelist:
                        if project in self.sp[student][0]:
                            d[project].append(student)
                    length = len(d[project])
                    self.proj_rank[project] = {d[project][i]:i for i in range(length)} # stores rank of each student in L_k_j
                    
            length = len(lecturerpreferencelist)
            # lecturer = [lecturer_capacity, lecturerpreferencelist, d]
            self.lp[lecturer] = [int(entry[1]), lecturerpreferencelist, d]
            # -------------------------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------------------------
            
# s = SPAS()
# filename = "input2.txt"
# s.read_file(filename)
# print(s.sp)
# print()
# print(s.plc)
# print()
# print(s.lp)
# print()
# print(s.lp_rank)
# print()
# print(s.proj_rank)

