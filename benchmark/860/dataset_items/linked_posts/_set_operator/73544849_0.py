 spec:
   containers:
    - name: webserver1
     image: nginx:1.6
     ports:
       - containerPort:80 // "- containerPort: 80" fixed it
