import re
from collections import Counter

STOP_WORDS = {"the", "a", "an", "is", "are", "was", "were", "in", "on", "at",
              "to", "and", "or", "but", "of", "for", "with", "not", "it", "this", "that"}

def analyze_text(text: str):
    text = text.strip()

    # ELLIPSIS = "…"
    # text_for_sentences = text.replace("...", ELLIPSIS)
    # sentence_count = len([s for s in re.split(r"[.!?…]", text_for_sentences) if s.strip()])
    sentences = re.split(r"[.!?…]+", text)
    sentence_count = len([s for s in sentences if s.strip()])

    clean_text = re.sub(r'[^\w\s\']', '', text.lower())
    words = clean_text.split()
    word_count = len(words)

    filtered_words = [w for w in words if w not in STOP_WORDS]
    top_words_counter = Counter(filtered_words).most_common(5)
    top_words = [{"word": w, "count": c} for w, c in top_words_counter]

    char_count_with_spaces = len(text)
    char_count_without_spaces = len("".join(text.split()))

    return {
        "word_count": word_count,
        "char_count_with_spaces": char_count_with_spaces,
        "char_count_without_spaces": char_count_without_spaces,
        "sentence_count": sentence_count,
        "top_words": top_words
    }