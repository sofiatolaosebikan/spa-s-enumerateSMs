#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:34:50 2020

@author: sofiat
"""

from readinput import SPAS

class ESMS:
    def __init__(self, filename):
        self.filename = filename
        r = SPAS()
        r.read_file(self.filename)
        
        self.students = r.students # no of students
        self.projects = r.projects # no of projects
        self.lecturers = r.lecturers # no of lecturers
        
        self.sp = r.sp
        self.plc = r.plc
        self.lp = r.lp
        self.lp_rank = r.lp_rank
        self.proj_rank = r.proj_rank
        
        self.M = {s:'' for s in self.sp}
        self.project_wstcounter = {'p' + str(i): [0, []] for i in range(1, len(self.plc)+1)}
        self.lecturer_wstcounter = {'l' + str(i): [0, []] for i in range(1, len(self.lp)+1)}  
        
        self.blockingpair = False

    
    # ----------------------------------------------------------------------
    #   --------------------- BLOCKING PAIR CRITERIA ----------------------
    # ----------------------------------------------------------------------
    def blockingpair1(self, project, lecturer):
        #  project and lecturer are both under-subscribed
        if self.plc[project][1] > 0 and self.lp[lecturer][0] > 0:
            #print("type 1:, ", project)
            self.blockingpair = True

    def blockingpair2(self, student, project, lecturer):
        #  project is under-subscribed, lecturer is full and l_k prefers s_i to its worst student in M(l_k)
        if self.plc[project][1] > 0 and self.lp[lecturer][0] == 0:
            matched_project = self.M[student]
            # check if the student is already matched to a project offered by l_k
            if matched_project != '':
                lec = self.plc[matched_project][0]
                if lec == lecturer:
                    self.blockingpair = True
            # check if s_i is in a position before the worst student assigned to l_k
            student_rank_Lk = self.lp_rank[lecturer][student]
            if student_rank_Lk < self.lecturer_wstcounter[lecturer][0]:                
                #print("type 2b:, ", student, project)
                self.blockingpair = True

    def blockingpair3(self, student, project, lecturer):
        #  project is full and lecturer prefers s_i to the worst student assigned to M(p_j)
        if self.plc[project][1] == 0:
            student_rank_Lkj = self.proj_rank[project][student]
            if student_rank_Lkj < self.project_wstcounter[project][0]:
            #print("type 3:, ", student, project, self.project_wstcounter[project][0])
                self.blockingpair = True

    # -------------------------------------------------------------------------
    #   ----------------- FIND BLOCKING PAIR ---------- 
    # If one exist, self.blockingpair is set to True and this bit halts -----
    # -------------------------------------------------------------------------

    def check_stability(self):
        for student in self.M:
            if self.M[student] == '':  # if student s_i is not assigned in M, we check if it forms a blocking pair with all the projects in A(s_i).
                p = self.sp[student][0]  # list of pj's wrt to s_i
            else:
                matched_project = self.M[student]  # get the matched project                
                rank_matched_project = self.sp[student][1][matched_project]  # find its rank on s_i's preference list A(s_i)
                p_list = self.sp[student][0]  # list of pj's wrt to s_i      # a copy of A(s_i)
                p = p_list[:rank_matched_project]  # we check all the projects that comes before the assigned project in A(s_i)
                
            for project in p:
                lecturer = self.plc[project][0]  # l_k

                self.blockingpair1(project, lecturer)  
                if self.blockingpair:
                    break

                self.blockingpair2(student, project, lecturer) 
                if self.blockingpair:
                    break

                self.blockingpair3(student, project, lecturer)
                if self.blockingpair:
                    break
            
            if self.blockingpair:
                break
                    
    # ------------------------------------------------------------------------
    # The choose function finds all the matchings in the given instance
    # The check_stability function is used to print only the stable matchings
    # ------------------------------------------------------------------------
    def choose(self, i):
                   
        if i > self.students:

            """
            the next two for loops updates the rank of the worst student
            assigned to each project and lecturer... this is essential just
            before we initialise the check_stability function to verify if there
            are any blocking pairs in the current matching
            """
            for project in self.plc:
                if self.project_wstcounter[project][1] != []:
                    self.project_wstcounter[project][0] = max(self.project_wstcounter[project][1])
            for lecturer in self.lp:
                if self.lecturer_wstcounter[lecturer][1] != []:
                    self.lecturer_wstcounter[lecturer][0] = max(self.lecturer_wstcounter[lecturer][1])
                    
            self.check_stability()
            if self.blockingpair:
                self.blockingpair = False
            else:
                print('-'*50)
                print(self.M)
            
            
        else:
            student = "s"+str(i)
            for project in self.sp[student][0]:
                lecturer = self.plc[project][0]
                if self.plc[project][1] > 0 and self.lp[lecturer][0] > 0:
                    self.M[student] = project
                    # decrement the capacity of project and lecturer
                    self.plc[project][1] -= 1
                    self.lp[lecturer][0] -= 1
                    
                    # keep track of the rank of the student assigned to the current project and lecturer
                    student_rank_Lk = self.lp_rank[lecturer][student]
                    student_rank_Lkj = self.proj_rank[project][student]
                    self.project_wstcounter[project][1].append(student_rank_Lkj)
                    self.lecturer_wstcounter[lecturer][1].append(student_rank_Lk)
                    
                    
                    self.choose(i+1)
                    
                    self.M[student] = ''
                    student_rank_Lk = self.lp_rank[lecturer][student]
                    student_rank_Lkj = self.proj_rank[project][student]
                    
                    #remove the student's rank from the current assignees of the project and lecturer
                    self.project_wstcounter[project][1].remove(student_rank_Lkj)
                    self.lecturer_wstcounter[lecturer][1].remove(student_rank_Lk)

                    self.plc[project][1] += 1
                    self.lp[lecturer][0] += 1
                    
            self.choose(i+1)
                