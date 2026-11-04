import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            position="part-time",
            started_at=datetime.datetime(2025, 8, 1),
        )

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.position, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, "Experience")
        self.assertContains(response, "experience-container")
        self.assertContains(response, "Test Toast Notifikasi")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada experience yang ditambahkan atau ditemukan.")

    def test_present_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Present")


class ProjectPageTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="iMABA",
            description="Membuat web untuk mahasiswa baru untuk mengenal budaya pacil",
            tech_stack="Next.js"
        )

    def test_project_model(self):
        self.assertEqual(str(self.project), "iMABA")
        self.assertEqual(self.project.tech_stack, "Next.js")

    def test_project_page(self):
        response = self.client.get("/projects/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Projects")
        self.assertContains(response, "project-search-form")

    def test_not_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditambahkan atau ditemukan.")