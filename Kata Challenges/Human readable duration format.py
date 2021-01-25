'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
'''


def format_duration(seconds):
    if seconds == 0:
        return 'now'

    output = []
    data = {31536000 :'year', 86400: 'day', 3600: 'hour', 60: 'minute', 1: 'second'}

    for secs, s in data.items():
        if seconds >= secs:
            i = seconds // secs
            seconds -= i * secs

            o = f', {i} {s}'
            if i > 1:
                o += 's'
            output.append(o)

    output[-1] = output[-1].replace(',', ' and')
    output = ''.join(output).strip()

    if output.startswith(', '):
        output = output[2:]
    if output.startswith(' and'):
        output = output[5:]

    return output


print(format_duration(456540))
