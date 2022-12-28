"""
This is a boilerplate pipeline 'deployment'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import proba

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = proba,
            inputs = "dropped_dataset_gojek",
            outputs = "proba_gojek",
            name = "proba_gojek_node"
        ),
        node(
            func = proba,
            inputs = "dropped_dataset_grab",
            outputs = "proba_grab",
            name = "proba_grab_node"
        )
    ])
