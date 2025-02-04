import axios from "axios"
import { jwtDecode } from "jwt-decode"



// export const BASE_URL = "http://127.0.0.1:8001"  
export const BASE_URL = "http://ec2-51-20-55-119.eu-north-1.compute.amazonaws.com:8001"
// export const BASE_URL = config.BASE_URL;

const api = axios.create({
    baseURL: BASE_URL
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("access")
        if(token){
            const decoded = jwtDecode(token)
            const expiry_date = decoded.exp
            const current_time = Date.now() / 1000
            if(expiry_date > current_time){
                config.headers.Authorization = `Bearer ${token}`
            }
            
        }
        return config;
    },

    (error) => {
        return Promise.reject(error)
    }

)






export default api