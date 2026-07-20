import csv
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_results = []
        for song in self.songs:
            song_dict = _song_to_dict(song)
            score, _ = score_song(_normalize_user_profile(user), song_dict)
            scored_results.append((score, song))

        scored_results.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_results[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        song_dict = _song_to_dict(song)
        _, reasons = score_song(_normalize_user_profile(user), song_dict)
        return " ; ".join(reasons) if reasons else f"This song fits your taste profile."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        songs = []
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def _normalize_user_profile(user_prefs: Any) -> Dict[str, Any]:
    if isinstance(user_prefs, UserProfile):
        return {
            "genre": user_prefs.favorite_genre,
            "mood": user_prefs.favorite_mood,
            "energy": user_prefs.target_energy,
            "likes_acoustic": user_prefs.likes_acoustic,
        }
    if isinstance(user_prefs, dict):
        return {
            "genre": user_prefs.get("genre") or user_prefs.get("favorite_genre"),
            "mood": user_prefs.get("mood") or user_prefs.get("favorite_mood"),
            "energy": user_prefs.get("energy") or user_prefs.get("target_energy"),
            "likes_acoustic": user_prefs.get("likes_acoustic", False),
        }
    raise TypeError("user_prefs must be a dict or UserProfile")


def _song_to_dict(song: Song) -> Dict[str, Any]:
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    normalized = _normalize_user_profile(user_prefs)
    score = 0.0
    reasons: List[str] = []

    if normalized.get("genre") and song.get("genre") == normalized["genre"]:
        score += 0.45
        reasons.append(f"matches your preferred genre {normalized['genre']}")
    elif normalized.get("genre"):
        reasons.append(f"genre differs from your preference {normalized['genre']}")

    if normalized.get("mood") and song.get("mood") == normalized["mood"]:
        score += 0.35
        reasons.append(f"matches your preferred mood {normalized['mood']}")
    elif normalized.get("mood"):
        reasons.append(f"mood differs from your preference {normalized['mood']}")

    if normalized.get("energy") is not None:
        target_energy = float(normalized["energy"])
        energy_gap = abs(float(song.get("energy", 0.0)) - target_energy)
        energy_score = max(0.0, 1.0 - energy_gap)
        score += 0.20 * energy_score
        reasons.append(f"energy is close to your target ({target_energy:.2f})")

    if normalized.get("likes_acoustic") is True:
        if float(song.get("acousticness", 0.0)) >= 0.6:
            score += 0.05
            reasons.append("has an acoustic sound profile")
    elif normalized.get("likes_acoustic") is False:
        if float(song.get("acousticness", 0.0)) <= 0.3:
            score += 0.05
            reasons.append("keeps the sound more electric")

    return round(score, 3), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "This song fits your taste profile."
        scored_results.append((song, score, explanation))

    scored_results.sort(key=lambda item: item[1], reverse=True)
    return scored_results[:k]
