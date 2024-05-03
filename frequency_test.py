from frequency import word_frequencies
import json

def test_pytest():
    f = "pytest"
    d = word_frequencies("files/" + f + ".txt")
    actual = json.dumps(d, sort_keys=True)
    e_file = open("files/" + f + ".out")
    expected = e_file.readline()
    assert actual == expected


def test_turing():
    f = "turing"
    d = word_frequencies("files/" + f + ".txt")
    actual = json.dumps(d, sort_keys=True)
    e_file = open("files/" + f + ".out")
    expected = e_file.readline()
    assert actual == expected

# # IF YOU WOULD LIKE A REAL WORLD MESSY TEXT CHALLENGE, UNCOMMENT THE FOLLOWING TEST
# def test_austen():
#     f = "austen"
#     d = word_frequencies("files/" + f + ".txt")
#     actual = json.dumps(d, sort_keys=True)
#     e_file = open("files/" + f + ".out")
#     expected = e_file.readline()
#     assert actual == expected
