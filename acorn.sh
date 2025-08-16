#!/bin/sh

LtpaToken2=$(xclip -sel clip -o) python3 acorn.py $@ | jq '.responseObject | {course: .displayName, title: .title + ": " + .meetings.[0].subTitle} + (.meetings.[] | {totalSpace, enrollSpace, enrollmentSpaceAvailable})'

