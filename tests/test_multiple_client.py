# Standard library imports
import json
import unittest

# Other third-party library imports
import responses

# Razorpay SDK local imports
from .helpers import ClientTestCase, mock_file


class TestClientPayment(ClientTestCase):

    def setUp(self):
        super(TestClientPayment, self).setUp()
        self.base_url = f"{self.base_url}/payments"
        self.secondary_base_url = f"{self.secondary_url}/v1/payments"

    @responses.activate
    def test_payment_primary_url(self):
        result = mock_file("payment_collection")
        url = self.base_url
        responses.add(
            responses.GET,
            url,
            status=200,
            body=json.dumps(result),
            match_querystring=True,
        )
        self.assertEqual(self.client.payment.all(), result)

    @responses.activate
    def test_payment_secondary_url(self):
        result = mock_file("payment_collection")
        url = self.secondary_base_url
        print("abseurl", url)
        responses.add(
            responses.GET,
            url,
            status=200,
            body=json.dumps(result),
            match_querystring=True,
        )
        self.assertEqual(self.secondary_client.payment.all(), result)

    @responses.activate
    def test_payment_with_headers(self):
        result = mock_file("payment_collection")
        url = self.base_url
        responses.add(
            responses.GET,
            url,
            status=200,
            body=json.dumps(result),
            match_querystring=True,
        )
        self.assertEqual(
            self.client.payment.all(headers={"Content-type": "text"}), result
        )
