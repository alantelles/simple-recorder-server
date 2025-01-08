#!/bin/bash

record() {
  FOLDER=$1
  mkdir -p $FOLDER
  FILE=$FOLDER/media/$(date  +%Y-%m-%d_%H-%M-%S).wav
  PROC=$FOLDER/recIdPr
  arecord -f cd -D default -V mono -q --process-id-file $PROC $FILE &
}

stop_record() {
  FOLDER=$1
  PROC_ID=$(cat "$FOLDER/recIdPr")
  kill -s SIGINT $PROC_ID
}

$1 $2