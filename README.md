# request402

Request the IP address, Headers, and Status Code of any website.

<h3> Basic Requirements </h3>

1. A  <a href="https://21.co">21 Bitcoin Computer</a> or 21 installed.
2. You will need to be connected the 21 Zerotier Marketplace.

How to use:

    $ 21 buy http://10.244.107.98:3002/get_status/www.example.com -> Status and headers
    $ 21 buy http://10.244.107.98:3002/get_ip/www.example.com --> IP Address


<p>Here is an example of the JSON response when running /get_status/ for Google.</p>
<pre><code> {
    "200": "OK",
    "headers": [
        [
            "Date",
            "Mon, 22 Aug 2016 17:29:27 GMT"
        ],
        [
            "Expires",
            "-1"
        ],
        [
            "Cache-Control",
            "private, max-age=0"
        ],
        [
            "Content-Type",
            "text/html; charset=ISO-8859-1"
        ],
        [
            "P3P",
            "CP=\"This is not a P3P policy! See https://www.google.com/support/accounts/answer/151657?hl=en for more info.\""
        ],
        [
            "Server",
            "gws"
        ],
        [
            "X-XSS-Protection",
            "1; mode=block"
        ],
        [
            "X-Frame-Options",
            "SAMEORIGIN"
        ]
    ]
}

</code></pre>
<p>This is an example of runnng /get_ip/ for Google.</p>
<pre><code> {
    "ip_address": "216.58.219.164",
    "url": "www.google.com"
}
</code></pre>
