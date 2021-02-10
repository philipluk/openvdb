# -*- coding: utf-8 -*-

name = 'nanovdb'

version = '21.0.0-ta.1.0.0'

authors = [
    'sergen.eren'
]

requires = [
    'tbb-2019.U9',
    'openexr-2.4.0',
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-6']

variants = [
    # Windows
    ['platform-windows', 'arch-x64', 'os-windows-10', 'boost-1.65.1', 'openvdb-7.1.0-houdini'],
    # Linux
    ['platform-linux', 'arch-x86_64', 'os-centos-7', 'boost-1.65.1', 'openvdb-7.1.0-houdini'],
]


build_system = "cmake"


def commands():

     # Split and store version and package version
    split_versions = str(version).split('-')
    env.NANOVDB_VERSION.set(split_versions[0])
    env.NANOVDB_PACKAGE_VERSION.set(split_versions[1])

    env.NANOVDB_ROOT.set( "{root}" )
    env.NANOVDB_LIB_DIR.set( "{root}/lib" )
    env.NANOVDB_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/bin" )
