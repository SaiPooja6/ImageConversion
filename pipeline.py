"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import grayscale_image, size_conversion, adding_text


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func= grayscale_image,
            inputs = "Inputimage",
            outputs = "OutputGrayscaledImage",
            name="grayscale_image",

        ),
        node(
             func= size_conversion,
            inputs = "OutputGrayscaledImage",
            outputs = "OutputGrayscaledSizeConvertedImage",
            name="size_conversion",

        ),
        node(
            func = adding_text,
            inputs = "OutputGrayscaledSizeConvertedImage",
            outputs = "OutputGrayscaledresizedTextImage",
            name = "adding_text"

        )
    ])
