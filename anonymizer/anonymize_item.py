import logging
import dtlpy as dl
from io import BytesIO
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

logger = logging.getLogger(name="presidio-anonymizer")


class PresidioAnonymizer(dl.BaseServiceRunner):
    """
    Service for anonymizing text files using Microsoft Presidio.
    Detects and redacts PII (Personally Identifiable Information) from text.
    """

    def __init__(self):
        """Initialize the Presidio analyzer and anonymizer engines."""
        self.logger = logger
        self.logger.info('Initializing Presidio Anonymizer')
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def anonymize_item(self, item: dl.Item, context: dl.Context) -> dl.Item:
        """
        Anonymize a Dataloop text item by detecting and redacting PII.

        :param item: The Dataloop item to anonymize
        :param context: The execution context containing node configuration
        :return: The uploaded anonymized item
        """
        self.logger.info(f"Anonymizing item {item.id}")
        
        # Get configuration
        node = context.node
        remote_path = node.metadata['customNodeConfig']['overwrite']

        try:
            text = item.download(save_locally=False).getvalue().decode('utf-8')
        except UnicodeDecodeError:
            self.logger.error(f"Item {item.id} cannot be decoded as UTF-8 text")
            raise ValueError(f"Item {item.id} is not a valid text file")
        
        # Analyze and anonymize PII
        results = self.analyzer.analyze(text=text, entities=[], language='en')
        anonymized = self.anonymizer.anonymize(text=text, analyzer_results=results)
        
        # Upload anonymized text back to Dataloop
        buffer = BytesIO(anonymized.text.encode('utf-8'))
        new_item = item.dataset.items.upload(
            local_path=buffer,
            remote_path=remote_path,
            remote_name=item.filename,
            overwrite=True
        )
        
        return new_item

















