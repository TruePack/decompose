from django.test import TestCase, Client
from simple.views import primfacs, calc


class PrimfacsTestCase(TestCase):
    def test_simple_is_simple(self):
        """A prime number returns the list containing itself."""
        self.assertEqual(primfacs(0), [0])
        self.assertEqual(primfacs(1), [1])
        self.assertEqual(primfacs(2), [2])
        self.assertEqual(primfacs(1499), [1499])
        self.assertEqual(primfacs(311111), [311111])

    def test_last_element_is_digit(self):
        """Last element in the returned list is not multiple sign."""
        twenty_five = primfacs(25)
        forty_four = primfacs(44)
        sixty_eight = primfacs(68)
        one_hundred_forty_three = primfacs(143)
        nine_hundred_two = primfacs(902)
        self.assertNotEqual(twenty_five[-1], "*")
        self.assertNotEqual(forty_four[-1], "*")
        self.assertNotEqual(sixty_eight[-1], "*")
        self.assertNotEqual(one_hundred_forty_three[-1], "*")
        self.assertNotEqual(nine_hundred_two[-1], "*")

    def test_prime_factors(self):
        """The returned list is equal to prime factorization.

        The multiplication sign is removed from the returned list.

        """
        twenty_five = [x for x in primfacs(25) if x != "*"]
        forty_four = [x for x in primfacs(44) if x != "*"]
        sixty_eight = [x for x in primfacs(68) if x != "*"]
        one_hundred_forty_three = [x for x in primfacs(143) if x != "*"]
        nine_hundred_two = [x for x in primfacs(902) if x != "*"]
        self.assertEqual(twenty_five, [5, 5])
        self.assertEqual(forty_four, [2, 2, 11])
        self.assertEqual(sixty_eight, [2, 2, 17])
        self.assertEqual(one_hundred_forty_three, [11, 13])
        self.assertEqual(nine_hundred_two, [2, 11, 41])


class CalcTestCase(TestCase):
    def setUp(self):
        # Every response need Client()
        self.client = Client()

    def test_server_is_aviable(self):
        """Server answer status code must be 200 (Ok)."""
        http_response = self.client.get("/")
        self.assertEqual(http_response.status_code, 200)

    def test_prime_factors(self):
        """Render context is correct.

        Answer in template must be follow some rules.
        If inputted number already simple -- return only number.
        Else return prime factor in format: 'x*x*x*x = number'

        """
        # Make GET request, with parameter "number".
        # Take context from template, like it in template.
        five = self.client.get("/", {"number": 5}).context
        result_five = five["answer"] + five["message"]
        twenty_five = self.client.get("/", {"number": 25}).context
        result_twenty_five = twenty_five["answer"] + twenty_five["message"]
        forty_four = self.client.get("/", {"number": 44}).context
        result_forty_four = forty_four["answer"] + forty_four["message"]
        # Checking to follow rules.
        self.assertEqual(result_five, "5")
        self.assertEqual(result_twenty_five, "5*5 = 25")
        self.assertEqual(result_forty_four, "2*2*11 = 44")
