from HanziNLP import lda_model, print_topics
import pandas as pd

speeches = pd.read_csv(
    "/home/lburton12/side_projects/xijinpin_talks/corpus/speeches.csv"
)

print(speeches.head())
