# simple inquiry example
import bluetooth


def main():

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))


if __name__ == '__main__':
    main()
