import unittest

from runner import Runner


class TestRunner(unittest.TestCase):
    def test_walk(self):
        obj = Runner('Clones')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = Runner('Clones')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj_1 = Runner('Clones1')
        obj_2 = Runner('Clones2')
        for i in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


if __name__ == '__main__':
    unittest.main()
