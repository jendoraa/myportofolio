from django.shortcuts import render
from main.models import Experience, Project

def show_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "project.html", context)

def show_main(request):
    context = {
        "name": "Rajendra Akbar",
        "npm": "2506596874",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik pada pengembangan perangkat keras dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rajendra Akbar",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
