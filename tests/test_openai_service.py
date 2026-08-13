from __future__ import annotations

import unittest
from types import SimpleNamespace

import openai_service


class FakeResponses:
    def __init__(self) -> None:
        self.last_request = None

    def create(self, **kwargs):
        self.last_request = kwargs
        return SimpleNamespace(
            output_text="hello from fake API",
            id="resp_test_123",
        )


class FakeClient:
    def __init__(self) -> None:
        self.responses = FakeResponses()


class OpenAIServiceTests(unittest.TestCase):
    def test_uses_responses_api_contract(self) -> None:
        client = FakeClient()

        text, response_id = openai_service.generate_response(
            "Hello",
            model="gpt-5.5",
            client=client,
        )

        self.assertEqual(text, "hello from fake API")
        self.assertEqual(response_id, "resp_test_123")
        self.assertEqual(client.responses.last_request["model"], "gpt-5.5")
        self.assertEqual(client.responses.last_request["input"], "Hello")
        self.assertIn("instructions", client.responses.last_request)
        self.assertNotIn(
            "previous_response_id",
            client.responses.last_request,
        )

    def test_previous_response_id_is_forwarded(self) -> None:
        client = FakeClient()

        openai_service.generate_response(
            "Follow up",
            previous_response_id="resp_previous",
            client=client,
        )

        self.assertEqual(
            client.responses.last_request["previous_response_id"],
            "resp_previous",
        )

    def test_empty_prompt_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            openai_service.generate_response(
                "   ",
                client=FakeClient(),
            )


if __name__ == "__main__":
    unittest.main()
