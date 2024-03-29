##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Cart(SConsPackage):
    """Collective and RPC Transport (CaRT)"""

    homepage = 'https://github.com/daos-stack/cart'
    git      = 'https://github.com/daos-stack/cart.git'

    version('master', branch='master', submodules=True)
    version('daos-devel', branch='daos_devel1', submodules=True)
    version('daos-0.6', commit='7bde2eaec684faa02372caca464b96136348aad4', submodules=True)
    version('daos-0.5', commit='ad94f7f36c4e8398d14576d393dfe66b3ea4713a', submodules=True)
    version('daos-0.4', commit='24c97eab7b97df49e8e26a4618157a806e92cbad', submodules=True)

    depends_on('boost', type='build')
    depends_on('cmocka', type='build')
    depends_on('mercury+boostsys')
    depends_on('openmpi+pmix')
    depends_on('openssl')
    depends_on('libuuid')
    depends_on('libyaml')

    patch('cart_include.patch')
    patch('werror.patch')

    def build_args(self, spec, prefix):
        args = [
            'PREFIX={0}'.format(prefix),
            'BOOST_PREBUILT={0}'.format(spec['boost'].prefix),
            'CMOCKA_PREBUILT={0}'.format(spec['cmocka'].prefix),
            'CRYPTO_PREBUILT={0}'.format(spec['openssl'].prefix),
            'MERCURY_PREBUILT={0}'.format(spec['mercury'].prefix),
            'OMPI_PREBUILT={0}'.format(spec['openmpi'].prefix),
            'PMIX_PREBUILT={0}'.format(spec['pmix'].prefix),
            'UUID_PREBUILT={0}'.format(spec['libuuid'].prefix),
        ]

        return args 
