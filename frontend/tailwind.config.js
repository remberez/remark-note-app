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
        pageColor: "#1B1B1B",
        orange: "#955B53",
        ocean: "#ABBFFF",
        veryLightGray: "#434343",
        lightGray: "#292929",
        yellow: "#F5B400",
      },
      fontFamily: {
        unbounded: ["Unbounded", "sans-serif"],
      }
    },
  },
  plugins: [],
}

