from pyparsing import Literal, CaselessLiteral, Word, Upcase, delimitedList, Optional, \
	Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
	ZeroOrMore, restOfLine, Keyword

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

def parse(sql):
	tokens = []
	try:
		tokens = simpleSQL.parseString(sql)
	except ParseException as err:
		print(" "*err.loc + "^\n" + err.msg)
		print(err)

	return tokens
