#!/usr/bin/env python
import csv
from pyparsing import Literal, CaselessLiteral, Word, Upcase, delimitedList, Optional, \
	Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
	ZeroOrMore, restOfLine, Keyword

def test( str ):
	print(str,"->")
	try:
		tokens = simpleSQL.parseString(str)
		print("tokens = ",        tokens)
		print("tokens.columns =", tokens.columns)
		print("tokens.tables =",  tokens.tables)
		print("tokens.where =", tokens.where)

		a = """F1,F2,F3,F4,F5
"A",2,3,4,5
"B",6,7,8,9
"""
		r = csv.DictReader(a.split("\n"))
		for row in r:
			for col in tokens.columns:
				print(row[col], end="")
			print()
	except ParseException as err:
		print(" "*err.loc + "^\n" + err.msg)
		print(err)
	print


print("Hello, World!")

# define SQL tokens
selectStmt = Forward()
selectToken = Keyword("select", caseless=True)
fromToken   = Keyword("from", caseless=True)

ident          = Word( alphas, alphanums + "_$" ).setName("identifier")
columnName     = Upcase( delimitedList( ident, ".", combine=True ) )
columnNameList = Group( delimitedList( columnName ) )
tableName      = Upcase( delimitedList( ident, ".", combine=True ) )
tableNameList  = Group( delimitedList( tableName ) )

selectStmt      << ( selectToken +
                   ( '*' | columnNameList ).setResultsName( "columns" ) +
                   fromToken +
                   tableNameList.setResultsName( "tables" ) )

simpleSQL = selectStmt
test("select f1,f5 from xx")

