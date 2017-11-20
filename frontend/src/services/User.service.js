import axios from 'axios'

export default class UserService {

  static async login(userObject, apiURL) {
    let header =  {
        'Content-Type': 'application/json'
    }

    return axios.post(apiURL, userObject, {
            headers: header
        })
        .then(response => {
            return response.data
        })
  }

  static async logout(apiURL, token) {
    let header = {
        'Authorization': 'Token ' + token
    }
    
    return axios.get(apiURL, {
            headers: header
        })
        .then(response => {
            return response.data
        })
  }
}
