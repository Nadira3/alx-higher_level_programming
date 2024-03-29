#!/usr/bin/python3
""" Log parse module """

if __name__ == "__main__":
    import sys
    import signal

    count = 0
    total_size = 0
    obj = {}
    statusCode = ""

    def handle_print():
        """ module documentation """
        print(f"File size: {total_size}")
        for key, value in sorted(obj.items()):
            try:
                code = int(key)
            except ValueError:
                continue
            print(f"{key}: {value}")

    def handle_interrupt(signal, frame):
        """ module documentation """
        handle_print()

    signal.signal(signal.SIGINT, handle_interrupt)

    for line in sys.stdin:
        if count >= 10 or line == "":
            count = 0
            handle_print()
        try:
            statusCode = line.split()[-2]

            if statusCode in obj:
                obj[statusCode] += 1
            else:
                obj[statusCode] = 1

            count += 1
            total_size += int(line.split()[-1])
        except (ValueError, IndexError):
            continue

    handle_print()
