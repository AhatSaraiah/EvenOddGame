######phase 2

import random

i = 1
rounds = 7
players = {}
players_count = int(input("Enter number of players (minimum 2 players): "))

def init_players(players, players_count):
    '''Initialize players with their names and set their initial scores to 0.

    Args:
    - players (dict): Dictionary to store player names and scores.
    - players_count (int): Number of players.

    Returns:None'''
    for p in range(players_count):
        player = input("Enter player name: ")
        players[player] = 0

def round_winner(rounds, points1, points2, winner):
    '''Check if a player has won the round and update the number of rounds.

    Args:
    - rounds (int): Total number of rounds to be played.
    - points1 (int): Points scored by player 1 in the current round.
    - points2 (int): Points scored by player 2 in the current round.
    - winner (str): Name of the winner in the current round.

    Returns:None'''
    
    if (points1 == (rounds // 2) + 1 or points2 == (rounds // 2) + 1):
        print(winner, "Wins! - it's the best of", rounds, "rounds")
        rounds += 2

def get_winner( player1_name, player2_name, points1, points2):
    '''Determine the winner of a round based on points scored.

    Args:
    - player1_name (str): Name of player 1.
    - player2_name (str): Name of player 2.
    - points1 (int): Points scored by player 1.
    - points2 (int): Points scored by player 2.

    Returns:- str: Name of the winner.'''
    if (points1 > points2):
        winner = player1_name
    else:
        winner = player2_name
    return winner

def print_status(i, player1_name, player2_name, new_round, points1, points2, winner):
     
    '''Print the status of the current round, including random number, scores, and winner.
    Args:
    - i (int): Round number.
    - player1_name (str): Name of player 1.
    - player2_name (str): Name of player 2.
    - new_round (int): Random number generated for the round.
    - points1 (int): Points scored by player 1.
    - points2 (int): Points scored by player 2.
    - winner (str): Name of the winner.
    Returns: None'''
    
    print("Round #", i, ", random number is", new_round, winner, "scored!")
    print("Status:", player1_name, points1, ",", player2_name, points2)

def get_rand_players(players):
    ''' Get two random players from the dictionary.
    Args:
    - players (dict): Dictionary containing player names and scores.

    Returns:
    - tuple: Names of two randomly selected players.'''
    player1_name, player2_name = random.sample(players.keys(), 2)
    return player1_name, player2_name



def round(player1_name, player2_name):
    '''Simulate a regular round and update scores accordingly.

        Args:
        - player1_name (str): Name of player 1.
        - player2_name (str): Name of player 2.

        Returns:- tuple: Random number, updated score of player 1, updated score of player 2. '''
    rand = random.randint(-5, 13)
    if rand % 2 == 0:
        players[player1_name] += 1
    else:
        players[player2_name] += 1
    return rand, players[player1_name], players[player2_name]

def even_odd_game(i, rounds, players):
    '''Simulate the entire game.

    Args:
    - i (int): Round number.
    - rounds (int): Total number of rounds to be played.
    - players (dict): Dictionary containing player names and scores.
    Returns:None '''
    i = 1
    boss=0
    while rounds not in players.values():
        player1_name, player2_name = get_rand_players(players)
        new_round, points1, points2 = round(player1_name, player2_name)
        winner = get_winner(player1_name, player2_name, points1, points2)
        print_status(i, player1_name, player2_name, new_round, points1, points2, winner)
        i += 1
        round_winner(rounds, points1, points2, winner)
      

init_players(players, players_count)
even_odd_game(i, rounds, players)

    



