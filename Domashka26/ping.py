import platform
import subprocess


def ping_websites(sites, ping_count):
    platform_name = platform.system().lower()
    for site in sites:
        ping_count_attribute = '-c'
        if platform_name == 'windows':
            ping_count_attribute = '-n'
        ping_command = ['ping', ping_count_attribute, str(ping_count), site]
        result = subprocess.run(ping_command, shell=True, capture_output=True, text=True)
        print(result.stdout)


if __name__ == '__main__':
    ping_websites(['google.com', 'fb.com', 'youtu.be'], 3)
