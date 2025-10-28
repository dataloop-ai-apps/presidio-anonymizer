# Presidio Anonymizer for Dataloop

This repository provides a **Dataloop** service that integrates **Microsoft Presidio** to automatically detect and anonymize Personally Identifiable Information (PII) in text files. The service is designed to seamlessly integrate into Dataloop pipelines for processing sensitive data while maintaining privacy compliance.

## Features

- **Automatic PII Detection**: Leverages Microsoft Presidio's analyzer to detect various types of PII including names, email addresses, phone numbers, addresses, and more.
- **Text Anonymization**: Replaces detected PII with generic placeholders (e.g., `<PERSON>`, `<EMAIL_ADDRESS>`).
- **Multi-format Support**: Works with any UTF-8 text file including `.txt`, `.json`, `.md`, `.csv`, and more.
- **Flexible Output Options**: Choose to overwrite original files or save anonymized versions to a separate folder.
- **Seamless Pipeline Integration**: Pre-built pipeline node for easy integration into your Dataloop workflows.

## Configuration

When adding the Presidio Anonymizer node to your pipeline, configure:

- **Overwrite**: Choose how to handle the anonymized output:
  - **True** : Overwrites the original file with the anonymized version
  - **False** : Saves the anonymized file to an `/anonymized` folder

## Pipeline Node

**Presidio Anonymizer**

- Takes a text file as input
- Analyzes the content for PII entities
- Anonymizes detected PII with placeholder tags
- Outputs the anonymized file to the configured location

### Example

**Input text:**

```
My name is Ludovit Horvath and my email is ludo.h@gmail.com
```

**Output text:**

```
My name is <PERSON> and my email is <EMAIL_ADDRESS>
```

## Supported PII Types

The service can detect and anonymize various PII types including:

- Person names (`<PERSON>`)
- Email addresses (`<EMAIL_ADDRESS>`)
- Phone numbers (`<PHONE_NUMBER>`)
- Credit card numbers (`<CREDIT_CARD>`)
- Dates of birth (`<DATE_TIME>`)
- Addresses (`<LOCATION>`)
- And many more...

For a complete list, see the [Presidio documentation](https://microsoft.github.io/presidio/supported_entities/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project makes use of the following technologies:

- **[Microsoft Presidio](https://github.com/microsoft/presidio)**: An open-source PII detection and anonymization framework, distributed under the [MIT License](https://github.com/microsoft/presidio/blob/main/LICENSE).
- **[spaCy](https://spacy.io/)**: Industrial-strength NLP library, distributed under the [MIT License](https://github.com/explosion/spaCy/blob/master/LICENSE).
- **[Dataloop](https://dataloop.ai/)**: AI data management and MLOps platform.
