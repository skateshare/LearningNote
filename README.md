
json_string='{"name": "John", "age": 30}'
dictionary=$(echo "${json_string}" | jq -r 'to_entries | map("\(.key)=\(.value|tostring)") | join("&")' | sed 's/\"//g' | sed 's/\ //g' | tr '\n' '&')
echo "${dictionary}"
