import spacy
import pandas as pd


def find_similarities(df, nlp, noise):
    score = 0

    for orgIdx, user in enumerate(noise['X'].values):
        user_doc = nlp(user)
        ranks = []

        for idx, question in enumerate(df['QUESTIONS'].values):
            if question == "":
                ranks.append((idx, 0))
                continue

            question_doc = nlp(question)
            similarity = user_doc.similarity(question_doc)
            ranks.append((idx, similarity))

        # Sort the similarity scores to find the most similar question
        sorted_ranks = sorted(ranks, key=lambda x: x[1], reverse=True)
        best_idx = sorted_ranks[0][0]

        if best_idx == orgIdx:
            score += 1

    return score / len(df)


def main():
    models = ["en_core_web_sm", "en_core_web_md", "en_core_web_lg"]
    df = pd.read_csv("app/data/data.csv")
    noise = pd.read_csv("app/data/noise.csv")

    for model in models:
        nlp = spacy.load(model)
        score = find_similarities(df, nlp, noise)
        print(f"{model} has accuracy of {score}")


if __name__ == "__main__":
    main()
