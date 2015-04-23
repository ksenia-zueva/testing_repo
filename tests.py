import unittest
from pydna import seq_utils

class TestSeqUtils(unittest.TestCase):
    def test_is_codon_correct(self):
        codon = 'aTG'
        result = seq_utils.is_codon_correct(codon)
        expected = True
        self.assertEqual(expected, result)
        
    def test_is_codon_correct_bad_codon(self):
        codon = 'aT4'
        result = seq_utils.is_codon_correct(codon)
        expected = False
        self.assertEqual(expected, result)
    