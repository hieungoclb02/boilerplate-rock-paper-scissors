# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[]):
    import random
    if prev_play:
        opponent_history.append(prev_play)
    if len(opponent_history)<5:
        return random.choice(['P','S','R'])

    last_moves=''.join(opponent_history[-3:])
    patterns={}
    for i in range(len(opponent_history)-3):
        key=''.join(opponent_history[i:i+3])
        next_move=opponent_history[i+3]
        if key==last_moves:
            patterns[next_move]=patterns.get(next_move,0)+1

    if patterns:
        predicted=max(patterns,key=patterns.get)
    else:
        predicted = random.choice(["R", "P", "S"])

    # Trả về nước **thắng** dự đoán
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[predicted]
