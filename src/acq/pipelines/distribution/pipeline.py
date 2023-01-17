"""
This is a boilerplate pipeline 'distribution'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import distribution

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = distribution,
            inputs = "training_results_acqu",
            outputs = ["training_results_acq_final", "distribution_training"],
            name = "distribution_training_node"
        ),
        node(
            func = distribution,
            inputs = "testing_results_acqu",
            outputs = ["testing_results_acq_final", "distribution_testing"],
            name = "distribution_testing_node"
        ),
        node(
            func = distribution,
            inputs = "proba_gojek",
            outputs = ["results_acq_final_gojek", "distribution_gojek"],
            name = "distribution_gojek_node"
        ),
        node(
            func = distribution,
            inputs = "proba_grab",
            outputs = ["results_acq_final_grab", "distribution_grab"],
            name = "distribution_grab_node"
        )
    ])
