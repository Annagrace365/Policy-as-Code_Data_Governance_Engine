import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from evaluation.accuracy import evaluate_accuracy

evaluate_accuracy()