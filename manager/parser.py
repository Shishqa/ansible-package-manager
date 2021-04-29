import copy


pkg_managers = set(['apt', 'pip'])


def init_host_pkg(host, host_pkg):
    host_pkg[host] = {}
    for manager in pkg_managers:
        host_pkg[host][manager] = []


def finalize_group(hosts, pkg, host_pkg):
    for host in hosts:
        if host not in host_pkg:
            init_host_pkg(host, host_pkg) 
        for manager in pkg:
            if manager not in host_pkg[host]:
                host_pkg[host][manager] = []
            host_pkg[host][manager] += copy.deepcopy(pkg[manager])
    hosts.clear()
    pkg.clear()


def get_chunks(reader):
    line = reader.get().rstrip()
    while len(line) == 0:
        reader.next()
        line = reader.get().rstrip()
    return line.split(' ')


def collect_hosts(reader):
    hosts = set()
    while not reader.end():
        chunks = get_chunks(reader)
        if chunks[0] in pkg_managers:
            break
        elif len(chunks) > 1:
            raise
        else:
            hosts.add(chunks[0])
        reader.next()
    print(hosts)
    return hosts


def collect_pkg(reader):
    pkg = {}
    while not reader.end():
        chunks = get_chunks(reader)
        if not chunks[0] in pkg_managers:
            break
        elif chunks[0] in pkg:
            pkg[chunks[0]] += chunks[1:]
        else:
            pkg[chunks[0]] = chunks[1:]
        reader.next()
    print(pkg)
    return pkg


def parse_group(reader, host_pkg):
    hosts = collect_hosts(reader)
    pkg = collect_pkg(reader)
    finalize_group(hosts, pkg, host_pkg)


def parse(reader):
    host_pkg = {}
    while not reader.end():
        parse_group(reader, host_pkg)
    return host_pkg
