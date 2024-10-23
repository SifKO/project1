"""
Config of our flask app
"""

import os


class Config:
    """
    class for config flask app, storing config variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '111cc8c7d71403a3c6fb750670d95c7ec6'
    WTF_CSRF_SECRET_KEY = os.environ.get(
        'WTF_CSRF_SECRET_KEY') or '121cc8c7q71403a3c6fb720670d95c7ec6'
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LdndGUqAAAAAFRf4C7CKlAE3P-SsW3BxJ7iKUAB'
    RECAPTCHA_PRIVATE_KEY = '6LdndGUqAAAAAADCm5hj3GX4nFPw4qc1g7_MDyuS'
    RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}

    # for files store
    UPLOAD_FOLDER = os.environ.get(
        'UPLOAD_FOLDER') or '/home/kid/Projects/lab1_TUSUR/image_processor/static/uploads'
    # Allowed files
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
