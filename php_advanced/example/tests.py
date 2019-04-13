from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SimpleTestCase(TestCase):
    hello_world_url = reverse("hello")

    def test_display_view(self):
        #field_name = 'field_name'
        #data = {field_name: ''
        response = self.client.get(self.hello_world_url)
        content = str(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.view_name, "hello")

class SimpleTestCase2(TestCase):
    form_view_url = reverse("add_gfl")

    def test_display_view(self):
        field_name = 'name'
        data = {field_name: 'oh curse my curse'}
        expected_error = f'You can not use forbidden words'
        response = self.client.post(self.form_view_url, data)
        # import ipdb;
        # ipdb.set_trace()

        self.assertFormError(response,'form',field_name, expected_error)


class SimpleTestCase3(TestCase):

    # def tearUp(self):
    #     # import ipdb;ipdb.set_trace()
    #     form_add_url = reverse("add_gfl")
    #     data = {'name': 'Whoooop'}
    #     res = self.client.post(form_add_url, data)
    #     import ipdb;ipdb.set_trace()



    def test_display_view(self):
        # self.tearUp()
        form_view_url = reverse("add_gfl")
        # import ipdb;ipdb.set_trace()
        field_name = 'name'
        data = {field_name: 'BLABLABLA'}
        expected_redirect = [(reverse("list_gfl"),302)]
        response = self.client.post(form_view_url, data, follow=True)
        # import ipdb;
        # ipdb.set_trace()

        self.assertEqual(response.redirect_chain, expected_redirect)


