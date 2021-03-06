#
# Copyright (c) 2019-2020 Red Hat, Inc.
#
# This file is part of nmstate
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

from distutils.version import StrictVersion
import os
import re

from .cmdlib import exec_cmd


def is_fedora():
    return os.path.exists("/etc/fedora-release")


def is_nm_older_than_1_25_2():
    _, output, _ = exec_cmd(["nmcli", "-v"], check=True)
    match = re.compile("version ([0-9.]+)").search(output)
    assert match

    return StrictVersion(match.group(1)) < StrictVersion("1.25.2")


def nm_is_not_supporting_ovs_patch_port():
    _, output, _ = exec_cmd(["nmcli", "-v"], check=True)
    match = re.compile("version ([0-9.]+)").search(output)

    return StrictVersion(match.group(1)) <= StrictVersion("1.22.14") or (
        StrictVersion(match.group(1)) >= StrictVersion("1.24.0")
        and StrictVersion(match.group(1)) <= StrictVersion("1.24.2")
    )
