import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_job_role(resume_text):
    df = pd.read_csv("data/job_roles.csv")
    job_titles = df["Role"].tolist()
    job_descriptions = df["Skills"].tolist()

    corpus = [resume_text] + job_descriptions

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    ranked_roles = sorted(zip(job_titles, similarity_scores), key=lambda x: x[1], reverse=True)

    return ranked_roles

