# main/tests.py

from django.test import TestCase
from django.core.urlresolvers import resolve
from main.views import index, market_items
from django.shortcuts import render_to_response
from django.test import RequestFactory
import mock


class MainPageTests(TestCase):

    ###############
    #### Setup ####
    ###############

    @classmethod
    def setUpClass(cls):
        super(MainPageTests, cls).setUpClass()
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}

    ########################
    #### Testing routes ####
    ########################

    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_response_code(self):
        resp = index(self.request)
        self.assertEqual(resp.status_code, 200)

    #####################################
    #### Testing templates and views ####
    #####################################

    def test_returns_exact_html(self):
        resp = index(self.request)
        self.assertEqual(
            resp.content,
            render_to_response(
                "main/index.html",
                {"marketing_items": market_items}
            ).content
        )

    def test_index_handles_logged_in_user(self):
        # Create a session that appears to have a logged in user
        self.request.session = {"user": "1"}

        with mock.patch('main.views.User') as user_mock:
            # Tell the mock what to do when called
            config = {'get_by_id.return_value': mock.Mock()}
            user_mock.configure_mock(**config)

            # Run the test
            resp = index(self.request)

            # Ensure we return the state of the session back to normal so we don't affect other tests
            self.request.session = {}

            # Verify it returns the page for the logged in user
            expected_html = render_to_response('main/user.html', {'user': user_mock.get_by_id(1)})
            self.assertEqual(resp.content, expected_html.content)
