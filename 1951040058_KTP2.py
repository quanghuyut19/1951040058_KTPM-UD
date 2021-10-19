def sort(x: STUDENT):
    return x._score

def test_KTP2():
    n = input("Nhap so sinh vien: ")
    list_graduate = []
    list_student = []
    for i in range(int(n)):
        s = STUDENT()
        list_student.append(s)
        if s.graduate():
            list_graduate.append(s)
    list_student.sort(key=sort, reverse=True)
    print(f'MSSV co diem cao nhat: {list_student[0]._id}')
    for student in list_student:
        print(f'{student._id}: {student._score}, credit: {student._credit}, graduate: {student.graduate()}')

