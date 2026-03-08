import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.policy_loader import PolicyLoader


def test_policy_loader():

    loader = PolicyLoader("./config/policy.yaml")
    policies = loader.load_policy_file()

    print("\nLoaded Policies:\n")

    for policy in policies:
        print(f"Content Type: {policy['content_type']}")
        print(f"Action: {policy['action']}")
        print(f"Detection Type: {policy['detection']['type']}")
        print("-" * 40)


if __name__ == "__main__":
    test_policy_loader()