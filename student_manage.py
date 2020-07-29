import file_manager
import model

teacher_name=''

def add_student():
    while True:
      x=file_manager.read_json(teacher_name+'.json',{})
      if not x:
          students=[]
          num=0
      else:
          students=x['all_student']
          num = int(x['num'])
      s_name=input('请输入学生姓名：')
      s_age=input('请输入年龄：')
      s_sex=input('请输入性别：')
      s_tel=input('请输入联系电话：')

      num += 1
      # 字符串的zfill方法，在字符串的前面补0.
      s_id = 'stu_' + str(num).zfill(4)

      s=model.Student(s_id,s_name,s_age,s_sex,s_tel)

      students.append(s.__dict__)
      data={'all_student':students,'num':len(students)}
      file_manager.write_json(teacher_name+'.json',data)
      choice=input('添加成功！\n1.继续\n2.返回\n请选择（1-2）：')
      if choice == '2':
          break

def show_student():
    key=value=''
    operate=input('1.查看所有学生。\n2.根据姓名查找。\n3.根据学号查找。\n其他：返回。\n请选择：')
    y=file_manager.read_json(teacher_name+'.json',{})
    students=y.get('all_student',[])

    if not students:
        print('该老师没有学生，请先添加学生。')
        return

    if operate=='1':
        pass

    elif operate=='2':
        value = input('请输入学生姓名：')
        key='name'
        #for student in students:
            #if student['name']==s_name:
                #same_name_student.append(student)

        # filter结果是一个filter类，它是一个可迭代对象

    elif operate=='3':
        value = input('请输入学生学号：')
        key='s_id'

    else:
        return

    students = filter(lambda s: s.get(key,'') == value, students)
    if not students:
        print('未找到学生。')
        return

    for student in students:
        print('学号：{s_id},姓名：{name},性别：{sex},年龄：{age},电话：{tel}'.format(**student))

def modify_student():
    pass

def delete_student():
    y = file_manager.read_json(teacher_name + '.json', {})
    all_students = y.get('all_student', [])
    key=value=''

    operate=input('1.按姓名删\n2.按学号删\n其他：返回')
    if operate == '1':
        key='name'
        value=input('请输入要删除学生的姓名：')
    elif operate == '2':
        key='s_id'
        value=input('请输入要删除学生的id：')
    else:
        return

    students=list(filter(lambda s:s.get(key,'')==value,all_students))
    if not students:
        print('该老师没有学生，请先添加学生。')
        return
    for i,s in enumerate(students):
        print('{x} 学号：{s_id}，姓名：{name}，性别：{sex}，年龄：{age}，电话：{tel}'.format(x=i,**s))
    n=input('请输入要删除学生的标号(0~{}),q-返回。'.format(i))

    if not n.isdigit() or not 0<=int(n)<=i:
        print('输入的内容不合法')
        return

    all_students.remove(students[int(n)])
    y['all_student']=all_students
    file_manager.write_json(teacher_name+'.json',y)

def show_manager():
    content=file_manager.readfile('students_page.txt') % teacher_name
    while True:
        print(content)
        operate=input('请选择（1-5）：')
        if operate == '1':
            add_student()
        elif operate == '2':
            show_student()
        elif operate == '3':
            modify_student()
        elif operate == '4':
            delete_student()
        elif operate == '5':
            break
        else:
            print('输入有误。')
