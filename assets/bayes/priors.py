import matplotlib.pyplot as plt
hyp_space = range(2, 30)
prior = map(lambda x: 1./x, hyp_space)
prior[:5] = [0.2]*5
prior = map(lambda x: x/sum(prior), prior)
fig, ax = plt.subplots()
ax.bar(hyp_space, prior); ax.set_title('Hypothesis Probabilities (I\'ve seen too many 2, 3, 4, 5, 6 sided dice in my life, so I gave them higher probabilities)'); 
ax.set_xticks(hyp_space)
ax.set_xlabel('Hypothesis'); ax.set_ylabel('Prior Probability') 
hyp_space_l = map(str, hyp_space)
hyp_space_l[-1] = '28+'
ax.set_xticklabels(hyp_space_l); plt.show()

from thinkbayes import Suite

class Dice(Suite):
    """Represents hypotheses about which die was rolled."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: integer number of sides on the die
        data: integer die roll
        """
        if hypo < data:
            return 0
        else:
            return 1.0/hypo




suite = Dice(hyp_space)
prior_ = {i:j for (i, j) in zip(range(2,30), prior)}
suite.d = prior_
suite.Update(3)
print 'After one 3'
suite.Print()
suite.UpdateSet([4, 2, 5, 4, 6, 4, 7, 4])
print 'After more rolls'
suite.Print()
fig, ax = plt.subplots()
ax.bar(suite.d.keys(), suite.d.values()); 
ax.set_xticks(hyp_space)
ax.set_title('Likelihood of each hypothesis'); ax.set_xlabel('Hypothesis'); ax.set_ylabel('Probability') 
ax.set_xticklabels(hyp_space_l); plt.show()