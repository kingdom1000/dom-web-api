from flask import Flask, request
import auth
import savantInterface


app = Flask(__name__)

# Run with no path for an ok running message
@app.route("/")
def serviceReady():
    return "OK"

@app.route("/test")
def test():
    print 'Receiving ...'
    if auth.check(request.data):
        print 'Auth ok'
    return 'Test Run'

@app.route("/tv-off")
def savantOff():
    if auth.check(request.data):
        savantInterface.off()
        return 'TV in the Living Room is off'
    else:
        return 'Not Auth'

@app.route("/chromecast-on")
def savantCCOn():
    if auth.check(request.data):
        savantInterface.chromecastOn()
        return 'TV on Chromecast'
    else:
        return 'Not Auth'

if __name__ == "__main__":
    app.run()