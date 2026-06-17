students ={"aditya":"tamilnadu", "analisha":"mumbai"}
for student in students:
    print(student, students[student], sep =", ")

def main():
    print_sq(3)    
def print_sq(size):
    for i in range(size):
        print_row(size)
def print_row(width):        
    print("#" * width)

main()    

students = ["Adi", "Riya", "Sam"]
for i in range(len(students)):
    print(students[i], i)