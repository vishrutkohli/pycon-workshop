import wsgiref.simple_server

def application(env,start_response):
    response = b"Basic web server running flwalessly"
    status = "200 OK"
    headers = [("Content-Type", "text/html")]

    start_response(status, headers)
    

    return [response]

if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )
    w_s.serve_forever()