# spa-s-enumerateSMs
An implementation that finds all the stable matchings in a given instance of the Student-Project Allocation problem with student preferences over projects and lecturer preferences over students (SPA-S).

Input :> a SPA-S instance represented as a .txt file 
Outut :> all stable matchings that the instance admits 

An example of a SPA-S instance is represented in input2.txt, which admits two stable matchings.

# How to read the txt file
Suppose number of students = n1, number of projects = n2 and number of lecturers = n3. The txt file can be read as follows:
n1 n2 n3
student1 <project preferences seperated by space>
student2 <project preferences seperated by space>
.		.
.		.
.		.
studentn1 <project preferences seperated by space>
project1
project2
.
.
.
projectn2
lecturer1
lecturer2
.
.
.
lecturern3

