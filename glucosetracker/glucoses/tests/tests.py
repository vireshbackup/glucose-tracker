from django.test import TestCase
from django.contrib.auth.models import User

from . import factories
from ..models import Glucose, Category


class UserTest(TestCase):

    def test_make_objects(self):
        for _ in range(5):
            user = factories.UserFactory()
            self.assertTrue(isinstance(user, User))


class CategoryTest(TestCase):

    def test_make_objects(self):
        for _ in range(5):
            category = factories.CategoryFactory()
            self.assertTrue(isinstance(category, Category))


class GlucoseTest(TestCase):

    def test_make_objects(self):
        for _ in range(5):
            glucose = factories.GlucoseFactory()
            self.assertTrue(isinstance(glucose, Glucose))