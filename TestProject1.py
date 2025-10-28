import random
import unittest
from io import StringIO
from unittest.mock import patch

import guess_my_number

class TestProject1(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_intro(self, mock_stdout):
        guess_my_number.game_intro()
        output = mock_stdout.getvalue()
        self.assertTrue(output, 
                        "Expected output from game_intro(), but got nothing.")

    def test_computer_number(self):
        seeds = {42: 82, 17: 67, 5: 80,
                 139: 1, 140: 99}
        for s in seeds:
            random.seed(s)
            self.assertEqual(guess_my_number.computer_number(), seeds[s])
        
    @patch('builtins.input', return_value='42')
    def test_player_number(self, mock_input):
        result = guess_my_number.player_number()
        self.assertEqual(result, 42)

    @patch('sys.stdout', new_callable=StringIO)
    def test_number_feedback(self, mock_stdout):
        guess_my_number.number_feedback(30, 70)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Too Low')

    @patch('sys.stdout', new_callable=StringIO)
    def test_number_feedback_elif(self, mock_stdout):
        guess_my_number.number_feedback(80, 50 )
        self.assertEqual(mock_stdout.getvalue().strip(), 'Too High')
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_number_feedback_empty(self, mock_stdout):
        guess_my_number.number_feedback(50, 50)
        self.assertEqual(mock_stdout.getvalue().strip(), '')
    
    @patch('guess_my_number.random.choice', return_value='New Number')
    @patch('guess_my_number.random.randint', return_value=42)
    @patch('sys.stdout', new_callable=StringIO)
    def test_new_number_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['New Number'], 55)
        output = mock_stdout.getvalue()
        self.assertIn('New Number', output)
        self.assertEqual(result, 42)

    @patch('guess_my_number.random.choice', return_value='Starts With')
    @patch('guess_my_number.random.randint', return_value=61)
    @patch('sys.stdout', new_callable=StringIO)
    def test_starts_with_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['Starts With'], 61)
        output = mock_stdout.getvalue()
        self.assertIn('Starts With', output)
        self.assertEqual(result, 61)

    @patch('guess_my_number.random.choice', return_value='Sum of Digits')
    @patch('guess_my_number.random.randint', return_value=11)
    @patch('sys.stdout', new_callable=StringIO)
    def test_some_of_digits_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['Sum of Digits'], 11)
        output = mock_stdout.getvalue()
        self.assertIn('Sum of Digits', output)
        self.assertIn('2', output)
        self.assertEqual(result, 11)

    @patch('guess_my_number.random.choice', return_value='I Love Python')
    @patch('guess_my_number.random.randint', return_value=91)
    @patch('sys.stdout', new_callable=StringIO)
    def test_i_love_python_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['I Love Python'], 91)
        output = mock_stdout.getvalue()
        self.assertIn('I Love Python', output)
        self.assertEqual(result, 91)

    @patch('guess_my_number.random.choice', return_value='Divisible by 3')
    @patch('guess_my_number.random.randint', return_value=24)
    @patch('sys.stdout', new_callable=StringIO)
    
    def test_div_by_3_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['Divisible by 3'], 24)
        output = mock_stdout.getvalue()
        self.assertIn('Divisible by 3', output)
        self.assertIn('IS divisible by 3', output)
        self.assertEqual(result, 24)

    @patch('guess_my_number.random.choice', return_value='Divisible by 3')
    @patch('guess_my_number.random.randint', return_value=25)
    @patch('sys.stdout', new_callable=StringIO)
    def test_not_div_by_3_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['Divisible by 3'], 25)
        output = mock_stdout.getvalue()
        self.assertIn('Divisible by 3', output)
        self.assertIn('NOT divisible by 3', output)
        self.assertEqual(result, 25)

    @patch('guess_my_number.random.choice', return_value='Winner!')
    @patch('guess_my_number.random.randint', return_value=53)
    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_card(self, mock_stdout, mock_randint, mock_choice):
        result = guess_my_number.card_feedback(['Winner!'], 53)
        output = mock_stdout.getvalue() #captures output of prgram - make sure you output divisible by three and it matches teh output. 
        self.assertIn('Winner!', output)
        self.assertIn('53', output)
        self.assertEqual(result, 53)
    
if "__main__" == __name__:
    unittest.main(argv=[''], verbosity=2, exit=False)

