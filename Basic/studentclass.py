class student:
    student_name="abc"
    student_id=123
    sub1=90
    sub2=95
    sub3=98
    def total():
        return (student.sub1+student.sub2+student.sub3)/3
print(student.total())