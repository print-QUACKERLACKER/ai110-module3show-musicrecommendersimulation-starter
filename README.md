# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple content-based music recommender that reads songs from a CSV file and ranks them by how well they match a user’s preferred genre, mood, and energy level
---

## How The System Works

Songs are organized by genre, mood, energy, and acousticness. A user profile stores a favorite genre, a preferred mood, a target energy level, and whether they tend to like acoustic sounds. The recommender gives a score to each song by rewarding strong matches on genre and mood, then adding a bonus for energy closeness and acoustic preference.

The recommendation flow from Claude is:

1. Load songs from the CSV catalog.
2. Convert a user profile into a preference dictionary.
3. Score every song against those preferences.
4. Sort the songs by score and return the top results.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the test suite with:

```bash
pytest
```

---

## Sample Recommendation Output

Example output for a user who likes pop, happy songs, and high energy:

Top recommendations:

Sunrise City - Score: 1.00
Because: matches your preferred genre pop; matches your preferred mood happy; energy is close to your target (0.80)

Gym Hero - Score: 0.95
Because: matches your preferred genre pop; mood differs from your preference happy; energy is close to your target (0.80)


---

## Experiments I Tried


- A pop + happy + high-energy profile favored upbeat songs such as Sunrise City.
- A chill profile preferred lofi and ambient tracks because the mood match was stronger.
- Changing the energy target shifted the ranking toward songs with a closer energy value.

---

## Limitations and Risks


- It only uses a small number of song features.
- It does not understand lyrics, artist identity, or listening context.


---

## Reflection

I was mostly confused on the logic of the program, so I had Claude do most of the hand holding. Through the information and instructions generated from my prompt with Claude, I was able to learn of the implementation of music rankings based off the users preferences. 



