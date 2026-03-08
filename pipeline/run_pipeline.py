import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.policy_loader import PolicyLoader
from core.detection import PIIDetector
from core.enforcement_engine import EnforcementEngine


def run_governance_pipeline(text):

    # Load policies
    loader = PolicyLoader("./config/policy.yaml")
    policies = loader.load_policy_file()

    # Initialize components
    detector = PIIDetector(policies)
    enforcer = EnforcementEngine(policies)

    # Detect sensitive data
    detected_items = detector.detect(text)

    # Apply enforcement
    sanitized_output = enforcer.enforce(text, detected_items)

    return sanitized_output