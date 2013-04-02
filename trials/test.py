#!/usr/bin/env python
import csv
import sqlparser


def test(str):
    print("\n", str, "->")
    tokens = sqlparser.parse(str)
    if tokens:
        print("tokens = ",        tokens)
        print("tokens.columns =", tokens.columns)
        print("tokens.tables =",  tokens.tables)
        print("tokens.where =",   tokens.where)

        csvstr = """F1,F2,F3,F4,F5
"A",2,3,4,5
"B",6,7,8,9
"""
        r = csv.DictReader(csvstr.split("\n"))
        for row in r:
            for col in tokens.columns:
                print(row[col], end="")
            print()

        print

print("Hello, World!")

test("select f1,f5 from xx")
test("fail")
test("select f1, f5")
test("select doesnotexist from xx")
test("select * from xx")
