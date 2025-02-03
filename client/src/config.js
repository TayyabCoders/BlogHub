const config = {
    BASE_URL: import.meta.env.VITE_API_URL || "http://default-api-url.com",  // Provide a fallback URL in case the env variable is missing
  };
  
export default config;