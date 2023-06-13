#!/usr/bin/python3
def multiple_returns(sentence):
    sl = len(sentence)
    first = sentence[0] if sl > 0 else None
    pair = sl, first
    return (pair)
