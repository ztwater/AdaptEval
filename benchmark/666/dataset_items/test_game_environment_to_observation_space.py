import unittest
from typing import Dict
from game_environment import GameEnvironment
import gym
import inspect
import re

# Test cases
class TestToObservationSpace(unittest.TestCase):
    def setUp(self):
        # Set up the GameState object with some attributes
        self.game_environment = GameEnvironment()

    def test_encapsulate_code_in_function(self):
        # Test the encapsulation of the code within the to_observation_space function
        observation_space = self.game_environment.to_observation_space()
        self.assertIn('instructions', observation_space)
        self.assertEqual(observation_space['instructions'], "")

    def test_change_instance_reference(self):
        # Test that the instance reference has been changed from 'f' to 'self.game_state'
        source = inspect.getsource(self.game_environment.to_observation_space)
        matched_self_game_state = re.search(r'self\.game_state\.__dict__\.items\(\)', source)
        matched_f = re.search(r'f\.__dict__\.items\(\)', source)
        self.assertIsNotNone(matched_self_game_state)
        self.assertIsNone(matched_f)

    def test_add_type_annotations(self):
        # Test that the function parameters and return type have type annotations
        # self.assertTrue('self' in  self.game_environment.to_observation_space.__annotations__)
        self.assertEqual(self.game_environment.to_observation_space.__annotations__['return'], Dict)

    # def test_non_callable_and_non_private_filtering(self):
    #     # Test that the method filters out private and callable attributes
    #     observation_space = self.game_environment.to_observation_space()
    #     self.assertNotIn('_private_var', observation_space)
    #     self.assertNotIn('callable_var', observation_space)

if __name__ == '__main__':
    unittest.main()
