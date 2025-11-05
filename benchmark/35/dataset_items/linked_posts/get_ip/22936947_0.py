trusted_proxies = {'127.0.0.1'}  # define your own set
route = request.access_route + [request.remote_addr]

remote_addr = next((addr for addr in reversed(route) 
                    if addr not in trusted_proxies), request.remote_addr)
