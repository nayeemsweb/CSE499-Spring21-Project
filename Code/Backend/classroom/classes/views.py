from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import ClassroomForm, PostForm, ExamForm, StudentSubmissionForm
from django.contrib import messages
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import redirect, render
from classes.models import Classroom, student_classroom, Post, exam, student_submission
from django.contrib.auth.models import User
from accounts.models import Student,Faculty
import datetime

def createCourse(request):
    classform = ClassroomForm()
    
    if request.method == 'POST':
        classform = ClassroomForm(request.POST, request.FILES)
        if classform.is_valid():
            classform = classform.save(commit=False)
            classform.faculty=request.user
                        
            classform.save()
            return redirect ('facultyDashboard')
    else:    
        context = {'classform':classform}
        return render(request,'create_new_course.html',context)

def courseDetail(request,pk):
    course_detail = Classroom.objects.get(class_codes = pk)
    posts = Post.objects.filter(classroom = Classroom.objects.get(class_codes = pk),comment = None).order_by('-id')
    studentList = student_classroom.objects.filter(classroom =Classroom.objects.get(class_codes = pk))
    examList = exam.objects.filter(classroom =Classroom.objects.get(class_codes = pk))
    if request.method == 'POST':
        if 'examForm' in request.POST:
            examForm = ExamForm(request.POST, request.FILES)
            if examForm.is_valid():
                examForm = examForm.save(commit=False)
                examForm.faculty = request.user
                examForm.classroom = Classroom.objects.get(class_codes = pk)
                examForm.save()
                return HttpResponseRedirect(course_detail.get_absolute_url())
        else:            
            postForm = PostForm(request.POST or None)
            if postForm.is_valid():
                post = request.POST.get('post')
                print(post)
                comment_id = request.POST.get('post_id')
                print(comment_id)
                post_qs = None
                if comment_id:
                    post_qs = Post.objects.get(id = comment_id)
                post = Post.objects.create(classroom=Classroom.objects.get(class_codes = pk), userID =request.user, post=post, comment= post_qs )
                print(post)

                post.save()
                return HttpResponseRedirect(course_detail.get_absolute_url())
    else:
        postForm = PostForm()
        examForm = ExamForm()
        context ={'course_detail':course_detail,'posts':posts,'postForm':postForm,'studentList':studentList,'examForm':examForm,'examList':examList}
        return render(request,'course_detail_view.html',context) ### Work still going on here


def courseDelete(request,pk):
    course = get_object_or_404(Classroom, class_codes=pk)
    if course.faculty != request.user:
        raise Http404()
    course.delete()
    return redirect('facultyDashboard')

def courseEdit(request,pk):
    PreviousCourse = Classroom.objects.get(class_codes=pk)
    courseForm= ClassroomForm(instance=PreviousCourse)

    if request.method == 'POST':
        courseForm = ClassroomForm(request.POST, instance=PreviousCourse)
        if courseForm.is_valid():                        
            courseForm.save()
            return redirect ('/')

    
    context = {'courseForm':courseForm}

    return render(request,'course_edit_view.html',context)

def joinclass(request):

    if request.method == 'POST':
        #print(request.POST['class_code'],"===============")
        joining_code=request.POST['class_code']
        course = Classroom.objects.filter(class_code=joining_code).first()
        NewStudent = Student.objects.filter(user=request.user).first()
        if course:
            student_classroom.objects.get_or_create(student=NewStudent, classroom=course)
        return redirect ('homePage')
    else:
        return render(request,'join_class.html')

def examDetails(request,pk):
    exam_detail = exam.objects.get(id=pk)
    submission_form = StudentSubmissionForm()
    all_submissions = student_submission.objects.filter(exam = exam.objects.get(id=pk))


    if request.method == 'POST':
        submission_form = StudentSubmissionForm(request.POST, request.FILES)
        if submission_form.is_valid():
            submission_form = submission_form.save(commit=False)
            submission_form.student = request.user
            submission_form.exam = exam.objects.get(id=pk)
            try:      
                submission_form.save()
                return redirect ('/')
            except IntegrityError as e:
                messages = "You have already submitted your script"
                context = {'messages':messages,'exam_detail':exam_detail,'all_submissions':all_submissions}
                return render (request, 'exam_details.html',context)

    else:
        context = {'exam_detail':exam_detail,'submission_form':submission_form,'all_submissions':all_submissions}
        return render (request, 'exam_details.html',context)

def submissionEdit(request,pk):
    previous_submission = student_submission.objects.get(id = pk)
    newSubmission_form = StudentSubmissionForm(instance = previous_submission)

    if request.method == 'POST':
        newSubmission_form = StudentSubmissionForm(request.POST, instance= previous_submission)
        if newSubmission_form.is_valid():
            newSubmission_form = newSubmission_form.save(commit=False)
            newSubmission_form.student_post_time = datetime.datetime.now()
            newSubmission_form.save()
            return redirect ('/')

    
    context = {'newSubmission_form':newSubmission_form}
    return render(request,'submission_edit.html',context)


def markSubmission(request,pk):
    studentSubmission = student_submission.objects.get(id = pk)
    
    if request.method == 'POST':
        studentSubmission.obtained_marks = request.POST['obtained_marks']
        studentSubmission.save()
        return redirect('/')
    else:
        context = {'studentSubmission':studentSubmission}
        return render(request,'mark_submission.html',context)
