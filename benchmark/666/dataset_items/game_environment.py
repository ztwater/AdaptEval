"""Environment that abstracts the operations of a Game.
"""

from enum import Enum
from typing import Dict, List

import gym

class LocalGameState:
    """Represents what the Agent Toolkit thinks is the current state of a game"""

    def __init__(self) -> None:
        self.instructions = ""
        self.conversation_history = []
        # initial states are set when the game begins and shouldn't be changed after that
        self.initial_player_states = {}
        self.player_states = {}
        self.active_role_id = ""
        self.blocks_in_world = {}

# from agent_toolkit.event_aggregator import EventAggregator
# from agent_toolkit.event_aggregator.local_game_state import LocalGameState
# from agent_toolkit.event_callback_provider import EventCallbackProvider

class TurnState(Enum):
    TURN_ABOUT_TO_START = "TURN_ABOUT_TO_START"
    TURN_IN_PROGRESS = "TURN_IN_PROGRESS"
    TURN_JUST_ENDED = "TURN_JUST_ENDED"

class GameEnvironment(gym.Env):
    """
    Environment that abstracts the operations of a Game.

    The GameEnvironment handles interactions between an Agent and the
    AgentToolkit, who will forward received events relative to the game.
    It keeps track of the Game State.
    """

    def __init__(
        self,
        # role_id: str,
        # callback_provider: EventCallbackProvider,
        # initial_game_state: LocalGameState,
        episode_timeout_seconds: int = 10
    ) -> None:
        """Creates a new GameEnvironment

        Args:
            role_id (str): The id that identifies the agent's role. It is used to recognize which
                events are caused by the Agent.
            callback_provider (EventCallbackProvider) object that provides methods to call when
                an operation that may trigger an event has happened.
            initial_game_state (LocalGameState): the game state constructed from the initial data.
            episode_timeout_seconds (int, optional): how many seconds to wait
                until the game (episode) is finished. Defaults to 10.
        """
        # self.callback_provider = callback_provider
        # self.role_id = role_id
        # self.episode_timeout_seconds = episode_timeout_seconds

        # self.episode_start_time_ms: float = 0.0

        # self.event_aggregator = EventAggregator(initial_game_state)

        # self.target_states: List[LocalGameState] = []

        # observation_space is initially set to empty dict. It's up to user of this class to
        # properly set it
        self.game_state = LocalGameState()

        self.observation_space = {}  # type: ignore

        self.is_first_step_in_turn = True

        self._turn_state: TurnState = TurnState.TURN_ABOUT_TO_START

    def to_observation_space(self) -> Dict:
        """
        Returns the current state of the game following the format expected by the model,
        which is defined in `self.observation_space`.

        This method is called at a high frequency at every opportunity to make inference. The
        transformations made from LocalGameState to observation space should be as fast as
        possible.
        """

        # by default, it just returns a dict representation of self.game_state. It's up to the
        # subclasses to overwrite this method if they so desire.

        # Create dictionary of all non-private and non-callable class properties
        # https://stackoverflow.com/a/69088860/2234619
        # TODO this creates a one-level dictionary, where values can still be instances.
        # This which can create aliasing problems by giving references to the local game state.
        # We should implement a solution that recursively converts all objects to
        # dictionaries using this same algorithm.
        
        return dict(
            (key, value) for key, value in self.game_state.__dict__.items()
            if not callable(value)
            and not key.startswith('_')
        )
