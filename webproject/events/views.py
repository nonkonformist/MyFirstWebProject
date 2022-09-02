from django.shortcuts import render, redirect
from .models import Events
from .forms import EventsForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def events_home(request):
    events = Events.objects.order_by('date')
    return render(request, 'events/events_home.html', {'events': events})

def create(request):
    error = ''
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_home')
        else:
            error='Ошибка'

    form = EventsForm()
    data = {
        'form': form
    }
    return render(request, 'events/create.html', data)


class EventDetailView(DetailView):
    model = Events
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventUpdateView(UpdateView):
    model = Events
    template_name = 'events/event_update.html'
    form_class = EventsForm

class EventDeleteView(DeleteView):
    model = Events
    success_url = '/events/'
    template_name = 'events/events_delete.html'