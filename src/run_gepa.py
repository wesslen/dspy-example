import dspy

import os
from dotenv import load_dotenv

from sacrebleu.metrics import BLEU
# Import the optimizer
from dspy.teleprompt import GEPA
from dspy.evaluate import Evaluate
from phoenix.otel import register

import pandas as pd

# configure the Phoenix tracer
tracer_provider = register(
  project_name="my-dspy-gepa-app", # Default is 'default'
  auto_instrument=True # Auto-instrument your app based on installed OI dependencies
)

# Load environment variables from .env file
load_dotenv()

lm = dspy.LM("openai/accounts/fireworks/models/gpt-oss-20b", api_key = os.environ.get("API_KEY"), base_url="https://api.fireworks.ai/inference/v1")

reflection_lm = dspy.LM("openai/accounts/fireworks/models/kimi-k2-thinking", api_key = os.environ.get("API_KEY"), base_url="https://api.fireworks.ai/inference/v1")

dspy.configure(lm=lm)

class Translation(dspy.Signature):
    """Translate to English"""
    lang = dspy.InputField(desc="language to translate from")
    source = dspy.InputField(desc="a sentence for translation")
    translation = dspy.OutputField(desc="translation in english")

translate = dspy.ChainOfThought(Translation)


def bleu_metric(example, pred, trace=None, pred_name=None, pred_trace=None):
    """
    DSPy metric for BLEU score using sacreBLEU.

    Args:
        example: Training/dev example containing reference text(s)
        pred: Prediction from DSPy program containing generated text

    Returns:
        float: BLEU score (0-100 scale) normalized to 0-1 for DSPy

    Expected format:
        - example.reference: reference text (string)
        - pred.translation: generated text (string)
    """
    # sacrebleu assumes lists
    references = [[example.reference]] # assumes list of list
    hypotheses = [pred.translation ]

    # Calculate BLEU score
    bleu = BLEU()
    score = bleu.corpus_score(hypotheses, references)

    # Return normalized score (BLEU is 0-100, normalize to 0-1)
    return score.score / 100.0

# Assume our ground truth eval dataset is a pandas dataframe
trainset_df = pd.read_csv("data/trainset.csv", index_col=False)

devset_df = pd.read_csv("data/devset.csv", index_col=False)

devset = [
    dspy.Example(source=row.source, reference=row.reference, lang=row.lang).with_inputs("source", "reference", "lang")
    for _, row in devset_df.iterrows()
]

trainset = [
    dspy.Example(source=row.source, reference=row.reference, lang=row.lang).with_inputs("source", "reference", "lang")
    for _, row in trainset_df.iterrows()
]


# Initialize optimizer
teleprompter = GEPA(
    metric=bleu_metric,
    auto="light", # Can choose between light, medium, and heavy optimization runs
    reflection_lm=reflection_lm
)

# Optimize program
print(f"Optimizing program with GEPA...")
optimized_program = teleprompter.compile(
    translate.deepcopy(),
    trainset=trainset
)

# Save optimize program for future use
optimized_program.save(f"./programs/gepa_light_optimized_v1.json")

evaluate_program = Evaluate(devset=devset, metric=bleu_metric, num_threads=2, display_progress=True, display_table=5)

# Evaluate optimized program
print(f"Evaluate optimized program...")
evaluate_program(optimized_program, devset=devset[:])