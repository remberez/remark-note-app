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
        },
        padding: "10px",
      },
      colors: {
        black: "#111114",
        grayText: "#B3B3B3",
        green: "#499F8E",
      },
      fontFamily: {
        unbounded: ["Unbounded", "sans-serif"],
      }
    },
  },
  plugins: [],
}

