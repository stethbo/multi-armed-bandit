import numpy as np
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s %(message)s")

class Bandit:
    def __init__(self, probs: list[float]) -> None:
        '''
        :param list probs: probabilities of following bandits
            len(probs) >= 2
            probs[i] in <0, 1>
        '''
        assert len(probs) > 2, 'List must be longer than 2'
        self.probs = probs
        self.scores = [0] * len(probs)


    def pull(self, i: int) -> int:
        '''
        :param int i: index of the bandit to be used
        '''
        return 1 if np.random.uniform(0, 1) < self.probs[i] else 0
        

if __name__ == '__main__':
    bandits_probs = np.random.randint(2, 10, 20) / 10
    
    mab = Bandit(bandits_probs)

    rounds = 25
    start_index = 0
    total_score = 0
    for _ in range(rounds):
        score = mab.pull(start_index)
        if score == 0:
            index = np.random.randint(0, len(bandits_probs))
        else:
            total_score += 1

    logging.info(f"Overall accuracy {total_score/rounds}")
    logging.info(f"Bandits probs: {bandits_probs}, {np.average(bandits_probs)}")
    