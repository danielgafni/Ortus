import axios from 'axios'

// let VUE_APP_BASE = process.env.VUE_APP_BASE
// let VUE_APP_API_ENDPOINT = VUE_APP_BASE.concat(':5000/api')  // TODO: find a way to load the port from .env
// console.log(VUE_APP_API_ENDPOINT)

export default() => {
    return axios.create({
        // baseURL: VUE_APP_API_ENDPOINT,
        baseURL: env.process.BASE_URL.concat(":5000/api"),
        withCredentials: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            'Access-Control-Allow-Origin': '*'
        },
    })
}

axios.interceptors.request.use(request => {
  console.log('Starting Request', JSON.stringify(request, null, 2))
  return request
})
//
axios.interceptors.response.use(response => {
  console.log('Response:', JSON.stringify(response, null, 2))
  return response
})