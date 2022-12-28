"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import matrix_confusion, score

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = score,
            inputs = ["training_results_acqu", "testing_results_acqu"],
            outputs = "metrics_evaluation",
            name = "metrics_eval_node"
        )
    ])
