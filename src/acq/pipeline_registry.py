"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


from acq.pipelines import data_preprocessing as dp
from acq.pipelines import modeling as md
from acq.pipelines import distribution as db
from acq.pipelines import model_evaluation as me
from acq.pipelines import deployment as dpl



def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.
    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_preprocessing_pipeline = dp.create_pipeline()
    modeling_pipeline = md.create_pipeline()
    distribution_pipeline = db.create_pipeline()
    model_evaluation_pipeline = me.create_pipeline()
    deployment_pipeline = dpl.create_pipeline()
    pipelines = find_pipelines()
    pipelines["__default__"] = data_preprocessing_pipeline + modeling_pipeline + distribution_pipeline + model_evaluation_pipeline + deployment_pipeline

    return pipelines
    return {
        "__default__": data_preprocessing_pipeline + modeling_pipeline + distribution_pipeline + model_evaluation_pipeline + deployment_pipeline,
        "dp": data_preprocessing_pipeline,
        "md": modeling_pipeline,
        "db": distribution_pipeline,
        "me": model_evaluation_pipeline,
        "dpl": deployment_pipeline
    }