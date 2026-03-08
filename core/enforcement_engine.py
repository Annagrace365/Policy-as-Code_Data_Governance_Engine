class EnforcementEngine:
    def __init__(self, policies):
        """
        policies: validated policies from PolicyLoader
        """
        self.policies = policies

    def enforce(self, text, detected_items):
        """
        text: original input text
        detected_items: output from Phase 4 detection
        """
        sanitized_text = text

        for item in detected_items:
            content_type = item["content_type"]
            matches = item["matches"]

            policy = self._get_policy_for_type(content_type)
            if not policy:
                continue

            action = policy["action"]

            if action == "Mask":
                for match in matches:
                    masked = self._mask_value(match)
                    sanitized_text = sanitized_text.replace(match, masked)

            elif action == "Replace":
                replacements = policy.get("detection", {}).get("replacements", {})
                for match in matches:
                    replacement = replacements.get(match.lower(), "[REDACTED]")
                    sanitized_text = sanitized_text.replace(match, replacement)

            elif action == "Block":
                for match in matches:
                    sanitized_text = sanitized_text.replace(match, "[BLOCKED]")
        return sanitized_text

    def _get_policy_for_type(self, content_type):
        for policy in self.policies:
            if policy["content_type"] == content_type:
                return policy
        return None

    def _mask_value(self, value):
        if len(value) <= 2:
            return "*" * len(value)

        visible_chars = 2
        return value[:visible_chars] + "*" * (len(value) - visible_chars)