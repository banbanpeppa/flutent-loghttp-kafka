import requests
import time

def send_logs(file_name='test.log', body={}):
    resp = requests.post(url='http://testing-chenzhiling.loghub.netease.com:16001/{}'.format(file_name), json=body)
    if resp.status_code == 200:
        return True

    return False


def pretty_timestamp(timestamp):
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)))


if __name__ == '__main__':
    while True:
        log = {
            'foo': 'testing',
            'collect_time': pretty_timestamp(time.time()),
        }
        send_logs('app.log', log)
        time.sleep(2)