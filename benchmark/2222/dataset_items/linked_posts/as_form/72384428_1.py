const fd = new FormData()
fd.append('username', username)
fd.append('password', password)

axios.post(`/login`, fd)
