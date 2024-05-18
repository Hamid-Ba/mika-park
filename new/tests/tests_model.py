"""
Test Blog Module Models
"""
from django.test import TestCase

from new import models


class NewModelTest(TestCase):
    """New Model Test"""

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        models.New.objects.create(
            title="Testnew",
            slug="test-new",
            short_desc="Short description",
            desc="Long description",
            image_alt="Test Alt",
            image_title="Test Title",
        )

    def test_title_label(self):
        new = models.New.objects.filter(title="Testnew").first()
        field_label = new._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "عنوان")

    def test_slug_max_length(self):
        new = models.New.objects.filter(title="Testnew").first()
        max_length = new._meta.get_field("slug").max_length
        self.assertEquals(max_length, 170)

    def test_object_name_is_title(self):
        new = models.New.objects.filter(title="Testnew").first()
        expected_object_name = f"{new.title}"
        self.assertEquals(expected_object_name, str(new))

    def test_short_desc_blank(self):
        new = models.New.objects.filter(title="Testnew").first()
        short_desc = new._meta.get_field("short_desc").blank
        self.assertTrue(short_desc)

    def test_desc_null(self):
        new = models.New.objects.filter(title="Testnew").first()
        desc = new._meta.get_field("desc").null
        self.assertTrue(desc)

    def test_image_alt_max_length(self):
        new = models.New.objects.filter(title="Testnew").first()
        max_length = new._meta.get_field("image_alt").max_length
        self.assertEquals(max_length, 72)

    def test_publish_date_default(self):
        new = models.New.objects.filter(title="Testnew").first()
        publish_date = new.publish_date
        self.assertIsNotNone(publish_date)

    def test_image_related_name(self):
        new = models.New.objects.filter(title="Testnew").first()
        related_name = new._meta.get_field("image").related_query_name()
        self.assertEquals(related_name, "news")
