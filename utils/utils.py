#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random
import os


def get_conf(field, conf, default=None):
    """Try to get config from environ variables and config obj"""
    return os.environ.get(field, getattr(conf, field, default))


def generate_random_token(length=6, charset=None):
    if charset is None:
        charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=length))
