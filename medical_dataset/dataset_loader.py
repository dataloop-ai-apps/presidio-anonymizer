import logging
import os

import dtlpy as dl

logger = logging.getLogger('medical-dataset-loader')

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')


class DatasetLoader(dl.BaseServiceRunner):

    def __init__(self):
        """
        Initialize the dataset downloader.
        """

        logger.info('Dataset loader initialized.')

    def upload_dataset(self, dataset: dl.Dataset, source: str, progress=None):
        if progress is not None:
            progress.update(progress=0,
                            message='Uploading medical records...',
                            status='Uploading medical records...')

        logger.info(f'Uploading items from {ASSETS_DIR}')
        dataset.items.upload(local_path=ASSETS_DIR)

        if progress is not None:
            progress.update(progress=100,
                            message='Upload complete.',
                            status='Upload complete.')
        logger.info('Dataset upload complete.')
