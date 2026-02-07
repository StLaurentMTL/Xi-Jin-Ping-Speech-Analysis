from HanziNLP import word_tokenize, get_font

# import WordCloud
import pandas as pd
import pprint
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt

speeches = pd.read_csv(
    "/home/lburton12/side_projects/xijinpin_talks/corpus/speeches.csv"
)


def filtering():
    speeches["publication"] = pd.to_datetime(speeches["publication"])

    speeches_2022 = speeches[speeches["publication"].dt.year == 2022]
    speeches_2023 = speeches[speeches["publication"].dt.year == 2023]
    speeches_2024 = speeches[speeches["publication"].dt.year == 2024]
    speeches_2025 = speeches[speeches["publication"].dt.year == 2025]

    # Looking for Speeches mentioning Taiwan

    taiwan_speeches = speeches[speeches["text"].str.contains("台湾")]

    print(taiwan_speeches.head())

    return speeches_2022, speeches_2023, speeches_2024, speeches_2025, taiwan_speeches


def tokenizations(speech_year: pd):
    tokens = []

    for text in speech_year["text"]:
        tokens.extend(word_tokenize(text))

    return tokens


def tokenizing():
    speeches_2022, speeches_2023, speeches_2024, speeches_2025, taiwan_speeches = (
        filtering()
    )
    speeches_2022_token = tokenizations(speeches_2022)
    speeches_2023_token = tokenizations(speeches_2023)
    speeches_2024_token = tokenizations(speeches_2024)
    speeches_2025_token = tokenizations(speeches_2025)
    speeches_token = tokenizations(speeches)
    taiwan_token = tokenizations(taiwan_speeches)

    return (
        speeches_2022_token,
        speeches_2023_token,
        speeches_2024_token,
        speeches_2025_token,
        speeches_token,
        taiwan_token,
    )


(
    speeches_2022_token,
    speeches_2023_token,
    speeches_2024_token,
    speeches_2025_token,
    speeches_token,
    taiwan_token,
) = tokenizing()


def wordcloud():
    text = " ".join(taiwan_token)

    wordcloud = WordCloud(
        font_path=get_font("NotoSerifSC-Medium"),
        width=800,
        background_color="white",
        min_font_size=10,
    ).generate(text)

    plt.figure(figsize=(5, 5), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.title("President Xi Jinping: Speeches mentioning Taiwan")

    plt.show()
