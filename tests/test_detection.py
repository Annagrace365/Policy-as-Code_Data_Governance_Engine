import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.policy_loader import PolicyLoader
from core.detection import PIIDetector


def test_pii_detection():

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    policy_path = os.path.join(project_root, "config", "policy.yaml")

    loader = PolicyLoader(policy_path)
    policies = loader.load_policy_file()

    detector = PIIDetector(policies)

    text = """
    Contact me at abc@gmail.com
    My phone number is 9876543210
    """

    detections = detector.detect(text)

    print("\nDetected PII:\n")

    for d in detections:
        print(f"Content Type: {d['content_type']}")
        print(f"Matches: {d['matches']}")
        print(f"Action: {d['action']}")
        print()


if __name__ == "__main__":
    test_pii_detection()