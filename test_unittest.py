import unittest
from unittest.mock import patch
import ex03.generator as ex03
import sys
import ex02.vector as ex02
import ex01.game as ex01
import ex04.eval as ex04


class Test_Python_Module_00(unittest.TestCase):

    @patch('builtins.print')
    def test_ex01(self, mock_print):
        arya = ex01.Stark('Arya')
        self.assertEqual(arya.__dict__, {'first_name': 'Arya', 'is_alive': True,
                         'family_name': 'Stark', 'house_words': 'Winter is Coming'})
        arya.print_house_words()
        mock_print.assert_called_with('Winter is Coming')
        self.assertTrue(arya.is_alive)
        arya.die()
        self.assertFalse(arya.is_alive)
        self.assertEqual(
            arya.__doc__, 'A class representing the Stark family. Or when bad things happen to good people.')

    def test_ex02(self):
        # Column vector of shape n * 1
        v1 = ex02.Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = v1 * 5
        # Expected output:
        # Vector([[0.0], [5.0], [10.0], [15.0]])
        self.assertListEqual(v2.values, [[0.0], [5.0], [10.0], [15.0]])
        # Row vector of shape 1 * n
        v1 = ex02.Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = v1 * 5
        # print(v2.values)
        self.assertListEqual(v2.values, [[0.0, 5.0, 10.0, 15.0]])
        # Expected output
        # Vector([[0.0, 5.0, 10.0, 15.0]])
        v1 = ex02.Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = v1 / 2.0
        # Expected output
        # Vector([[0.0], [0.5], [1.0], [1.5]])
        self.assertListEqual(v2.values, [[0.0], [0.5], [1.0], [1.5]])
        # Expected ouput
        # ZeroDivisionError: division by zero.
        self.assertRaises(ZeroDivisionError, lambda: v1 / 0.0)
        # Expected output:
        # NotImplementedError: Division of a scalar by a Vector is not defined here.
        self.assertRaises(NotImplementedError, lambda: 2.0 / v1)

    def test_ex03(self):
        text = "Le Lorem Ipsum est simplement du faux texte."
        testcases: list[tuple[list[str], str]] = [
            ([text, " ", None], [
             'Le', 'Lorem', 'Ipsum', 'est', 'simplement', 'du', 'faux', 'texte.']),
            ([text, " ", 'ordered'], [
                'Ipsum', 'Le', 'Lorem', 'du', 'est', 'faux', 'simplement', 'texte.']),
            (["Lorem Ipsum Lorem Ipsum", " ", 'unique'], set([
                'Lorem', 'Ipsum'])),
            ([1, ' ', None], ['ERROR'])
        ]
        for inp, out in testcases:
            ret = ex03.generator(inp[0], sep=inp[1], option=inp[2])
            for a, b in zip(ret, out):
                self.assertEqual(a, b)

        lst = ex03.generator(text, sep=' ', option=None)
        lst = [i for i in lst]
        self.assertListEqual(lst, [
            'Le', 'Lorem', 'Ipsum', 'est', 'simplement', 'du', 'faux', 'texte.'])

    def test_ex04(self):
        testcases = [
            ([[1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"]], 32.0),
            ([[0.0, -1.0, 1.0, -12.0, 0.0, 42.42],
             ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]], -1),
        ]
        for inp, out in testcases:
            ret1 = ex04.Evaluator.zip_evaluate(inp[0], inp[1])
            ret2 = ex04.Evaluator.enumerate_evaluate(inp[0], inp[1])
            self.assertEqual(ret1, ret2)
            self.assertEqual(ret1, out)


if __name__ == '__main__':
    unittest.main()
