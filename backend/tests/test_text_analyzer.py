from app.services.text_analyzer import analyze_text


def test_basic_text_analysis():
    text = "Hello world. Hello again!"

    result = analyze_text(text)

    assert result["word_count"] == 4
    assert result["sentence_count"] == 2
    assert result["char_count_with_spaces"] == len(text)
    assert result["char_count_without_spaces"] == len(text.replace(" ", ""))


def test_stop_words_removed_from_top_words():
    text = "The fox and the dog"

    result = analyze_text(text)

    top_words = [w["word"] for w in result["top_words"]]

    assert "the" not in top_words
    assert "and" not in top_words
    assert "fox" in top_words
    assert "dog" in top_words


def test_contractions_count_as_one_word():
    text = "Don't stop believing."

    result = analyze_text(text)

    assert result["word_count"] == 3

def test_sample_input_from_assignment():
    text = """
The quick brown fox jumps over the lazy dog. The dog barked, but the fox kept running!

Fox and dog... they're actually friends. The fox visits the dog every day, and the dog always welcomes the fox. It's a beautiful friendship.

Don't you love stories about animals? Animals bring joy and happiness. The fox and the dog are proof that friendship has no boundaries!
"""

    result = analyze_text(text)

    assert result["word_count"] == 64
    assert result["char_count_with_spaces"] == 365
    assert result["char_count_without_spaces"] == 300
    assert result["sentence_count"] == 9

    top_words = {w["word"]: w["count"] for w in result["top_words"]}

    assert top_words["fox"] == 6
    assert top_words["dog"] == 6