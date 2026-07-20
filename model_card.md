# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeMatch 1.0

---

## 2. Intended Use

This recommender is designed for classroom exploration and small-scale demonstration. It generates music recommendations for a user based on a short taste profile, such as preferred genre, mood, and energy level. It assumes the user wants songs that are similar in a simple, human-readable way rather than a highly personalized recommendation from a large streaming service.

---

## 3. How the Model Works

The system uses a few basic song features: genre, mood, energy, and acousticness. A user profile includes a favorite genre, a favorite mood, a target energy level, and a preference for or against acoustic songs. The model scores each song by rewarding direct matches on genre and mood, then giving extra credit when the song’s energy level is close to the user’s target and when the acousticness fits their taste. The final ranking is simply the highest-scoring songs first.

---

## 4. Data

The model uses a small catalog of 10 songs stored in the CSV file in the data folder. The songs span several genres and moods, including pop, lofi, rock, ambient, jazz, synthwave, and indie pop. The dataset is small and curated, so it does not capture the full complexity of real musical taste.

---

## 5. Strengths

The recommender works well for simple user profiles because it is easy to understand and explain. It gives sensible results when a user clearly prefers one genre or mood, and it is especially useful for seeing how structured features can turn into ranked recommendations.

---

## 6. Limitations and Bias

This system has important limits. It does not consider lyrics, cultural context, artist popularity, or user history, so it can miss what a real recommender would learn from richer data. It may also over-represent a single genre or mood if a user profile is too narrow, and it may not be fair or useful for users with diverse or changing tastes.

---

## 7. Evaluation

I evaluated the system by trying a few different user profiles and checking whether the output matched expectations. A pop-focused, happy, high-energy profile ranked upbeat songs higher, while chill profiles favored lofi and ambient songs. The tests also confirmed that the recommender returns a non-empty explanation for each suggested song.

---

## 8. Future Work

In the future, I would add more features such as tempo, danceability, and listening history. I would also improve diversity in the top recommendations so the system does not repeat similar songs too often. Better explanation text and richer preference modeling would make the recommender more helpful and realistic.

---

## 9. Personal Reflection

This project helped me see that recommendation systems are built from simple rules that become powerful when they are tested and refined. I also learned that even a small recommender can reflect bias if the data and feature choices are limited, which is an important lesson for real-world AI systems.  
