import os, subprocess, sys
import shutil

# TODO: We should build glew properly, but ben skinner didn't have the time
# I'm terribly sorry...

if __name__ == "__main__":
    src = os.environ["HOUDINI_ROOT"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"]
    inc_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/include"
    lib_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/lib"

    
    if 'win' in str(sys.platform):

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)


        #os.mkdir(inc_dst + "/OpenImageIO")

        shutil.copytree(src + "/toolkit/include/openvdb", inc_dst + "/openvdb")
        
        os.mkdir(lib_dst)

        shutil.copy(src + '/custom/houdini/dsolib/openvdb_sesi.lib', lib_dst + "/openvdb.lib")

    else:

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)


        #os.mkdir(inc_dst + "/OpenImageIO")

        shutil.copytree(src + "/toolkit/include/openvdb", inc_dst + "/openvdb")
        
        os.mkdir(lib_dst)

        shutil.copy(src + '/dsolib/libopenvdb_sesi.so.7.1.0', lib_dst + "/libopenvdb.so")
