# WIP
Keeps track of your dead (offline) light bulbs and dim them as soon as they get back online.

Set your user id and bridge ip in `app.py` and set your `dim` level.

* Get your bridge IP: [https://www.meethue.com/api/nupnp](https://www.meethue.com/api/nupnp)
* Get your user ID: [https://developers.meethue.com/documentation/getting-started](https://developers.meethue.com/documentation/getting-started)

# run

```
while :;do python app.py;done
```

# TODO

* [ ] Get rid of this bash while loop
* [ ] get bridge ip automatically
* [ ] get user automatically by pressing the button
* [ ] fix everything
