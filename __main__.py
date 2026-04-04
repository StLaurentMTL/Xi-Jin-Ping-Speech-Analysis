import sys
import argparse
import pathlib
from .markov import Markov

def identify_source(k: int, unknown_text: str, known_sources: list[str]) -> list[int]:
    """
    Given sample text from two or more known sources, return a list with the
    *normalized log probabilities* of each of the sources.

    The list should return probabilities in the same order as the sources in
    `known_sources`.

    Parameters:
        - k: k order for Markov models
        - unknown_text: The text to be identified.
        - known_sources: List of training texts to create models.
    """

    # Initializing normalized probabilities list
    normalized_probs = []

    for source in known_sources:
        source_markov = Markov(k, source)
        normalized = source_markov.log_probability(unknown_text) / len(unknown_text)

        normalized_probs.append(normalized)

    return normalized_probs

def main():
    print("Hello from xijinpin-talks!")


if __name__ == "__main__":
    main()
