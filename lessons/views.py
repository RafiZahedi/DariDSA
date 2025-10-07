from django.shortcuts import render, get_object_or_404
from .models import Lesson
from django.core.paginator import Paginator



def lesson_list(request):
    lessons = Lesson.objects.all()
    # the number shows how many lessons per page
    paginator = Paginator(lessons, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lessons/lesson_list.html', {'page_obj': page_obj})


def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})