# download_nyc_taxi_data.py

import os
import urllib
import urllib.request

print( dir(urllib) )

print('1. urllib.__package__:', urllib.__package__)
print('2. urllib.__path__:', urllib.__path__)
print('3. urllib.__name__:', urllib.__name__)
print('4. urllib.__file__:', urllib.__file__)

print('5. os.getcwd():', os.getcwd())


with open('F:\\app\\git_workspace\\doit_pandas\\data\\raw_data_urls.txt', 'r') as data_urls:
# with open('doit_pandas\\data\\raw_data_urls.txt', 'r') as data_urls:
    for line, url in enumerate( data_urls ):
        url = url.strip()
        print(str(line) + '. url:', url)

        url_split = url.split('/')
        # print('\t- url_split:', url_split)

        fn = url_split[-1]
        # print('\t- fn:', fn)

        fp = os.path.join(os.getcwd(), 'taxi_data', fn)
        # print('\t- fp:', fp)

        print('\t- urllib.request.urlretrieve({}, {})'.format(url, fp))
        urllib.request.urlretrieve(url, fp)
        pass

    pass

