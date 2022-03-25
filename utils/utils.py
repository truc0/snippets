#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random

def generate_random_token(length=6, charset=None):
    if charset is None:
        charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=length))
