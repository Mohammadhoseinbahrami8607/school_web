from django.contrib.auth import decorators
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from . import models, forms


# Create your views here.
class Sign_up(generic.CreateView):
    model = models.CustomUser
    template_name = 'accounts/sign_up.html'
    form_class = forms.CoustomuserCrationForm
    success_url = reverse_lazy('login')


@decorators.login_required()
def panel_list_view(request, username):
    user_inf = get_object_or_404(models.CustomUser, username=username)
    return render(request, 'accounts/panel_list_view.html', context={
        'user': user_inf
    })


def exam_panel(request, username):
    user = get_object_or_404(models.CustomUser, username=username)
    all_exam = models.Exam.objects.all().order_by('datetime')
    return render(request, 'accounts/exam_panel.html', context={
        'exam': all_exam
    })


def exam_detail_view(request, username, pk):
    user = get_object_or_404(models.CustomUser, username=username)
    exam = get_object_or_404(models.Exam, pk=pk)
    # soal = exam.soalat.all()
    exam_detail = models.Exam.objects.all()
    # exam_quastionss = models.Soal.objects.all()
    return render(request, 'accounts/exam_list.html', context={
        # 'soal': soal,
        'exams': exam_detail,
        # 'quastions': exam_quastionss
    })


def exam_quastion(requast, username, pk, pk2):
    user = get_object_or_404(models.CustomUser, username=username)
    exam = get_object_or_404(models.Exam, pk=pk)
    quastions = get_object_or_404(models.Soal, pk=pk2)
    exam_quastionss = quastions.objects.all()
    return render(requast, 'accounts/exam.html', context={
        'quastions': exam_quastionss
    })
