# Debugging Utilities
# def f(globals, locals):
#     import base64
#     code="ZGVmIG1ha2VfcHJpbnRfbG9jYWxzKCk6IAogICAgIyBJbiBhIGZ1bmN0aW9uIHRvIHByZXZlbnQgbG9jYWxzIGFuZCBpbXBvcnRzIGZyb20gbGVha2luZy4KICAgIGdsb2JhbCBtYWtlX3ByaW50X2xvY2FscwogICAgZGVsIG1ha2VfcHJpbnRfbG9jYWxzICAjIE9ubHkgcnVuIHRoaXMgZnVuY3Rpb24gb25jZS4KCiAgICBpbXBvcnQgSVB5dGhvbgogICAgaW1wb3J0IGFzdAogICAgaW1wb3J0IGluc3BlY3QKCiAgICBjbGFzcyBWaXNpdG9yKGFzdC5Ob2RlVmlzaXRvcik6CiAgICAgICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgICAgICBzZWxmLnZhcmlhYmxlcyA9IHNldCgpCiAgICAgICAgZGVmIHZpc2l0X05hbWUoc2VsZiwgbmFtZSk6CiAgICAgICAgICAgIHNlbGYudmFyaWFibGVzLmFkZChuYW1lLmlkKQogICAgICAgICMgVE9ETzogUG9zc2libHkgZGV0ZWN0IHdoZXRoZXIgdmFyaWFibGVzIGFyZSBhc3NpZ25lZCB0by4KCiAgICBBTExPV19UWVBFUyA9IFtpbnQsIGZsb2F0LCBzdHIsIGJvb2wsIGxpc3QsIGRpY3QsIHR1cGxlLCByYW5nZV0KICAgIGRlZiBmaWx0ZXJfdmFyaWFibGVzKHZhcmlhYmxlcywgbG9jYWxzKToKICAgICAgICBmb3IgdiBpbiB2YXJpYWJsZXM6CiAgICAgICAgICAgIGlmIHYgaW4gbG9jYWxzIGFuZCB0eXBlKGxvY2Fsc1t2XSkgaW4gQUxMT1dfVFlQRVM6CiAgICAgICAgICAgICAgICB5aWVsZCB2CiAgCiAgICAjIFVuZm9ydHVuYXRlbHksIHRoZXJlIGRvZXNuJ3Qgc2VlbSB0byBiZSBhIHN1cHBvcnRlZCB3YXkgb2YgZ2V0dGluZwogICAgIyB0aGUgY3VycmVudCBjZWxsJ3MgY29kZSB2aWEgdGhlIHB1YmxpYyBJUHl0aG9uIEFQSXMuIEhvd2V2ZXIsIGJlY2F1c2UKICAgICMgd2UgYXJlIGdldHRpbmcgY2FsbGVkIGZyb20gSVB5dGhvbiBpdHNlbGYgYW5kIHdlIGFyZSBhbHJlYWR5IGluc3BlY3RpbmcKICAgICMgdGhlIHN0YWNrdHJhY2UsIHdlIG1pZ2h0IGFzIHdlbGwganVzdCBwZWVrIGludG8gaXRzIGZyYW1lLi4uCiAgICBpZiBJUHl0aG9uLl9fdmVyc2lvbl9fID09ICI1LjUuMCI6CiAgICAgICAgIyBjb2xhYgogICAgICAgIGRlZiBnZXRfYXN0KGZyYW1lKToKICAgICAgICAgICAgcmV0dXJuIGFzdC5Nb2R1bGUoZnJhbWUuZl9iYWNrLmZfYmFjay5mX2xvY2Fsc1sibm9kZWxpc3QiXSkKICAgICAgICBkZWYgZmluZF9sb2NhbHMoZnJhbWUpOgogICAgICAgICAgICByZXR1cm4gZnJhbWUuZl9sb2NhbHMKICAgICAgICBkZWYgYXRfdG9wX2xldmVsKGZyYW1lKToKICAgICAgICAgICAgcmV0dXJuIGZyYW1lLmZfYmFjay5mX2NvZGUuY29fZmlsZW5hbWUuZW5kc3dpdGgoIklQeXRob24vY29yZS9pbnRlcmFjdGl2ZXNoZWxsLnB5IikKCiAgICBlbGlmIElQeXRob24uX192ZXJzaW9uX18gPT0gIjguNC4wIjoKICAgICAgICAjIGxhYiBjb21wdXRlcnMKICAgICAgICBkZWYgZ2V0X2FzdChmcmFtZSk6CiAgICAgICAgICAgIHJldHVybiBhc3QuTW9kdWxlKGZyYW1lLmZfYmFjay5mX2JhY2suZl9sb2NhbHNbIm5vZGVsaXN0Il0pCiAgICAgICAgZGVmIGZpbmRfbG9jYWxzKGZyYW1lKToKICAgICAgICAgICAgcmV0dXJuIGZyYW1lLmZfbG9jYWxzCiAgICAgICAgZGVmIGF0X3RvcF9sZXZlbChmcmFtZSk6CiAgICAgICAgICAgIHJldHVybiBmcmFtZS5mX2JhY2suZl9jb2RlLmNvX2ZpbGVuYW1lLmVuZHN3aXRoKCJJUHl0aG9uL2NvcmUvaW50ZXJhY3RpdmVzaGVsbC5weSIpCiAgICBlbHNlOgogICAgICAgIHByaW50KGYicHJpbnRfbG9jYWxzKCkgbm90IHN1cHBvcnRlZCBvbiBJUHl0aG9uIHZlcnNpb24ge0lQeXRob24uX192ZXJzaW9uX199IikKCiAgICBkZWYgZ2V0X2NlbGxfbmFtZXMoZnJhbWUpOgogICAgICAgIHRyZWUgPSBnZXRfYXN0KGZyYW1lKQogICAgICAgIHZpc2l0b3IgPSBWaXNpdG9yKCkKICAgICAgICB2aXNpdG9yLnZpc2l0KHRyZWUpCiAgICAgICAgcmV0dXJuIGZpbHRlcl92YXJpYWJsZXModmlzaXRvci52YXJpYWJsZXMsIGZyYW1lLmZfbG9jYWxzKQoKICAgIGRlZiBmaW5kX3doaWNoKGZyYW1lKToKICAgICAgICAjIEZyYW1lIGlzIHRoZSBmcmFtZSB3aG9zZSBsb2NhbHMgd2UgYXJlIGludGVyZXN0ZWQgaW4gcHJpbnRpbmcuCiAgICAgICAgaWYgYXRfdG9wX2xldmVsKGZyYW1lKToKICAgICAgICAgICAgIyBUaGUgcGFyZW50IGZyYW1lIG9mIHRoZSBpbnRlcmVzdGVkIGZyYW1lIGlzIGEgbW9kdWxlLCBtb3N0IGxpa2VseQogICAgICAgICAgICAjICJpbnRlcmFjdGl2ZXNoZWxsIi4gVGhpcyBtZWFucyB3ZSBhcmUgaW4gdGhlIGdsb2JhbCBzY29wZSwgc2luY2UKICAgICAgICAgICAgIyBvbmx5IHRoZSBnbG9iYWwgc2NvcGUgc2hvdWxkIGJlIGRpcmVjdGx5IHJ1biBieSB0aGUgaW50ZXJhY3RpdmUgc2hlbGwuCiAgICAgICAgICAgIHJldHVybiBzZXQoZ2V0X2NlbGxfbmFtZXMoZnJhbWUpKQogICAgICAgICMgVGhlIHBhcmVudCBmcmFtZSBpcyBub3QgYSBtb2R1bGUsIHNvIHdlIGFyZSBpbiBhIGxvY2FsIHNjb3BlLgogICAgICAgIHJldHVybiBzZXQoZnJhbWUuZl9sb2NhbHMpCgogICAgZGVmIHByaW50X2xvY2Fscygqd2hpY2gsIHR5cGVzPUZhbHNlKToKICAgICAgICAiIiJQcmludCB0aGUgbG9jYWwgdmFyaWFibGVzIGluIHRoZSBjYWxsZXIncyBmcmFtZS4iIiIKICAgICAgICBpbXBvcnQgaW5zcGVjdAogICAgICAgICMgY3VycmVudGZyYW1lKCkgZnJhbWUgaXMgcHJpbnRfbG9jYWxzLiBXZSB3YW50IHRoZSBjYWxsZXIncyBmcmFtZQogICAgICAgIGZyYW1lID0gaW5zcGVjdC5jdXJyZW50ZnJhbWUoKS5mX2JhY2sKICAgICAgICBsb2NhbHMgPSBmaW5kX2xvY2FscyhmcmFtZSkKICAgICAgICB3aGljaCA9IHNldCh3aGljaCkgaWYgd2hpY2ggZWxzZSBmaW5kX3doaWNoKGZyYW1lKQogICAgICAgIGxsID0ge2s6IHYgZm9yIGssIHYgaW4gbG9jYWxzLml0ZW1zKCkgaWYgayBpbiB3aGljaH0KICAgICAgICBpZiBub3QgbGw6CiAgICAgICAgICAgIHByaW50KCJwcmludF9sb2NhbHM6IG5vIGxvY2FscyIpCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIHR5cGVzOgogICAgICAgICAgICBwcmludCgiXG4iLmpvaW4oZiJ7a306IHt0eXBlKHYpLl9fbmFtZV9ffSDihpAge3Z9IiBmb3IgaywgdiBpbiBsbC5pdGVtcygpKSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCgiOyAiLmpvaW4oZiJ7a30g4oaQIHtyZXByKHYpfSIgZm9yIGssIHYgaW4gbGwuaXRlbXMoKSkpCgogICAgcmV0dXJuIHByaW50X2xvY2FscwoKcHJpbnRfbG9jYWxzID0gbWFrZV9wcmludF9sb2NhbHMoKQ=="
#     exec(base64.b64decode(code), globals, locals)
# f(globals(), locals())
# del f

def assert_equal(want, got):
    if want == got:
        print("Test case passed.")
        return

    print()
    print("--------- Test case failed. ---------")
    print(f"Want: {repr(want)} (type: {type(want).__name__})")
    print(f"Got:  {repr(got)} (type: {type(got).__name__})")
    print("-------------------------------------")
    print()

def check(fn, *input, expected):
    result = fn(*input)
    if expected != result:
        print(f"{fn.__name__}({', '.join(str(i) for i in input)}) should be {expected}, not {result}.")
    else:
        print(f"Test case passed!")