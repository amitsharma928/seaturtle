{
  'variables': {
    'chromium_code': 1,
    'seaturtle_debug_build%': 0,
  },
  'includes': [
  ],
  'targets': [
    {
      'target_name': 'seaturtle_protos',
      'type': 'static_library',
      'sources': [
        'protos/jni.proto',
        'protos/blocking.proto',
        'protos/setting.proto',
        'protos/https.proto',
      ],
      'variables': {
        'proto_in_dir': './protos',
        'proto_out_dir': 'seaturtle/protos',
      },
      'includes': [
        '../build/protoc.gypi',
      ],
    },
    {
      'target_name': 'libseaturtle',
      'type': 'shared_library',
      'dependencies': [
        'seaturtle_protos',
        # BEGIN REPLACEMENT FOR CONTENT_SHELL_LIB

        '../content/app/strings/content_strings.gyp:content_strings',
        '../content/content.gyp:content_app_both',
        '../content/content.gyp:content_browser',
        '../content/content.gyp:content_common',
        '../content/content.gyp:content_gpu',
        #'content.gyp:content_plugin',
        #'content.gyp:content_ppapi_plugin',
        '../content/content.gyp:content_renderer',
        #'../content/content.gyp:content_utility',
        '../content/content_resources.gyp:content_resources',
        #'content_shell_resources',
        #'copy_test_netscape_plugin',
        #'layouttest_support_content',
        '../base/base.gyp:base',
        '../base/base.gyp:base_static',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../cc/cc.gyp:cc',
        #'../components/components.gyp:breakpad_component',
        '../gin/gin.gyp:gin',
        '../gpu/gpu.gyp:gpu',
        '../ipc/ipc.gyp:ipc',
        '../media/media.gyp:media',
        '../net/net.gyp:net',
        '../net/net.gyp:net_resources',
        '../skia/skia.gyp:skia',
        '../third_party/WebKit/public/blink.gyp:blink',
        #'../third_party/WebKit/public/blink.gyp:blink_test_support',
        '../ui/base/ui_base.gyp:ui_base',
        '../ui/events/events.gyp:events_base',
        '../ui/gfx/gfx.gyp:gfx',
        '../ui/gfx/gfx.gyp:gfx_geometry',
        '../ui/gfx/ipc/gfx_ipc.gyp:gfx_ipc',
        '../ui/gl/gl.gyp:gl',
        '../url/url.gyp:url_lib',
        '../v8/tools/gyp/v8.gyp:v8',
        '../webkit/storage_browser.gyp:webkit_storage_browser',
        '../webkit/glue/resources/webkit_resources.gyp:webkit_resources',

        # OLD 
#          '../content/content.gyp:content_app_both',
#          '../content/content.gyp:content_browser',
#          '../content/content.gyp:content_common',
#          '../content/content.gyp:content_gpu',
#          # '../content/content.gyp:content_plugin',
#          # '../content/content.gyp:content_ppapi_plugin',
#          '../content/content.gyp:content_renderer',
#          '../content/content.gyp:content_utility',
#          '../content/content.gyp:content_worker',
#          '../content/content_resources.gyp:content_resources',
#          #'../content/content_shell_and_tests.gyp:content_shell_resources',
#          # 'copy_test_netscape_plugin',
#          #'test_support_content',
#          '../base/base.gyp:base',
#          '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
#          #'../components/components.gyp:breakpad_component',
#          '../gin/gin.gyp:gin',
#          '../ipc/ipc.gyp:ipc',
#          '../media/media.gyp:media',
#          '../net/net.gyp:net',
#          '../net/net.gyp:net_resources',
#          '../skia/skia.gyp:skia',
#          '../third_party/WebKit/public/blink.gyp:blink',
#          # '../third_party/WebKit/public/blink.gyp:blink_web_test_support',
#          '../ui/base/ui_base.gyp:ui_base',
#          '../ui/events/events.gyp:events_base',
#          '../ui/gfx/gfx.gyp:gfx',
#          '../ui/gfx/gfx.gyp:gfx_geometry',
#          '../ui/gl/gl.gyp:gl',
#          '../url/url.gyp:url_lib',
#          '../v8/tools/gyp/v8.gyp:v8',
#          '../webkit/common/webkit_common.gyp:webkit_common',
#          '../webkit/webkit_resources.gyp:webkit_resources',
#        # END REPLACEMENT FOR CONTENT_SHELL_LIB
#
#          # ABANDON for the hax below:
#          # ABANDON this is borring ssl in teh latest build.
#          #'../third_party/openssl/openssl.gyp:openssl',

          # For rewrites
          '../third_party/re2/re2.gyp:re2',
      ],
      'sources': [
        # ABANDON hacky:
        #'../net/cert/cert_verify_proc_openssl.h',
        #'../net/cert/cert_verify_proc_openssl.cc',

        'extra/shell_descriptors.h',
        'app/android/library_loader_hooks.h',
        'app/android/library_loader_hooks.cc',
        'block/blocker.h',
        'block/blocker.cc',
        'shell/common/shell_content_client.h',
        'shell/common/shell_content_client.cc',
        'shell/browser/shell.h',
        'shell/browser/shell.cc',
        'shell/browser/shell_javascript_dialog_manager.h',
        'shell/browser/shell_javascript_dialog_manager.cc',
        'shell/browser/shell_login_dialog.h',
        'shell/browser/shell_login_dialog.cc',
        'shell/browser/shell_browser_main_parts.h',
        'shell/browser/shell_browser_main_parts.cc',
        'shell/browser/shell_url_request_context_getter.h',
        'shell/browser/shell_url_request_context_getter.cc',
        'shell/browser/shell_quota_permission_context.h',
        'shell/browser/shell_quota_permission_context.cc',
        'shell/browser/shell_browser_context.h',
        'shell/browser/shell_browser_context.cc',
        'shell/browser/shell_network_delegate.h',
        'shell/browser/shell_network_delegate.cc',
        'shell/browser/shell_download_manager_delegate.h',
        'shell/browser/shell_download_manager_delegate.cc',
        'shell/browser/shell_resource_dispatcher_host_delegate.h',
        'shell/browser/shell_resource_dispatcher_host_delegate.cc',
        'shell/browser/shell_web_contents_view_delegate.h',
        'shell/browser/shell_web_contents_view_delegate.cc',
        'shell/renderer/shell_render_frame_observer.h',
        'shell/renderer/shell_render_frame_observer.cc',
        # 'shell/renderer/shell_render_process_observer.h',
        # 'shell/renderer/shell_render_process_observer.cc',
        'shell/renderer/shell_content_renderer_client.h',
        'shell/renderer/shell_content_renderer_client.cc',
        'shell/browser/shell_content_browser_client.h',
        'shell/browser/shell_content_browser_client.cc',
        'shell/app/shell_main_delegate.h',
        'shell/app/shell_main_delegate.cc',
        'shell/renderer/shell_render_view_observer.h',
        'shell/renderer/shell_render_view_observer.cc',
        'extra/base.h',
        'extra/https_rewriter.h',
        'extra/https_rewriter.cc',
        'extra/constants.h',
        'extra/constants.cc',
        'extra/net_log.h',
        'extra/net_log.cc',
        'extra/settings.h',
        'extra/settings.cc',
        'extra/process_cache.h',
        'extra/process_cache.cc',
        'extra/gfx_util.h',
        'extra/gfx_util.cc',
        'extra/file_util.h',
        'extra/file_util.cc',
        'extra/fetch.h',
        'extra/fetch.cc',
        'extra/shell_messages.h',
        'extra/shell_messages.cc',
        'extra/proxy_config_service.h',
        'extra/proxy_config_service.cc',
        'extra/split_cookie_store.h',
        'extra/split_cookie_store.cc',
        'extra/cookie_access_policy.h',
        'extra/cookie_access_policy.cc',
        'extra/ssl_config_service.h',
        'extra/ssl_config_service.cc',
        'extra/seaturtle_protocol_handler.h',
        'extra/seaturtle_protocol_handler.cc',
        'jni/jni_bridge.h',
        'jni/jni_bridge.cc',
        'shell/android/shell_library_loader.cc',
      ],
      'conditions': [
        ['seaturtle_debug_build==1', {
          'defines': [
            'SEATURTLE_DEBUG_BUILD',
          ],
          'cflags': [
            # Allow C++11 extensions (for "override")
            '-std=c++11',
          ],
        }],
      ],
    },
    {
      'target_name': 'seaturtlegyp_apk',
      'type': 'none',
      'dependencies': [
        #'../content/content.gyp:content_icudata',
        '../content/content.gyp:content_java',
        #'../content/content_shell_and_tests.gyp:content_java_test_support',
        '../content/content_shell_and_tests.gyp:content_shell_java',
        'libseaturtle',
        '../base/base.gyp:base_java',
        '../media/media.gyp:media_java',
        '../net/net.gyp:net_java',
        #'../third_party/mesa/mesa.gyp:osmesa_in_lib_dir',
        '../tools/android/forwarder/forwarder.gyp:forwarder',
        '../ui/android/ui_android.gyp:ui_java',
      ],
      'variables': {
        'apk_name': 'SeaTurtleGyp',
        'manifest_package_name': 'org.chromium.sea_turtle_gyp_apk',
        'java_in_dir': '../content/shell/android/shell_apk',
        'resource_dir': '../content/shell/android/shell_apk/res',
        'native_lib_target': 'libseaturtle',
        'additional_input_paths': ['<(PRODUCT_DIR)/content_shell/assets/content_shell.pak'],
        'asset_location': '<(PRODUCT_DIR)/content_shell/assets',
        #'extra_native_libs': ['<(SHARED_LIB_DIR)/libosmesa.so'],
        'conditions': [
          ['icu_use_data_file_flag==1', {
            'additional_input_paths': [
              '<(PRODUCT_DIR)/icudtl.dat',
            ],
          }],
        ],
      },
      'conditions': [
        ['android_webview_build==0', {
          'dependencies': [
            '../tools/imagediff/image_diff.gyp:image_diff#host',
          ],
        }],
      ],
      'includes': [ '../build/java_apk.gypi' ],
    },
  ],
}