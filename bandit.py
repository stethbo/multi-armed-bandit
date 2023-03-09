import numpy as np
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s %(message)s")

class Bandit:
    def __init__(self, prob: int) -> None:
        self.prob = prob / 10
        self.score = 0

    def pull(self):
        if np.random.uniform(0, 1) < self.prob:
            self.score += 1
            return 1
        else:
            self.score -= 1
            return -1
        
    def get_info(self):
        return self.prob, self.score
    

bandit_a = Bandit(np.random.randint(2, 8))
bandit_b = Bandit(np.random.randint(2, 8))
bandit_c = Bandit(np.random.randint(2, 8))

for n in range(100):
    bandit_a.pull()
    bandit_b.pull()
    bandit_c.pull()

logging.info(f" {bandit_a.score=}, {bandit_a.prob=}")
logging.info(f" {bandit_b.score=}, {bandit_b.prob=}")
logging.info(f" {bandit_c.score=}, {bandit_c.prob=}")
