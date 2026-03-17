"""Using different delimiters."""

from digin import NestedDict

data = {"a": {"b": {"c": {"d": 42}}}}

# Default: ->
nd1 = NestedDict(data)
print("->  delimiter:", nd1.get("a->b->c->d"))

# Dot
nd2 = NestedDict(data, ".")
print(".   delimiter:", nd2.get("a.b.c.d"))

# Slash (filesystem-like)
nd3 = NestedDict(data, "/")
print("/   delimiter:", nd3.get("a/b/c/d"))

# Double colon
nd4 = NestedDict(data, "::")
print("::  delimiter:", nd4.get("a::b::c::d"))

# Pipe
nd5 = NestedDict(data, "|")
print("|   delimiter:", nd5.get("a|b|c|d"))
