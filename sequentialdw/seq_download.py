import os
import requests

def convert_bytes_to_mb(bytes_size):
    return bytes_size / (1024 * 1024)  # Convert bytes to megabytes

def seqDownload(base_url, start_index, end_index, custom_iterator, file_extension, output_folder):
    # Your function code here...
