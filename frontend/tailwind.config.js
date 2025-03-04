/** @type {import('tailwindcss').Config} */

export default {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkBlue: "#332f42"
      },
      fontFamily: {
        heebo: ['Heebo', 'sans-serif'],
        robotoCondensed: ['Roboto Condensed', 'sans-serif'],
        rubik: ['Rubik', 'sans-serif'],
        yantramanav: ['Yantramanav', 'sans-serif'],
      },
    },
    container: {
      center: true,
    }
  },
  plugins: [],
}

