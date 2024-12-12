import unittest
import tests_12_3

variable = unittest.TestSuite()
variable.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TestRunner))
variable.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(variable)
