Title: How to share your local server with anyone using Ngrok
Date: 2022-09-01
Category: General
Summary: Getting a secure, private public url for our local server 
opengraph_image: ngrok_og.jpg


- There will be instances where we want to share our dev web app with friends before deploying it somewhere, or even check its UI on your mobile, or we may need to test webhooks. A common constraint in these situations is that your development web app is on your local machine. 
- A free tool called Ngrok is available to handle this.
- Ngrok creates a secure, private connection tunnel to the cloud service. Your local server is mapped to a ngrok.io sub-domain, which can be used by a remote user to access your local server.

###### How to use NGROK:

To demo this, I will run a simple HTML file on my localhost. You can extend its usability to other areas as I mentioned above.

1. Create a new HTML file, hello.html in any local folder

    ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h3>Hello World</h3>
        </body>
        </html>
    ```

2. Assuming you have python installed on your machine, you can run this HTML on the local server using the below command in your command prompt
    `python -m http.server` 
3. You can see the results at http://127.0.0.1:8000/hello.html using a browser. (default port will be 8000)
4. We can now use "Ngrok" to share this with our friends.
5. Download its package from Ngrok's official [website](https://ngrok.com/download)
6. Unzip the downloaded file to your local storage.
7. Open Command prompt, cd to the folder containing the ngrok file, and run the below command
8. `ngrok http 8000`, will provide you with a public URL that serves the same hello.html file
        ![ngrok_demo]({static}images/ngrok_demo.png)
