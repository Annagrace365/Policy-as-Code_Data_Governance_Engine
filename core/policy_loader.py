import yaml
import os


class PolicyValidationError(Exception):
    """Custom exception for policy validation errors"""
    pass


class PolicyLoader:
    def __init__(self, policy_file_path: str):
        self.policy_file_path = policy_file_path
        self.policies = []

    def load_policy_file(self):
        """Load YAML policy file"""
        if not os.path.exists(self.policy_file_path):
            raise FileNotFoundError(f"Policy file not found: {self.policy_file_path}")

        try:
            with open(self.policy_file_path, "r") as file:
                data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise PolicyValidationError(f"Invalid YAML syntax: {e}")

        if not data or "policies" not in data:
            raise PolicyValidationError("Missing 'policies' key in YAML file")

        if not isinstance(data["policies"], list):
            raise PolicyValidationError("'policies' must be a list")

        self.policies = data["policies"]
        return self.validate_policies()

    def validate_policies(self):
        """Validate each policy structure"""
        validated_policies = []

        for index, policy in enumerate(self.policies):
            if not isinstance(policy, dict):
                raise PolicyValidationError(f"Policy at index {index} is not a dictionary")

            # Required top-level fields
            required_fields = ["content_type", "detection", "action"]
            for field in required_fields:
                if field not in policy:
                    raise PolicyValidationError(
                        f"Missing '{field}' in policy at index {index}"
                    )

            detection = policy["detection"]
            if not isinstance(detection, dict):
                raise PolicyValidationError(
                    f"'detection' must be a dictionary in policy at index {index}"
                )

            detection_type = detection.get("type")

            if detection_type not in ["regex", "keyword", "none"]:
                raise PolicyValidationError(
                    f"Invalid detection type '{detection_type}' in policy at index {index}"
                )

            # Regex validation
            if detection_type == "regex":
                if "pattern" not in detection:
                    raise PolicyValidationError(
                        f"Missing regex 'pattern' in policy at index {index}"
                    )

            # Keyword validation
            if detection_type == "keyword":
                replacements = detection.get("replacements")
                if not isinstance(replacements, dict) or not replacements:
                    raise PolicyValidationError(
                        f"'replacements' must be a non-empty dictionary in policy at index {index}"
                    )

            # Masking validation (only if action is Mask)
            if policy["action"] == "Mask":
                if "masking_strategy" not in policy:
                    raise PolicyValidationError(
                        f"Missing 'masking_strategy' for Mask action at index {index}"
                    )

            validated_policies.append(policy)

        return validated_policies


# --------- Test Execution (Phase 3 Testing) ---------
if __name__ == "__main__":
    loader = PolicyLoader("./config/policy.yaml")

    try:
        policies = loader.load_policy_file()
        print("✅ Policy file loaded and validated successfully\n")
        for p in policies:
            print(f"- {p['content_type']} | Action: {p['action']}")
    except Exception as e:
        print(f"❌ Policy loading failed: {e}")