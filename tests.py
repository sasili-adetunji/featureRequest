from datetime import datetime, timedelta
import unittest
from app import create_app, db
from flask import abort, url_for
from flask_testing import TestCase

from app.models import Feature, Client, ClientType, User, ProductAreaType
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestBase(TestCase):

    def create_app(self):
        app = create_app(TestConfig)
        return app


    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()

        # create test user
        user = User(username="testuser", password="user2016")

        # save user to database
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

  
class TestModelsCase(TestBase):

    def test_user_model(self):
        """
        Test number of records in User table
        """

        user1 = User(email="test@example.com",
                    username="tester",
                    first_name="testname",
                    last_name="testlast",
                    password="testpassword1")

        db.session.add(user1)
        db.session.commit()
                        
        self.assertEqual(User.query.count(), 2)

    def test_client_model(self):
        """
        Test number of records in Client table
        """

        # create test client
        client = Client(client=ClientType.CLIENT_B,
                        client_priority=2,
                )
        db.session.add(client)
        db.session.commit()

        self.assertEqual(Client.query.count(), 1)

  
    def test_feature_model(self):
        """
        Test number of records in Feature table
        """

        # create test feature
        client = Client(client=ClientType.CLIENT_B,
                        client_priority=2,
                )
        db.session.add(client)
        db.session.commit()
      
        feature = Feature(title="test title",
                          description="test description",
                          product_area=ProductAreaType.CLAIMS,
                          target_date=datetime.now(),
                          client=client,

                  )
        db.session.add(feature)
        db.session.commit()

        self.assertEqual(Feature.query.count(), 1)

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_features_view(self):
        """
        Test that features page is inaccessible without login
        and redirects to login page then to features page
        """
        target_url = url_for('admin.list_features')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


if __name__ == '__main__':
    unittest.main()
