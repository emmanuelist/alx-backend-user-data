#!/usr/bin/env python3
"""
Redaction module.

This module provides a function to redact sensitive information in a message.
"""

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
