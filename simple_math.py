#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2009 Ballistic Pigeon, LLC

def sign(number):
    """Returns 1 if number is positive, -1 if number is negative and 0 if number is 0"""
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0
