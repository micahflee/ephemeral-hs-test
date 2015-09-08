# Ephemeral Tor hidden service test

Install flask and stem in a virtualenv.

```sh
$ virtualenv env
$ . env/bin/activate
(env) $ pip install flask stem
(env) $ python ephemeral-hs-test.py # to run
```

Open Tor Browser 5.5a2 (or any version that includes Tor version >= 0.2.7.1-alpha) and run `ephemeral-hs-test.py`.

*Expected behavior:*

The script should start a simple web server, start a hidden service, and then eventually connect to itself.

*Actual behavior:*

```
$ python2 ephemeral-hs-test.py                              1 ↵
Starting web app
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
lsd6hxung26xoapz.onion
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
Attempting to connect to lsd6hxung26xoapz.onion
Not ready yet, waiting...
```

(It never successfully connects to itself.)
