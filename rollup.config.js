import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import sveltePreprocess from 'svelte-preprocess';
import postcss from 'rollup-plugin-postcss';
import {config} from 'dotenv';
import replace from '@rollup/plugin-replace';
import css from 'rollup-plugin-css-only';

const production = !process.env.ROLLUP_WATCH;

const extensions = [".js", ".ts"];

function serve() {
	let server;
	
	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

const postcssOptions = () =>({
	extensions: ['.scss', '.sass'],
  extract: false,
  minimize: true,
  use: [
    ['sass', {
      includePaths: [
        './src/theme',
        './node_modules',
      ]
    }]
	]
});

export default {
	input: 'src/main.ts',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'ThingsWeOwn',
		file: 'public/build/bundle.js'
	},
	plugins: [
		svelte({
						emitCss:true,
						preprocess: sveltePreprocess({
							scss: {
								prependData: `@import 'src/theme/smui-theme.scss';`
						},
					}),
		}),
		css({output:'bundle.css'}),
		replace({
      // stringify the object
			preventAssignment:true,       
      appenv: JSON.stringify({
        env: {
          isProd: production,
          ...config().parsed // attached the .env config
        }
      }),
    }),
		resolve({
			browser: true,
			dedupe: ['svelte'],
			extensions,
		}),
		commonjs(),
		postcss(postcssOptions()),

		// In dev mode, call `npm run start` once
		// the bundle has been generated
		!production && serve(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload('public'),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser()
	],
	watch: {
		clearScreen: false
	},
};
