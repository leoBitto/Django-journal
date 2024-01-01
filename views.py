from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiaryEntryForm
from .models import Entry
from django.db.models import Avg


def diary_entry_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:diary_entry_create')
    else:
        form = DiaryEntryForm()
    return render(request, 'journal/diary_entry_form.html', {'form': form})


def diary_entry_detail(request, date_entry):
    entry = get_object_or_404(Entry, date_entry=date_entry)
    return render(request, 'journal/diary_entry_detail.html', {'entry': entry})


def mood_statistics(request, start_date, end_date):
    mood_stats = (
        Entry.objects
        .filter(date_entry__range=[start_date, end_date])
        .values('date_entry')
        .annotate(average_mood=Avg('mood'))
    )
    return render(request, 'journal/mood_statistics.html', {'mood_stats': mood_stats})