import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'



// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    watch: {
      // Watcher options
    },
    proxy: {
      '/api': {
        target: 'http://backend-dev:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  // Github pages live demo configuration
  publicPath: process.env.NODE_ENV === "production" ? "/Rosla-Technology-Webapp" : "/",
  base: "/Rosla-Technology-Webapp/",
})
