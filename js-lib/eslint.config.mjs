import js from "@eslint/js";
import tseslint from "typescript-eslint";
import vuePrettier from "@vue/eslint-config-prettier";
import globals from "globals";

export default tseslint.config(
  { ignores: ["dist", "examples/**"] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  vuePrettier,
  {
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        ...globals.browser,
        ...globals.es2021,
      },
    },
    rules: {
      "no-unused-vars": "off",
      "@typescript-eslint/no-unused-vars": "error",
      "@typescript-eslint/no-explicit-any": "off",
    },
  },
);
