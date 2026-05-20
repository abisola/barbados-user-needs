// Tailwind CDN config for alpha.gov.bb prototypes.
// Mirrors the published GovBB design tokens.
tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Figtree', '-apple-system', 'system-ui', 'Segoe UI', 'Roboto', 'sans-serif']
      },
      colors: {
        'bb-yellow-00': '#e8a833',
        'bb-yellow-100': '#ffc726',
        'bb-yellow-40': '#ffe9a8',
        'bb-yellow-10': '#fff9e9',
        'bb-blue-00': '#00164a',
        'bb-blue-100': '#00267f',
        'bb-blue-40': '#99a8cc',
        'bb-blue-10': '#e5e9f2',
        'bb-black-00': '#000',
        'bb-mid-grey-00': '#595959',
        'bb-grey-00': '#e0e4e9',
        'bb-grey-10': '#f4f6f8',
        'bb-white-00': '#fff',
        'bb-green-00': '#00654a',
        'bb-green-100': '#1fbf84',
        'bb-green-40': '#a5e5ce',
        'bb-green-10': '#e9f9f3',
        'bb-red-00': '#a42c2c',
        'bb-red-100': '#ff6b6b',
        'bb-red-40': '#ffc4c4',
        'bb-red-10': '#fff0f0',
        'bb-teal-00': '#0e5f64',
        'bb-teal-100': '#30c0c8',
        'bb-teal-40': '#ace6e9',
        'bb-teal-10': '#eaf9f9',
        'bb-purple-00': '#4a235a',
        'bb-purple-100': '#a962c7',
        'bb-pink-00': '#ad1157',
        'bb-pink-100': '#ff94d9'
      },
      spacing: {
        'xs': '0.5rem',
        's': '1rem',
        'xm': '1.5rem',
        'm': '2rem',
        'l': '4rem',
        'xl': '8rem'
      },
      boxShadow: {
        'form-hover': '0 0 0 2px #000'
      }
    }
  }
};
