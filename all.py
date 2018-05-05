from __future__ import print_function, division
from os import listdir, curdir, path
import json

from ui.report_generator import generate_report

if __name__ == '__main__':
    files = ['static/{}'.format(f) for f in listdir(path.join(curdir, 'static')) if (f.endswith('.jpg') or f.endswith('.png')) and not (f.startswith('sign_') or f.startswith('small_'))]
    results = generate_report(files)

    f = open('static/result.js', 'w')
    f.write('const data = ')
    f.write(json.dumps(results))
