import logging

logger = logging.getLogger("audit_logger")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("audit.log")
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class AuditLogger:

    @staticmethod
    def log_detection(detected_items):
        for item in detected_items:
            logger.info(f"Detected: {item['content_type']} -> {item['matches']}")
            logger.info(f"Action: {item['action']}")

    @staticmethod
    def log_output(output):
        logger.info(f"Sanitized Output: {output}")
        