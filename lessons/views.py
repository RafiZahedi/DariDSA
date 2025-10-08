from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_list(request):
    # Get all unique categories from the database
    categories = Lesson.objects.values('category').distinct()

    # Selected category from GET param
    selected_category = request.GET.get('category')

    # Lessons filtered by selected category
    lessons_in_category = Lesson.objects.filter(category=selected_category) if selected_category else []

    # Latest 5 lessons
    latest_lessons = Lesson.objects.order_by('-created_at')[:5]

    # Map category code to display name
    category_map = dict(Lesson.CATEGORY_CHOICES)
    roadmap_categories = [
        {'code': cat['category'], 'name': category_map[cat['category']]} 
        for cat in categories
    ]

    # Get the display name for selected category
    selected_category_name = category_map.get(selected_category) if selected_category else None

    return render(request, 'lessons/lesson_list.html', {
        'roadmap_categories': roadmap_categories,
        'lessons_in_category': lessons_in_category,
        'latest_lessons': latest_lessons,
        'selected_category': selected_category,
        'selected_category_name': selected_category_name,
    })


def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})
