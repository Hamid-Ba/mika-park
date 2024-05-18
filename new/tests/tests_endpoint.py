from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, timedelta

from new import models


class NewTestCase(APITestCase):
    def setUp(self):
        self.new1 = models.New.objects.create(
            title="New 1",
            slug="new-1",
            publish_date=datetime.now() - timedelta(days=2),
        )
        self.new2 = models.New.objects.create(
            title="New 2",
            slug="new-2",
            publish_date=datetime.now() - timedelta(days=1),
        )

    def test_new_detail_view(self):
        url = reverse("new:new_detail", args=[self.new1.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["slug"], self.new1.slug)

    def test_news_view(self):
        url = reverse("new:news-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["title"], self.new2.title)

    def test_latest_news_view(self):
        url = reverse("new:latest-news-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], self.new2.title)
