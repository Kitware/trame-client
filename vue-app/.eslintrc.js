module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/essential', 'eslint:recommended', 'plugin:prettier/recommended'],
  parserOptions: {
    parser: '@babel/eslint-parser',
  },
  rules: {
    'vue/multi-word-component-names': 0,
    'no-console': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
};
