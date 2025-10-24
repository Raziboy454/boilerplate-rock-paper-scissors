# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import defaultdict


def player(prev_play,
           history_and_state=[{
               'history': [],
               'N': 5,
               'patterns': defaultdict(lambda: defaultdict(int))
           }]):
    # Unpack state for easy access
    state = history_and_state[0]
    opponent_history = state['history']
    patterns = state['patterns']
    N = state['N']

    #  CRITICAL STATE MANAGEMENT (Reset for new opponent) 
    # The initial call to a new opponent has prev_play = "" and history is NOT empty from the previous opponent.
    if not prev_play and len(opponent_history) > 0:
        opponent_history.clear()
        # Reset the pattern dictionary for the new opponent
        state['patterns'] = defaultdict(lambda: defaultdict(int))
        patterns = state['patterns']

    # . Record Previous Play and Update Pattern Counts
    # Record the opponent's *last* move before it is added to history
    if prev_play:
        # Check if we have enough history to form an N-length sequence
        if len(opponent_history) >= N:
            # The sequence that *precedes* the current prev_play is the last N moves
            sequence = "".join(opponent_history[-N:])

            # The 'prev_play' is the move that *followed* that sequence
            # We record the move that was made *after* the sequence
            patterns[sequence][prev_play] += 1

        # Now append the new move
        opponent_history.append(prev_play)

    # Initial Moves: Play randomly (or a constant) for warm-up 
    # We need a few moves to build up the history before we can predict
    if len(opponent_history) < N + 1:
        # Play a constant or random move during the warm-up phase
        return random.choice(
            ["R", "P", "S"])  # Constant "R" is also a fine warm-up strategy

    # Prediction Logic (N-Order Markov Chain) 

    # The sequence we use for prediction is the *last N moves* in the history.
    # We are trying to predict the move that follows this sequence.
    current_sequence = "".join(opponent_history[-N:])

    # Find the observed follow-up moves for this sequence
    possible_next_moves = patterns.get(current_sequence)

    prediction = random.choice(["R", "P", "S"])  # Default to random

    if possible_next_moves:
        # Find the most frequent move that historically followed this sequence
        prediction = max(possible_next_moves, key=possible_next_moves.get)

    # If the current sequence is entirely new, we might still have useful information
    # from shorter sequences (e.g., N-1). Let's stick with the most reliable pattern
    # prediction above, which defaults to random if the N-length pattern is new.

    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    return counter_moves[prediction]
