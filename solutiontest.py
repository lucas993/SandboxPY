import unittest

from SandboxPY import solution as s


class MyTestCase(unittest.TestCase):

    def test_happy_path_1(self):
        self.assertEqual(23, s.solution(10), "Values should equal")

    def test_happy_path_2(self):
        self.assertEqual(3, s.solution(5), "Values should equal")

    def test_happy_path_3(self):
        self.assertEqual(98, s.solution(21), "Values should equal")

    def test_happy_path_relative(self):
        self.assertEqual(s.solution_r(10 - 1), s.solution(10), "Values should equal")

    def test_sad_path(self):
        test_var = s.solution(1)
        self.assertEqual(0, test_var)
        self.assertNotEqual(23, test_var, "Not equals wrong number")

    def test_str_path(self):
        test_var = s.solution("string")
        self.assertEqual(0, test_var)
        self.assertNotEqual(23, test_var, "Not equals wrong number")

    def test_raise_exception(self):
        with self.assertRaises(TypeError):
            s.solution_r("str")


if __name__ == '__main__':
    unittest.main()
