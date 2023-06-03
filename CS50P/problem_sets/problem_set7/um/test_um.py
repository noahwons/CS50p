from um import count

def test_um_sentance():
    assert count("Um, um um.") == 3
    assert count("Um, hello, yummy") == 1

def test_words_containing_um():
    assert count("Yummy") == 0
    assert count("Alphanumerics") == 0

def test_punctuation():
    assert count("Um, um... um?") == 3
    assert count("Yummy, um? um!") == 2