import os
import re
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from evaluation.test_cases import test_cases
from core.policy_loader import PolicyLoader
from core.detection import PIIDetector
from core.enforcement_engine import EnforcementEngine


def normalize(text):
    """
    Normalize text for fair comparison.
    - Collapse multiple * into one
    - Remove extra spaces
    """
    text = re.sub(r"\*+", "*", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def evaluate_accuracy():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    policy_path = os.path.join(base_dir, "config", "policy.yaml")

    loader = PolicyLoader(policy_path)
    policies = loader.load_policy_file()

    detector = PIIDetector(policies)
    enforcer = EnforcementEngine(policies)

    total = len(test_cases)
    passed = 0
    failed = 0
    failed_cases = []

    print("\nRunning Accuracy Evaluation")
    print("--------------------------------")

    start_time = time.time()

    for case in test_cases:

        text = case["text"]
        expected = case["expected"]

        # Detection
        detections = detector.detect(text)

        # Enforcement
        output = enforcer.enforce(text, detections)

        # Normalized comparison
        if normalize(output) == normalize(expected):
            passed += 1
        else:
            failed += 1
            failed_cases.append({
                "input": text,
                "expected": expected,
                "output": output
            })

    end_time = time.time()

    accuracy = passed / total if total else 0
    duration = end_time - start_time

    print("\nEvaluation Summary")
    print("--------------------")
    print("Total Tests :", total)
    print("Passed      :", passed)
    print("Failed      :", failed)
    print("Accuracy    :", round(accuracy * 100, 2), "%")

    print("\nPerformance")
    print("--------------------")
    print("Execution Time :", round(duration, 3), "seconds")
    print("Throughput     :", round(total / duration, 2), "texts/sec")

    # Show failed cases (limited)
    if failed_cases:
        print("\nFailed Test Cases (showing first 10)")
        print("--------------------------------------")

        for case in failed_cases[:10]:

            print("\nInput   :", case["input"])
            print("Expected:", case["expected"])
            print("Output  :", case["output"])

    print("\nEvaluation Complete\n")