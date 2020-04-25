import unittest
from main_calculator import Counter


class CalcTest(unittest.TestCase):

    def test_formula1_1(self):
        self.assertEqual(Counter(-10).answer(1), 26409.31)

    def test_formula1_2(self):
        with self.assertRaises(ValueError) as context:
            Counter(0).answer(1)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula1_3(self):
        self.assertEqual(Counter(500).answer(1), 187001580839.5)

    def test_formula1_4(self):
        with self.assertRaises(ValueError) as context:
            Counter(100).answer(1)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula1_5(self):
        self.assertEqual(Counter(-5.645).answer(1), 2348.8621734280405)

    def test_formula1_6(self):
        with self.assertRaises(ValueError) as context:
            Counter(-5.640).answer(1)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula1_7(self):
        self.assertEqual(Counter(409.254).answer(1), 83971172358.0089)

    def test_formula1_8(self):
        with self.assertRaises(ValueError) as context:
            Counter(409.253).answer(1)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula2_1(self):
        self.assertEqual(Counter(-172).answer(2), -21676942.592)

    def test_formula2_2(self):
        with self.assertRaises(ValueError) as context:
            Counter(2).answer(2)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula2_3(self):
        self.assertEqual(Counter(842).answer(2), 2532943697.8240004)

    def test_formula2_4(self):
        with self.assertRaises(ValueError) as context:
            Counter(164).answer(2)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula2_5(self):
        self.assertEqual(Counter(-5.645).answer(2),  -856.8464333367499)

    def test_formula2_6(self):
        with self.assertRaises(ValueError) as context:
            Counter(5.640).answer(2)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula2_7(self):
        self.assertEqual(Counter(409.254).answer(2),  290644000.5073057)

    def test_formula2_8(self):
        with self.assertRaises(ValueError) as context:
            Counter(409.253).answer(2)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula3_1(self):
        self.assertEqual(Counter(-729).answer(3), 1214173.557)

    def test_formula3_2(self):
        with self.assertRaises(ValueError) as context:
            Counter(18).answer(3)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula3_3(self):
        self.assertEqual(Counter(450).answer(3), 465469.65)

    def test_formula3_4(self):
        with self.assertRaises(ValueError) as context:
            Counter(340).answer(3)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula3_5(self):
        self.assertEqual(Counter(-5.645).answer(3),  51.08753224999999)

    def test_formula3_6(self):
        with self.assertRaises(ValueError) as context:
            Counter(5.640).answer(3)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula3_7(self):
        self.assertEqual(Counter(409.254).answer(3),  385136.11337964)

    def test_formula3_8(self):
        with self.assertRaises(ValueError) as context:
            Counter(409.253).answer(3)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula4_1(self):
        self.assertEqual(Counter(-278).answer(4), -687.4939999999999)

    def test_formula4_2(self):
        with self.assertRaises(ValueError) as context:
            Counter(127).answer(4)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula4_3(self):
        self.assertEqual(Counter(666).answer(4), 1647.0179999999998)

    def test_formula4_4(self):
        with self.assertRaises(ValueError) as context:
            Counter(233).answer(4)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula4_5(self):
        self.assertEqual(Counter(-5.645).answer(4),  -13.960084999999998)

    def test_formula4_6(self):
        with self.assertRaises(ValueError) as context:
            Counter(5.640).answer(4)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula4_7(self):
        self.assertEqual(Counter(409.254).answer(4),  1012.085142)

    def test_formula4_8(self):
        with self.assertRaises(ValueError) as context:
            Counter(409.253).answer(4)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))

    def test_formula_entering_true(self):
        self.assertEqual(Counter(-10).answer(1), 26409.31)

    def test_formula_entering_false(self):
        with self.assertRaises(ValueError) as context:
            Counter(409.253).answer(0)
        self.assertTrue('Number you entered is not in range. Please reenter number.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
