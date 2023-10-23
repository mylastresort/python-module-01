class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        return -1 if len(coefs) != len(words) else sum([cof * len(wrd) for cof, wrd in zip(coefs, words)])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        return -1 if len(coefs) != len(words) else sum([cof * len(words[i]) for i, cof in enumerate(coefs)])
