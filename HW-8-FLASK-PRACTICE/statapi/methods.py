import functools
from enum import Enum

import psutil as ps
import json, toml, yaml

# (!) Note: depends on PIP packages: psultil toml pyyaml


__all__ = ('methods')

def _parse_spec(spec):
    """Convert library-internal data structures.
    
    Conversion is done into general Python types.
    """

    if hasattr(spec, '_asdict'):
        # assume namedtuple
        spec = spec._asdict()

    if isinstance(spec, dict):
        return {k: _parse_spec(v) for k, v in spec.items()}
    elif isinstance(spec, list):
        return [_parse_spec(itm) for itm in spec]
    elif isinstance(spec, Enum):
        return spec.name
    return spec

# Dict of a form:
# formatter_name: (mimetype, format_function)
# ...
formatters = {
    'json': ('application/json', json.dumps),
    'toml': ('text', toml.dumps),
    'yaml': ('text', functools.partial(yaml.dump, sort_keys=False)),
    'repr': ('text', repr)
}


def method_api(method, format='json', *args, **kwargs):
    """Call method, parse result and format it accordingly."""
    format = format.lower()
    if format not in formatters:
        raise ValueError(f"Invalid format parameter\nPossible format types are: {', '.join(formatters)}")

    spec = method(*args, **kwargs)
    parsed = _parse_spec(spec)

    mime, func = formatters[format]
    res = func(parsed)

    return res, mime


# dict of methods wrapped for api calls of a form:
# method_name: method_callable

# start building
methods = dict.fromkeys([
    'boot_time', 'cpu_count', 'cpu_freq', 'cpu_percent', 'cpu_stats',
    'cpu_times', 'cpu_times_percent', 'disk_io_counters', 'disk_partitions',
    'getloadavg', 'net_if_stats', 'net_io_counters', 'sensors_battery',
    'swap_memory', 'virtual_memory', 'wait_procs'
]) # deleted methods: 'sensors_fans', 'sensors_temperatures' | raises AttributeError

# get original methods by name
methods = {name: getattr(ps, name) for name in methods}

# patch one as it requires argument
methods['disk_usage'] = functools.partial(ps.disk_usage, '/')

# now wrap methods
methods = {
    name: functools.partial(method_api, func) for name, func in methods.items()
}

if __name__ == '__main__':
    spec = ps.cpu_times()
    res = _parse_spec(spec)

    mtd = methods['cpu_times']
    res, mime = mtd(format='yaml')
    print(f'Yaml res:\n{res}')
