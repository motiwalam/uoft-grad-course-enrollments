import os
import sys

import requests

def get_info(course_code, section):
    sess_code = {'F': '20259', 'S': '20261'}[section]
    cookies = {
	'LtpaToken2': os.getenv('LtpaToken2')
    }

    params = {
        'courseCode': course_code,
        'courseSessionCode': sess_code,
        'postCode': 'CS   MSC T',
        'primaryOrgCode': 'SGS',
        'sectionCode': section,
        'sessionCode': sess_code,
    }
    
    response = requests.get(
        'https://acorn.utoronto.ca/sws/rest/enrolment/course/view',
        params=params,
        cookies=cookies,
    )

    return response


def main(course_code, section):
    resp = get_info(course_code, section)
    print(resp.text)


if __name__ == "__main__":
    raise SystemExit(main(*sys.argv[1:]))
