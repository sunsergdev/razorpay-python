import json

import responses

from .helpers import ClientTestCase, mock_file


class TestClientIin(ClientTestCase):

    def setUp(self):
        super(TestClientIin, self).setUp()
        self.base_url = f'{self.base_url}/iins'
        self.token_iin = '412345'

    @responses.activate
    def test_addon_fetch(self):
        result = mock_file('fake_iin')
        url = f'{self.base_url}/{self.token_iin}'
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.iin.fetch(self.token_iin), result)

    @responses.activate
    def test_addon_fetch(self):
        result = mock_file('iin_collection')
        query = 'sub_type=otp'
        url = f"{self.base_url}/list?{query}"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.iin.all({"sub_type":"otp"}), result)
