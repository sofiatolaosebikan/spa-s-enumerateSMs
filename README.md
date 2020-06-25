# spa-s-enumerateSMs
An implementation (brute-force) that finds all the stable matchings in a given instance of the Student-Project Allocation problem with student preferences over projects and lecturer preferences over students (SPA-S).

Input => a SPA-S instance represented as a .txt file

Outut => all stable matchings that the instance admits 

An example of a SPA-S instance is represented in input2.txt, which admits two stable matchings.

# How to read the txt file
Let n1 =  number of students, n2 = number of projects, and n3 = number of lecturers. The .txt file can be read as follows:

n1 n2 n3

student1 preferences_over_projects
  
student2 preferences_over_projects
  
.		      .

.		      .

.		      .

studentn1 preferences_over_projects
  
project1 capacity lecturer

project2 capacity lecturer

.           .         .

.           .         .

.           .         .

projectn2 capacity lecturer

lecturer1 capacity preferences_over_students
  
lecturer2 capacity preferences_over_students
  
.             .           .

.             .           .

.             .           .

lecturern3 capacity preferences_over_students
  


# An illustration
To read input2.txt, the first line of the file tells us there are 4 students, 4 projects and 2 lecturers

student1 prefers project1 to project2

student2 prefers project2 to project3

student3 prefers project3 to project1

student4 prefers project4 to project1

project1 has capacity 1 and is offered by lecturer1

project2 has capacity 1 and is offered by lecturer1

project3 has capacity 1 and is offered by lecturer2

project4 has capacity 1 and is offered by lecturer2

lecturer1 has capacity 2 and prefers student3 to student1 to student2 to student4

lecturer2 has capacity 2 and prefers student2 to student4 to student3

