curl -sc /tmp/gcokie "${ggURL}&id=${ggID}" >/dev/null  
getcode="$(awk '/_warning_/ {print $NF}' /tmp/gcokie)"  
curl -LOJb /tmp/gcokie "${ggURL}&confirm=${getcode}&id=${ggID}" 
