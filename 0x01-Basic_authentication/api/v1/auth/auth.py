#!/usr/bin/env python3
""" Module for API authentication
"""
from flask import request
from typing import List, Type, TypeVar


class Auth:
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header"""
        return None

    class User:
        """Class representing a user"""
        pass

    def current_user(self, request=None) -> Type[User]:
        """Method to get the current user"""
        return None
