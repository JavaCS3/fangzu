#!/usr/bin/env bash
set -e

DB=${DB}
BUCKET=${BUCKET}
YEAR=$1
DEST_DIR=$2

FILENAMES=$(aws s3 ls s3://${BUCKET}/${YEAR}/ --recursive | awk '{ print $4 }' | grep ${DB})
mkdir -p ${DEST_DIR}
echo "${FILENAMES}" | xargs -P 5 -I {} -t aws s3 cp s3://${BUCKET}/{} ${DEST_DIR}