import re


class PIIDetector:
    def __init__(self, policies):
        self.policies = policies

    def detect(self, text):
        """
        Detect PII in text based on loaded policies.
        Returns a list of detections, each as a dict:
        {
            "content_type": ...,
            "matches": [...],
            "action": ...
        }
        """
        detections = []

        for policy in self.policies:
            content_type = policy["content_type"]
            detection = policy.get("detection", {})
            action = policy.get("action", "Allow")

            detection_type = detection.get("type", "none")

            # --- Regex detection ---
            if detection_type == "regex":
                pattern = detection.get("pattern", "")
                if pattern:
                    matches = [m.group() for m in re.finditer(pattern, text)]
                    if matches:
                        detections.append({
                            "content_type": content_type,
                            "matches": matches,
                            "action": action
                        })

            # --- Keyword detection ---
            elif detection_type == "keyword":
                replacements = detection.get("replacements", {})
                for keyword in replacements.keys():
                    # Case-insensitive search
                    if re.search(rf"\b{re.escape(keyword)}\b", text, flags=re.IGNORECASE):
                        detections.append({
                            "content_type": content_type,
                            "matches": [keyword],
                            "action": action
                        })

        return detections