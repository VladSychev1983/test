//import globals from "globals";
import pluginJs from "@eslint/js";
import pluginJest from 'eslint-plugin-jest';

/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files: ['**/*.spec.js', '**/*.test.js', '**/*.js'],
    plugins: { jest: pluginJest },
    languageOptions: { 
        //globals: globals.browser,
        globals: pluginJest.environments.globals.globals,
        },
        rules: {
            semi: ["warn", "always"],
            'no-console': 'off',
            "no-unused-vars": "warn",
            "no-undef": "warn",
            'func-call-spacing': 'off',
            'comma-spacing': 'error',
            'no-spaced-func': 'off',
            "indent": ["error", 4],
            'max-len': ['error', { code: 70 }],
            'jest/no-disabled-tests': 'warn',
            'jest/no-focused-tests': 'error',
            'jest/no-identical-title': 'error',
            'jest/prefer-to-have-length': 'warn',
            'jest/valid-expect': 'error',
          },
          //ignores: ["*.mjs", "config/*"],
    },
  pluginJs.configs.recommended,
];