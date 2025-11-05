jq -r '.cells[] | select(.cell_type  == "code") | .source[] | rtrimstr("\n")' $filename
