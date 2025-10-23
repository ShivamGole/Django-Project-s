from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Doctor

def home(request):
    """
    View for the home page.
    Displays a welcome message and a search form for finding doctors.
    """
    return render(request, 'doctors/home.html')

def doctors_list(request):
    """
    View for displaying the list of doctors.
    Supports searching by specialization and location.
    """
    query = request.GET.get('q', '')  # Get search query from URL parameters
    doctors = Doctor.objects.all()  # Start with all doctors

    if query:
        # Filter doctors based on search query (case-insensitive search in name, specialization, or location)
        doctors = doctors.filter(
            Q(name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(location__icontains=query)
        )

    context = {
        'doctors': doctors,
        'query': query,
    }
    return render(request, 'doctors/doctors_list.html', context)

def doctor_detail(request, doctor_id):
    """
    View for displaying detailed information about a specific doctor.
    """
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Get doctor or return 404 if not found
    context = {
        'doctor': doctor,
    }
    return render(request, 'doctors/doctor_detail.html', context)

def about(request):
    """
    View for the about page.
    Provides information about the Health Hub website.
    """
    return render(request, 'doctors/about.html')
