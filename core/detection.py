import re


class PIIDetector:
    def __init__(self, policies):
        self.policies = policies

    def detect(self, text):
        """
        Detect PII in text using loaded policies
        """
        detections = []

        for policy in self.policies:
            content_type = policy["content_type"]
            detection = policy["detection"]
            action = policy["action"]

            detection_type = detection.get("type")

            # Regex detection
            if detection_type == "regex":
                pattern = detection["pattern"]
                matches = [m.group() for m in re.finditer(pattern, text)]
                print("DEBUG DETECTED:", matches)
                if matches:
                    detections.append({
                        "content_type": content_type,
                        "matches": matches,
                        "action": action
                    })

            # Keyword detection
            elif detection_type == "keyword":
                replacements = detection.get("replacements", {})

                for word in replacements.keys():
                    if word in text:
                        detections.append({
                            "content_type": content_type,
                            "matches": [word],
                            "action": action
                        })

        return detections