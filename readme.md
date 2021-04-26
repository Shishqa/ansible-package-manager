# YAAPI - yet another ansible package installer

the name is self-descriptive :)

### Supported package managers

- apt
- pip

## Input format

```ini
hostName1
apt package_1 package_2 ... package_N1
pip package_1 package_2 ... package_M1
hostName2
apt package_1 package_2 ... package_N2
pip package_1 package_2 ... package_M2

...

hostNameK
apt package_1 package_2 ... package_NK
pip package_1 package_2 ... package_MK
```

## Dependencies

- python3
- pip
- ansible

## Usage

Let the input looks like this:
```
$ cat pkg_list
192.168.100.11
192.168.100.12
apt vifm nginx
pip ansible

192.168.100.13
pip pep8
```

To install these packages on these hosts, run
```
./pack pkg_list
```

To uninstall packages, add `-u` flag

