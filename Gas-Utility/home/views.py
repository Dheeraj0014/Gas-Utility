from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def submit_request(request):
  if request.method == 'POST':
    form = ServiceRequestForm(request.POST)
    if form.is_valid():
      form.save(commit=False)  
      form.instance.customer = request.user.customer 
      form.save()
      return redirect('success') 
  else:
    form = ServiceRequestForm()  
  return render(request, 'submit_request.html', {'form': form})

def track_requests(request):
requests = ServiceRequest.objects.filter(customer=request.user.customer)
return render(request, 'track_requests.html', {'requests': requests})
