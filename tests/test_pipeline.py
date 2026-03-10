import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.run_pipeline import run_governance_pipeline  # make sure this points to your pipeline file

if __name__ == "__main__":
    # Sample texts to test
    texts = [
        "Contact me at john.doe@example.com for details.",
        "Call me at 9876543210 tomorrow.",
        "This is a safe text with no PII."
    ]

    for i, text in enumerate(texts, start=1):
        print(f"\n--- Test Case {i} ---")
        print("Original Text: ", text)
        sanitized = run_governance_pipeline(text)
        print("Sanitized Output: ", sanitized)