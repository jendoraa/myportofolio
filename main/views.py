from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

def create_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main:show_experience')

    else:
        form = ExperienceForm()

    return render(request, 'create_experience.html', {
        'form': form
    })

def update_experience(request, id):
    experience = get_object_or_404(Experience, id=id)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)

        if form.is_valid():
            form.save()
            return redirect('main:show_experience')

    else:
        form = ExperienceForm(instance=experience)

    return render(request, 'update_experience.html', {
        'form': form,
        'experience': experience
    })

def delete_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    experience.delete()
    messages.success(request, "Experience berhasil dihapus!")
    return redirect("main:show_experience")

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(
        experiences_json,
        content_type="application/json"
    )

def experience(request):
    experiences = Experience.objects.all()

    experiences_json = serializers.serialize(
        "json",
        experiences
    )

    experience_list = list(
        serializers.deserialize(
            "json",
            experiences_json
        )
    )

    return render(
        request,
        "experience.html",
        {
            "experience_list": experience_list
        }
    )

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Rajendra",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rajendra Akbar",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

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
