var tailwindcss = require('tailwindcss');

module.exports = {
  plugins: [
    // ...
    require('postcss-import'),
    require('postcss-url')({
      url: 'copy',
      useHash: true, // Optional: Add a hash to the font filename for cache busting
    }),
    tailwindcss('./tailwind.js'),
    require('autoprefixer')(),
    // ...
  ],
}