"""my_dataset dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds

# TODO(my_dataset): BibTeX citation
_CITATION = """
"""

# TODO(my_dataset):
_DESCRIPTION = """
"""
_TRAIN_URL = "https://drive.google.com/uc?export=download&id=1IEE-oav-81_Wx1-mCbl_7loIWmaE7P7B"
_TEST_URL = "https://drive.google.com/uc?export=download&id=1MJ9TZIoBbyqGl9BJZaLi84ReRI559bAn"
_IMAGE_SIZE = 32
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)
class MyDataset(tfds.core.GeneratorBasedBuilder):
  """TODO(my_dataset): Short description of my dataset."""

  # TODO(my_dataset): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(my_dataset): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE), #"image": tfds.features.Image(shape=_IMAGE_SHAPE)  
            "label": tfds.features.ClassLabel(
                names=["N", "P"]),
        }),
        supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path)
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path)
            }),
    ]

  def _generate_examples(self, archive):
    """Generate horses or humans images and labels given the directory path.

    Args:
      archive: object that iterates over the zip.

    Yields:
      The image path and its corresponding label.
    """

    for fname, fobj in archive:
      print(fname)
      print(type(fobj))
      if 'N/' in fname:  # if anything other than .png; skip
        label = "N"
        record = {
          "image": fobj,
          "label": label,
        }
      elif 'P/' in fname:
        label= "P"
        record = {
          "image": fobj,
          "label": label,
        }
      else:
        continue
      yield fname, record





















