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

@app.route("/bbc1")
def savantBbc1():
    if auth.check(request.data):
        savantInterface.changeChannel('BBC1')
        return 'TV on Virgin and BBC1'
    else:
        return 'Not Auth'

@app.route("/itv1")
def savantItv1():
    if auth.check(request.data):
        savantInterface.changeChannel('ITV1')
        return 'TV on Virgin and ITV1'
    else:
        return 'Not Auth'

@app.route("/channelnumber/<channel>")
def savantChannelChange(channel):
    if auth.check(request.data):
        savantInterface.changeChannelNumeric(channel)
        return 'Channel changed to ' + channel
    else:
        return 'Not Auth'

if __name__ == "__main__":
    app.run()