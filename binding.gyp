{
    "targets": [ {
        "target_name": "grandiose",
        "sources": [
            "src/grandiose_util.cc",
            "src/grandiose_find.cc",
            "src/grandiose_send.cc",
            "src/grandiose_receive.cc",
            "src/grandiose_routing.cc",
            "src/grandiose.cc"
        ],
        "include_dirs": [ "include", "<!(node -p \"require('node-addon-api').include_dir\")" ],
        "defines": [
          "NAPI_DISABLE_CPP_EXCEPTIONS",
          "NODE_ADDON_API_ENABLE_MAYBE"
        ],
        "conditions":[
            [ "OS == 'win' and target_arch == 'ia32'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "lib/win-x86/Processing.NDI.Lib.x86.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x86.lib" ],
                    "library_dirs": [ "lib/win-x86" ]
                }
            } ],
            [ "OS == 'win' and target_arch == 'x64'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "lib/win-x64/Processing.NDI.Lib.x64.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x64.lib" ],
                    "library_dirs": [ "lib/win-x64" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'ia32'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "lib/lnx-x86/libndi.so",
                                      "lib/lnx-x86/libndi.so.5",
                                      "lib/lnx-x86/libndi.so.5.1.1" ]
                } ],
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,'$$ORIGIN'", "-lndi" ],
                    "library_dirs": [ "lib/lnx-x86" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'x64'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "lib/lnx-x64/libndi.so",
                                      "lib/lnx-x64/libndi.so.5",
                                      "lib/lnx-x64/libndi.so.5.1.1" ]
                } ],
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,'$$ORIGIN'", "-lndi" ],
                    "library_dirs": [ "lib/lnx-x64" ]
                }
            } ],
            ["OS=='mac'", {
              "cflags+": ["-fvisibility=hidden"],
              "xcode_settings": {
                  "GCC_SYMBOLS_PRIVATE_EXTERN": "YES", # -fvisibility=hidden
                  "OTHER_CPLUSPLUSFLAGS": [
                  "-std=c++14",
                  "-stdlib=libc++",
                  "-fexceptions"
                  ],
                  "OTHER_LDFLAGS": [
                  "-Wl,-rpath,@loader_path/../../lib/mac_universal"
                  ]
              },
              "link_settings": {
                  "libraries": [
                  "<(module_root_dir)/lib/mac_universal/libndi.dylib"
                  ],
              }
            }]
        ]
    } ]
}
