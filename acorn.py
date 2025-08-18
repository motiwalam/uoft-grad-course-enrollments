import sys
import acornapi
import json

def get_info(utorid, password, course_code, section):
    sess_code = {'F': '20259', 'S': '20261'}[section]

    with acornapi.ACORNWithCachedAuth(utorid, password) as acorn:
        return acorn.course_registration_info(
            course_code,
            section,
            sess_code,
            registration_params={
                "postCode": "CS   MSC T",
                "primaryOrgCode": "SGS",
            }
        )


def main(utorid, password, course_code, section):
    resp = get_info(utorid, password, course_code, section)
    print(json.dumps(resp))


if __name__ == "__main__":
    raise SystemExit(main(*sys.argv[1:]))
