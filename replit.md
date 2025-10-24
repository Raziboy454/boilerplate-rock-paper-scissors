# Rock Paper Scissors - Machine Learning Project

## Overview
This is a FreeCodeCamp Machine Learning with Python project. It's a Rock Paper Scissors game where you build an AI player that can defeat various bot opponents at least 60% of the time.

## Project Structure
- `main.py` - Entry point that runs the game simulations
- `RPS.py` - Contains the player function to be implemented
- `RPS_game.py` - Game logic and bot opponents (DO NOT MODIFY)
- `test_module.py` - Unit tests to verify the player wins >60% of games

## How to Run
The project runs automatically via the workflow, executing `main.py` which:
1. Plays 1000 games against each bot (quincy, abbey, kris, mrugesh)
2. Reports win rates for each match

To run manually: `python main.py`
To run tests: Uncomment the test line in main.py or run `python test_module.py`

## Recent Changes
- 2025-10-11: Initial setup for Replit environment
  - Installed Python 3.11
  - Configured workflow for console output
  - Created project documentation

## Project Architecture
- **Language**: Python 3.11
- **Type**: CLI/Console application
- **Game Logic**: Multiple bot opponents with different strategies
  - `quincy`: Plays a fixed pattern
  - `abbey`: Uses Markov chains to predict next move
  - `kris`: Counters the opponent's last move
  - `mrugesh`: Counters most frequent move in last 10 plays

## User Preferences
None configured yet.
