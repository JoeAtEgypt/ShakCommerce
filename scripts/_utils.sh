
# Arg1 is the str
# Arg2 (Optional) delimiter default="_"
# return string as Pascal ex: "hello_world" -> "HelloWorld"
classify() {
  str=$1
  delimiter=${2:-"_"} # set default delimiter
  # shellcheck disable=SC2207
  arr=($(echo "$str" | tr "$delimiter" " "))
  res=""
  for w in "${arr[@]}"; do
    res+="$(tr '[:lower:]' '[:upper:]' <<<"${w:0:1}")${w:1}"
  done
  echo "$res"
}
