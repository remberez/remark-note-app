/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      container: {
        center: true,
        screens: {
          xl: "1200px",
          "2xl": "1200px",
        }
      },
      colors: {
        black: "#111114",
        grayText: "#B3B3B3",
      },
      fontFamily: {
        unbounded: ["Unbounded", "sans-serif"],
      }
    },
  },
  plugins: [],
}

