# keep default namespace
start {http://www.test.com}doc
start {http://www.test.com}node
end {http://www.test.com}node
end {http://www.test.com}doc

# ignore default namespace
start doc
start node
end node
end doc
