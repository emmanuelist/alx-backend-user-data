#!/usr/bin/env python3
"""
Redaction module.

This module provides a function to redact sensitive information in a message.
"""

import logging
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Redacts sensitive information in a message by replacing specified
    fields with a redaction string.

    Args:
        fields (List[str]): A list of field names to redact.
        redaction (str): The string to replace the sensitive information with.
        message (str): The input message to redact.
        separator (str): The separator character used to separate
        key-value pairs in the message.

    Returns:
        str: The redacted message.

    Example:
        >>> filter_datum(["password", "api_key"], "REDACTED",
        "username=john&password=secret&api_key=123456", "&")
        'username=john&password=REDACTED&api_key=REDACTED'
    """
    pattern = "|".join([f"{field}=[^{separator}]+" for field in fields])
    return re.sub(
        pattern,
        lambda m: f"{m.group(0).split('=')[0]}={redaction}",
        message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter.

        Args:
            fields (List[str]): A list of field names to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)
