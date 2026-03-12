class Ranker:

    def rank(self, results):

        ranked = sorted(results, key=lambda x: x[1])

        return ranked
