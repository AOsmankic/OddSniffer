import unittest
import src.pattern_searcher as pattern_searcher


class TestPatterns(unittest.TestCase):
    def test_true_secret(self):
        secret = "ghs_000000000000000000000000000000000000"
        result = pattern_searcher.does_string_match_any_pattern(secret)
        self.assertIsNotNone(result)
