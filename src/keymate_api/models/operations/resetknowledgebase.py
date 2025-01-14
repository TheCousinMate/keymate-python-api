"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from keymate_api import utils
from typing import Optional


@dataclasses.dataclass
class ResetknowledgebaseRequest:
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""set this parameter as ''"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResetknowledgebaseStatus:
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The result of the operation"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResetknowledgebaseResponseBody:
    r"""Successful operation"""
    status: Optional[ResetknowledgebaseStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class ResetknowledgebaseResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[ResetknowledgebaseResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

