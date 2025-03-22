import numpy as np
from googleapiclient.discovery import build
from sklearn.feature_extraction.text import TfidfVectorizer

# YouTube API setup (Replace with your API Key)
API_KEY = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

# Fetch trending video titles
def get_trending_titles(region_code="US", max_results=5):
    response = youtube.videos().list(
        part="snippet,contentDetails", chart="mostPopular", regionCode=region_code, maxResults=max_results
    ).execute()
    return [
        item["snippet"]["title"]
        for item in response.get("items", [])
        if item["snippet"]["categoryId"] != "10"  # Exclude music videos
    ] if "items" in response else []

# Extract keywords from titles
def extract_keywords(titles):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(titles)
    indices = np.argsort(vectorizer.idf_)[::-1]
    features = vectorizer.get_feature_names_out()
    top_keywords = [features[i] for i in indices[:10]]
    return top_keywords

# Generate video titles using trending topics
def generate_titles(trending_titles, templates, num_titles=3):
    if not trending_titles:
        return ["No trending titles found"]
    keywords = extract_keywords(trending_titles)
    return [
        np.random.choice(templates).replace("{keyword}", np.random.choice(keywords))
        for _ in range(num_titles)
    ]

if __name__ == "__main__":
    templates = [
        "How to Master {keyword} in 10 Minutes!",
        "Top 5 {keyword} Hacks You Need to Know",
        "Why {keyword} is Changing Everything!"
    ]
    
    trending_titles = get_trending_titles()
    print("Trending Titles:", trending_titles)
    generated_titles = generate_titles(trending_titles, templates)
    print("Generated Video Titles:", generated_titles)
