# Ephemeral Tor hidden service test

Install flask and stem in a virtualenv.

```sh
$ virtualenv env
$ . env/bin/activate
(env) $ pip install flask stem
(env) $ python ephemeral-hs-test.py # to run
```

Open Tor Browser 5.5a2 (or any version that includes Tor version >= 0.2.7.1-alpha) and run `ephemeral-hs-test.py`. It will start a hidden service, then successfully connect to itself.
