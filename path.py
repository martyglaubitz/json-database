from dataclasses import dataclass

import os.path

from urllib.parse import urlparse

import configuration

def path_segments_from_url(url: str):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')

    return PathSegments(document_name = path_parts[-1], path_to_document = [part for part in path_parts[:-1] if part])
    

@dataclass
class PathSegments:

    document_name: str

    path_to_document: list




