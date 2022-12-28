"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, model_acq

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_data,
            inputs = "preprocessed_dataset",
            outputs = ["data_train", "data_test", "label_train", "label_test"],
            name = "split_dataset_node"
        ),
        node(
            func = model_acq,
            inputs = ["data_train", "data_test", "label_train", "label_test"],
            outputs = ["training_results_acqu", "testing_results_acqu"],
            name = "model_acq_node"
        )
    ])
