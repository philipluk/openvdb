# -*- coding: utf-8 -*-

name = 'openvdb'

version = '7.0.0-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

requires = [
    'openexr-2.4.0',
    'tbb-2019',
    'blosc-1.5',
    'boost-1.69.0',
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x64'],
]

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.OPENVDB_VERSION.set(split_versions[0])
    env.OPENVDB_PACKAGE_VERSION.set(split_versions[1])

    env.OPENVDB_ROOT.set("{root}")
    env.OPENVDB_ROOT_DIR.set("{root}")
    env.OPENVDB_INCLUDE_DIR.set("{root}/include")
    env.OPENVDB_LIBRARY_DIR.set("{root}/lib")
    env.OPENVDB_BINARY_DIR.set("{root}/bin")

    env.PATH.append( str(env.OPENVDB_BINARY_DIR) )
