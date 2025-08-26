#!/bin/bash

function run()
{
	local LOGIN_PATH
	local OPT
	local CUSTOM_USERNAME=

	LOGIN_PATH=client
	while getopts "l:u:" OPT; do
		case $OPT in
			l)
				LOGIN_PATH=$OPTARG;;
			u)
				CUSTOM_USERNAME=$OPTARG;;
			*)
				usage
				return 1;;
			\?)
				usage
				return 1;;
		esac
	done
	shift $((OPTIND-1))

	if [ $# -ne 1 ]; then
		usage
		return 1
	fi

	SCHEMA=$1
	NEW_USERNAME=$SCHEMA
	if [ -n "$CUSTOM_USERNAME" ]; then
		NEW_USERNAME=$CUSTOM_USERNAME
	fi

	BUFF=`mktemp /tmp/my-admin-tools.XXXXXX`
	QUERY="select routine_name, routine_type from information_schema.routines where routine_schema = '$SCHEMA' and definer != '$NEW_USERNAME@%'"
	mysql --login-path=$LOGIN_PATH -N -e "$QUERY" >$BUFF || { rm $BUFF; return 1; }
	SQL=`mktemp /tmp/my-admin-tools.XXXXXX`
	while read -r LINE; do
		NAME=`echo $LINE | awk '{print $1;}'`
		TYPE=`echo $LINE | awk '{print $2;}'`
		echo "drop $TYPE $SCHEMA.$NAME;" >>$SQL
		echo "delimiter //" >>$SQL
		QUERY="show create $TYPE $SCHEMA.$NAME"
		mysql --login-path=$LOGIN_PATH -N -e "$QUERY" | awk -F '\t' '{print $3;}' | sed -e 's/\\n/\n/g' -e 's/\\t/\t/g' >>$SQL
		echo "//" >>$SQL
		echo "delimiter ;" >>$SQL
	done <$BUFF
	rm $BUFF
	sed -r -i -e "s/DEFINER=.*%\`/definer=\`$NEW_USERNAME\`@\`\%\`/" $SQL
	mysql --login-path=$LOGIN_PATH $SCHEMA <$SQL || { rm $SQL; return 1; }
	rm $SQL
	return 0
}

function usage()
{
	echo "my-admin-tools"
	echo "   my-fix-definer-routines - Fix DEFINER for all routines in a schema"
	echo "Usage: $0 [ -l <path> ] [ -u <username> ] <schema>"
	echo "Options:"
	echo "   -l use login path <path> to connect to mysql"
	echo "      Default: client"
	echo "   -u change DEFINER to <username>"
	echo "      Default: <schema>"
}
run $*
exit $?
