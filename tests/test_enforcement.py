import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.policy_loader import PolicyLoader
from core.detection import PIIDetector
from core.enforcement_engine import EnforcementEngine


# Step 1: Load policies
loader = PolicyLoader("./config/policy.yaml")
policies = loader.load_policy_file()

# Step 2: Initialize detection and enforcement
detector = PIIDetector(policies)
enforcer = EnforcementEngine(policies)


# Step 3: Test input text
text = """
Contact me at abc@gmail.com
Call me at 9876543210
My card number is 1234 5678 9012 3456
You are stupid
"""


print("Original Text:\n")
print(text)


# Step 4: Detect PII
detected_items = detector.detect(text)

print("\nDetected Items:\n")
for item in detected_items:
    print(item)


# Step 5: Apply enforcement
sanitized_text = enforcer.enforce(text, detected_items)

print("\nSanitized Output:\n")
print(sanitized_text)