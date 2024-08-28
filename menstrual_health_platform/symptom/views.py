from django.shortcuts import render,redirect

# Create your views here.

from .models import SymptomLog
from .forms import SymptomLogForm  # Create a form for SymptomLog
def symptom_log(request):
    if request.method == 'POST': #create and validate form
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('symptom_log_success')  # Redirect to success view
    else:
        form = SymptomLogForm()
    return render(request, 'health_resources/symptom_log.html', {'form': form})

def symptom_log_success(request):#if its a GET requuest
    return render(request, 'health_resources/symptom_log_success.html')