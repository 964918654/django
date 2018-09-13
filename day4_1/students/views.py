from django.shortcuts import render,redirect,reverse
from students.models import StudentInfo
# Create your views here.
def index(request):
    return render(request,'index.html')

def students_list(request):
    all_students = StudentInfo.objects.all()
    return render(request,'students_list.html',{
        'all_students' : all_students
    })

def add_student(request):
    if request.method == 'GET':
        return render(request,'add_student.html')
    else:
        a = StudentInfo()
        stuname = request.POST.get('stuname','')
        stuage = request.POST.get('stuage','')
        stugender = request.POST.get('stugender','')
        stuheight = request.POST.get('stuheight','')
        a.name = stuname
        a.height = stuheight
        a.gender = stugender
        a.age = stuage
        a.save()
        return redirect(reverse('students:students_list'))

def student_update(request,student_id):
    a = StudentInfo.objects.filter(id=int(student_id))[0]
    if student_id:
        if request.method == 'GET':
            return render(request,'student_update.html',{
                'student': a
            })
        else:
            stuname = request.POST.get('stuname', '')
            stuage = request.POST.get('stuage', '')
            stugender = request.POST.get('stugender', '')
            stuheight = request.POST.get('stuheight', '')
            a.name = stuname
            a.height = stuheight
            a.gender = stugender
            a.age = stuage
            a.save()
            return redirect(reverse('students:students_list'))

def student_delete(request,student_id):
    a = StudentInfo.objects.filter(id=int(student_id)).delete()
    if student_id:
        return redirect(reverse('students:students_list'),{
            'student_delete': a
        })