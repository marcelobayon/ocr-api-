from app.ocr import extract_text

def test_extract_text_from_sample_image():
    with open("tests/sample.png", "rb") as f:
        text = extract_text(f.read())
    assert isinstance(text, str)
    assert len(text) > 0  # Simplistic test
