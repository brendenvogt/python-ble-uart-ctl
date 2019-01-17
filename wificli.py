# author: Brenden Vogt
# description: a tool

import argparse
import sys

# introduce encryption
# qr code generation
# wpa_passphrase "testing" < file_where_password_is_stored


class Cli():

    def __init__(self, argString):
        if (argString):
            self.args = argString.split(" ")

    def main(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-ssid", type=str, default="", required=True,
                                 help="The wifi name (ssid) for the wifi network")
        self.parser.add_argument("-password", type=str, default="", required=True,
                                 help="The password for the wifi network")

        if (len(self.args) > 0):
            args = self.parser.parse_args(self.args)
        else:
            args = self.parser.parse_args()

        sys.stdout.write(str(self.handle(args)))

    def handle(self, args):
        x = f"connecting to {args.ssid} with paswd {args.password}\n"
        return x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssid", type=str, default="", required=True,
                        help="The wifi name (ssid) for the wifi network")
    parser.add_argument("--password", type=str, default="", required=True,
                        help="The password for the wifi network")
    args = parser.parse_args()
    sys.stdout.write(str(handle(args)))


def handle(args):
    x = f"connecting to {args.ssid} with paswd {args.password}\n"
    return x


if __name__ == "__main__":
    # --option1
    # main()

    # --option2
    x = Cli("--ssid hello --password test")
    x.main()
