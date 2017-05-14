{
	'target_defaults': {
		'default_configuration': 'Release',
		'configurations': {
			'Release': {
				'xcode_settings': {
					'GCC_OPTIMIZATION_LEVEL': '3',
					'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'OTHER_CPLUSPLUSFLAGS': [ '-std=c++14' ],
				},
				'msvs_settings': {
					'VCCLCompilerTool': {
						'Optimization': 3,
						'FavorSizeOrSpeed': 1,
					},
				},
			},
			'Debug': {
				'xcode_settings': {
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'OTHER_CPLUSPLUSFLAGS': [ '-std=c++14' ],
				},
			},
		},
	},
	'targets': [
		{
			'target_name': 'isolated_vm',
			'cflags_cc': [ '-std=c++14' ],
			'cflags!': [ '-fno-exceptions' ],
			'cflags_cc!': [ '-fno-exceptions' ],
			'sources': [
				'src/external_copy.cc',
				'src/isolate.cc',
				'src/script_handle.cc',
				'src/shareable_isolate.cc',
				'src/transferable.cc',
			],
		},
	],
}