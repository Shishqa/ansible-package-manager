import reader as rd


pkg_managers = set(['apt', 'pip'])


def finalize_group(hosts, pkg, host_pkg):
    for host in hosts:
        host_pkg[host] = {}
        for manager in pkg_managers:
            if manager in pkg:
                host_pkg[host][manager] = pkg[manager][:]  # copy
            else:
                host_pkg[host][manager] = []
    hosts.clear()
    pkg.clear()


def parse_group(reader, host_pkg):
    hosts = []
    pkg = {}
    hosts_collected = False

    while not reader.end():
        line = reader.get().rstrip()
        if len(line) == 0:
            reader.next()
            continue
        line_split = line.split(' ')
        if line_split[0] in pkg_managers:
            hosts_collected = True
            if line_split[0] in pkg:
                pkg[line_split[0]] += line_split[1:]
            else:
                pkg[line_split[0]] = line_split[1:]
        elif not hosts_collected:
            hosts.append(line_split[0])
        else:
            break
        reader.next()
    finalize_group(hosts, pkg, host_pkg)


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()


def parse(path):
    reader = rd.Reader(read_lines(path))
    host_pkg = {}
    while not reader.end():
        parse_group(reader, host_pkg)
    return host_pkg
