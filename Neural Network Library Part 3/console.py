import pandas as pd

class console:
    @staticmethod
    def table(m):
        print(pd.DataFrame(m.matrix))
        print("\n")