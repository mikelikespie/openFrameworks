 {
    'targets': [
      {
        'target_name': 'of3d',
        'type': 'static_library',
        'dependencies': [
          'ofgl',
          'ofmath',
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/3d",
        ],
        'sources': [
          "libs/openFrameworks/3d/of3dPrimitives.cpp",
          "libs/openFrameworks/3d/of3dPrimitives.h",
          "libs/openFrameworks/3d/of3dUtils.cpp",
          "libs/openFrameworks/3d/of3dUtils.h",
          "libs/openFrameworks/3d/ofCamera.cpp",
          "libs/openFrameworks/3d/ofCamera.h",
          "libs/openFrameworks/3d/ofEasyCam.cpp",
          "libs/openFrameworks/3d/ofEasyCam.h",
          "libs/openFrameworks/3d/ofMesh.cpp",
          "libs/openFrameworks/3d/ofMesh.h",
          "libs/openFrameworks/3d/ofNode.cpp",
          "libs/openFrameworks/3d/ofNode.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofapp',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'link_settings': {
          'libraries': [ 
            'glfw',
          ],
        },
        'include_dirs': [
          "libs/openFrameworks/app",
          'libs/glfw/include',
        ],
        'all_dependent_settings': {
          'include_dirs':[
            'libs/tess2/include',
          ],
        },
        'sources': [
          "libs/openFrameworks/app/ofAppBaseWindow.h",
          "libs/openFrameworks/app/ofAppEGLWindow.cpp",
          "libs/openFrameworks/app/ofAppEGLWindow.h",
          "libs/openFrameworks/app/ofAppGLFWWindow.cpp",
          "libs/openFrameworks/app/ofAppGLFWWindow.h",
          "libs/openFrameworks/app/ofAppGlutWindow.cpp",
          "libs/openFrameworks/app/ofAppGlutWindow.h",
          "libs/openFrameworks/app/ofAppNoWindow.cpp",
          "libs/openFrameworks/app/ofAppNoWindow.h",
          "libs/openFrameworks/app/ofAppRunner.cpp",
          "libs/openFrameworks/app/ofAppRunner.h",
          "libs/openFrameworks/app/ofBaseApp.h",
          "libs/openFrameworks/app/ofIcon.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofcommunication',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/communication",
        ],
        'sources': [
          "libs/openFrameworks/communication/ofArduino.cpp",
          "libs/openFrameworks/communication/ofArduino.h",
          "libs/openFrameworks/communication/ofSerial.cpp",
          "libs/openFrameworks/communication/ofSerial.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofevents',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/events",
        ],
        'sources': [
          "libs/openFrameworks/events/ofDelegate.h",
          "libs/openFrameworks/events/ofEvents.cpp",
          "libs/openFrameworks/events/ofEvents.h",
          "libs/openFrameworks/events/ofEventUtils.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofgl',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/gl",
        ],
        'sources': [
          "libs/openFrameworks/gl/ofFbo.cpp",
          "libs/openFrameworks/gl/ofFbo.h",
          "libs/openFrameworks/gl/ofGLProgrammableRenderer.cpp",
          "libs/openFrameworks/gl/ofGLProgrammableRenderer.h",
          "libs/openFrameworks/gl/ofGLRenderer.cpp",
          "libs/openFrameworks/gl/ofGLRenderer.h",
          "libs/openFrameworks/gl/ofGLUtils.cpp",
          "libs/openFrameworks/gl/ofGLUtils.h",
          "libs/openFrameworks/gl/ofLight.cpp",
          "libs/openFrameworks/gl/ofLight.h",
          "libs/openFrameworks/gl/ofMaterial.cpp",
          "libs/openFrameworks/gl/ofMaterial.h",
          "libs/openFrameworks/gl/ofShader.cpp",
          "libs/openFrameworks/gl/ofShader.h",
          "libs/openFrameworks/gl/ofTexture.cpp",
          "libs/openFrameworks/gl/ofTexture.h",
          "libs/openFrameworks/gl/ofVbo.cpp",
          "libs/openFrameworks/gl/ofVbo.h",
          "libs/openFrameworks/gl/ofVboMesh.cpp",
          "libs/openFrameworks/gl/ofVboMesh.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofgraphics',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/graphics",
        ],
        'sources': [
          "libs/openFrameworks/graphics/of3dGraphics.cpp",
          "libs/openFrameworks/graphics/of3dGraphics.h",
          "libs/openFrameworks/graphics/ofBitmapFont.cpp",
          "libs/openFrameworks/graphics/ofBitmapFont.h",
          "libs/openFrameworks/graphics/ofCairoRenderer.cpp",
          "libs/openFrameworks/graphics/ofCairoRenderer.h",
          "libs/openFrameworks/graphics/ofGraphics.cpp",
          "libs/openFrameworks/graphics/ofGraphics.h",
          "libs/openFrameworks/graphics/ofImage.cpp",
          "libs/openFrameworks/graphics/ofImage.h",
          "libs/openFrameworks/graphics/ofPath.cpp",
          "libs/openFrameworks/graphics/ofPath.h",
          "libs/openFrameworks/graphics/ofPixels.cpp",
          "libs/openFrameworks/graphics/ofPixels.h",
          "libs/openFrameworks/graphics/ofPolyline.cpp",
          "libs/openFrameworks/graphics/ofPolyline.h",
          "libs/openFrameworks/graphics/ofRendererCollection.cpp",
          "libs/openFrameworks/graphics/ofRendererCollection.h",
          "libs/openFrameworks/graphics/ofTessellator.cpp",
          "libs/openFrameworks/graphics/ofTessellator.h",
          "libs/openFrameworks/graphics/ofTrueTypeFont.cpp",
          "libs/openFrameworks/graphics/ofTrueTypeFont.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofmath',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/math",
        ],
        'sources': [
          "libs/openFrameworks/math/ofMath.cpp",
          "libs/openFrameworks/math/ofMath.h",
          "libs/openFrameworks/math/ofMatrix3x3.cpp",
          "libs/openFrameworks/math/ofMatrix3x3.h",
          "libs/openFrameworks/math/ofMatrix4x4.cpp",
          "libs/openFrameworks/math/ofMatrix4x4.h",
          "libs/openFrameworks/math/ofQuaternion.cpp",
          "libs/openFrameworks/math/ofQuaternion.h",
          "libs/openFrameworks/math/ofVec2f.cpp",
          "libs/openFrameworks/math/ofVec2f.h",
          "libs/openFrameworks/math/ofVec3f.h",
          "libs/openFrameworks/math/ofVec4f.cpp",
          "libs/openFrameworks/math/ofVec4f.h",
          "libs/openFrameworks/math/ofVectorMath.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofsound',
        'type': 'static_library',
        'dependencies': [
          'ofutils',
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/sound",
        ],
        'sources': [
          "libs/openFrameworks/sound/ofBaseSoundPlayer.h",
          "libs/openFrameworks/sound/ofBaseSoundStream.h",
          "libs/openFrameworks/sound/ofFmodSoundPlayer.cpp",
          "libs/openFrameworks/sound/ofFmodSoundPlayer.h",
          "libs/openFrameworks/sound/ofOpenALSoundPlayer.cpp",
          "libs/openFrameworks/sound/ofOpenALSoundPlayer.h",
          "libs/openFrameworks/sound/ofRtAudioSoundStream.cpp",
          "libs/openFrameworks/sound/ofRtAudioSoundStream.h",
          "libs/openFrameworks/sound/ofSoundPlayer.cpp",
          "libs/openFrameworks/sound/ofSoundPlayer.h",
          "libs/openFrameworks/sound/ofSoundStream.cpp",
          "libs/openFrameworks/sound/ofSoundStream.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'oftype',
        'type': 'static_library',
        'dependencies': [
        ],
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/types",
        ],
        'sources': [
          "libs/openFrameworks/types/ofBaseTypes.cpp",
          "libs/openFrameworks/types/ofBaseTypes.h",
          "libs/openFrameworks/types/ofColor.cpp",
          "libs/openFrameworks/types/ofColor.h",
          "libs/openFrameworks/types/ofParameter.cpp",
          "libs/openFrameworks/types/ofParameter.h",
          "libs/openFrameworks/types/ofParameterGroup.cpp",
          "libs/openFrameworks/types/ofParameterGroup.h",
          "libs/openFrameworks/types/ofPoint.h",
          "libs/openFrameworks/types/ofRectangle.cpp",
          "libs/openFrameworks/types/ofRectangle.h",
          "libs/openFrameworks/types/ofTypes.h",
        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
        ],
      },
      {
        'target_name': 'ofutils',
        'type': 'static_library',
        'defines': [
        ],
        'include_dirs': [
          "libs/openFrameworks/utils",
          "libs/tess2/include",
          "libs/poco/include",
        ],
        'all_dependent_settings': {
          'include_dirs':[
            'libs/tess2/include',
            "libs/poco/include",
          ],
        },
        'link_settings': {
          'libraries': [
            'glew',
            'poco',
            'tess2',
            'cairo',
          ],
        },
        'sources': [
          "libs/openFrameworks/utils/ofConstants.h",
          "libs/openFrameworks/utils/ofFileUtils.cpp",
          "libs/openFrameworks/utils/ofFileUtils.h",
          "libs/openFrameworks/utils/ofLog.cpp",
          "libs/openFrameworks/utils/ofLog.h",
          "libs/openFrameworks/utils/ofMatrixStack.cpp",
          "libs/openFrameworks/utils/ofMatrixStack.h",
          "libs/openFrameworks/utils/ofNoise.h",
          "libs/openFrameworks/utils/ofSystemUtils.cpp",
          "libs/openFrameworks/utils/ofSystemUtils.h",
          "libs/openFrameworks/utils/ofThread.cpp",
          "libs/openFrameworks/utils/ofThread.h",
          "libs/openFrameworks/utils/ofURLFileLoader.cpp",
          "libs/openFrameworks/utils/ofURLFileLoader.h",
          "libs/openFrameworks/utils/ofUtils.cpp",
          "libs/openFrameworks/utils/ofUtils.h",
          "libs/openFrameworks/utils/ofXml.cpp",
          "libs/openFrameworks/utils/ofXml.h",

        ],
        'conditions': [
          ['OS=="mac"', {
            'include_dirs': [
              'libs/glew/include',
            ],

            'all_dependent_settings': {
              'include_dirs':[
                'libs/glew/include',
              ],
            },

            'cflags': [
              '-x',
              'objective-c++',
            ],
            'xcode_settings': {
              'GCC_INPUT_FILETYPE': 'sourcecode.cpp.objcpp',
            },

            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
            ],
            
          }
        ],
      ]
    },
    {
      'target_name': 'ofvideo',
      'type': 'static_library',
      'dependencies': [
      ],
      'defines': [
      ],
      'include_dirs': [
        "libs/openFrameworks/video",
      ],
      'sources': [
        "libs/openFrameworks/video/ofDirectShowGrabber.cpp",
        "libs/openFrameworks/video/ofDirectShowGrabber.h",
        "libs/openFrameworks/video/ofGstUtils.cpp",
        "libs/openFrameworks/video/ofGstUtils.h",
        "libs/openFrameworks/video/ofGstVideoGrabber.cpp",
        "libs/openFrameworks/video/ofGstVideoGrabber.h",
        "libs/openFrameworks/video/ofGstVideoPlayer.cpp",
        "libs/openFrameworks/video/ofGstVideoPlayer.h",
        "libs/openFrameworks/video/ofQTKitGrabber.h",
        "libs/openFrameworks/video/ofQTKitMovieRenderer.h",
        "libs/openFrameworks/video/ofQTKitPlayer.h",
        "libs/openFrameworks/video/ofQtUtils.cpp",
        "libs/openFrameworks/video/ofQtUtils.h",
        "libs/openFrameworks/video/ofQuickTimeGrabber.cpp",
        "libs/openFrameworks/video/ofQuickTimeGrabber.h",
        "libs/openFrameworks/video/ofQuickTimePlayer.cpp",
        "libs/openFrameworks/video/ofQuickTimePlayer.h",
        "libs/openFrameworks/video/ofVideoGrabber.cpp",
        "libs/openFrameworks/video/ofVideoGrabber.h",
        "libs/openFrameworks/video/ofVideoPlayer.cpp",
        "libs/openFrameworks/video/ofVideoPlayer.h",

      ],
      'conditions': [
        ['OS=="mac"', {
            'include_dirs': [
            ],
          }],
      ],
    },
  ],
}
