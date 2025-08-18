#!/bin/sh

python3 acorn.py $@ | jq "$(cat <<JQPROG
    .responseObject
    | {course: .displayName, 
       title: .title + ": " + .meetings.[0].subTitle}
      + (.meetings.[] | {totalSpace, enrollSpace, enrollmentSpaceAvailable})
      + (.meetings.[] | {percentFull: (.enrollSpace - .enrollmentSpaceAvailable)/.enrollSpace * 100})
JQPROG
)"

