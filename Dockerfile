FROM  hub.dataloop.ai/dtlpy-runner-images/cpu:python3.11_opencv

RUN pip install presidio_analyzer
RUN pip install presidio_anonymizer
RUN python -m spacy download en_core_web_lg


