#!/usr/bin/env bash
NEXT_ID=`ls kennel/db/versions/* | grep -P '/\d{4}_.*\.py$' | wc -l`
alembic revision -m $@ --rev-id=`printf "%04d" ${NEXT_ID}`
