import json

import responses

from .helpers import ClientTestCase, mock_file


class TestClientAddon(ClientTestCase):

    def setUp(self):
        super(TestClientAddon, self).setUp()
        self.base_url = f'{self.base_url}/addons'
        self.addon_id = 'ao_8sg8LU73Y3ieav'

    @responses.activate
    def test_addon_fetch(self):
        result = mock_file('fake_addon')
        url = f'{self.base_url}/{self.addon_id}'
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.addon.fetch(self.addon_id), result)

    @responses.activate
    def test_addon_delete(self):
        result = []
        url = f'{self.base_url}/{self.addon_id}'
        responses.add(responses.DELETE,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.addon.delete(self.addon_id), result)

    
    @responses.activate
    def test_addon_fetch_all(self):
        result = mock_file('addon_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.addon.all(), result)       
