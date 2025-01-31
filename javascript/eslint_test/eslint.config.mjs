import js from "@eslint/js";
import globals from "globals";

export default [
    js.configs.recommended,
    {
        files: ["**/*.js"],
        languageOptions: {
          globals: {
            ...globals.browser,
            ...globals.node,
            myCustomGlobal: "readonly"
          },
        },
        rules: {
            semi: ["warn", "always"],
            'no-console': 'off',
            "no-unused-vars": "warn",
            "no-undef": "warn",
            'func-call-spacing': 'off',
            'comma-spacing': 'error',
            'no-spaced-func': 'off',
            'max-len': ['error', { code: 70 }],
        }
    }
];