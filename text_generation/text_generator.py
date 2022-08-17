import train
import generate


class TextGenerator:
    @staticmethod
    def fit(model, input_dir='stdin'):
        model += '.pickle'
        train.fit(model, input_dir)

    @staticmethod
    def generate(model, length, seed=None):
        model += '.pickle'
        generate.generate(model, length, seed)


TextGenerator.fit('otvet', 'otryad.txt')
TextGenerator.generate('otvet', 1000)
