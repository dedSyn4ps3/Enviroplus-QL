import strawberry

#from bme280 import BME280
#from enviroplus import gas
#
#try:
#    from smbus2 import SMBus
#except ImportError:
#    from smbus import SMBus


# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.05

########################
#  Initialize Sensor   #
########################

#bus = SMBus(1)
#bme280 = BME280(i2c_dev=bus)

#################
#  API Routes   #
#################

# temperature route
#def temperature():
#    temps = [get_cpu_temperature()] * 4
#    cpu = get_cpu_temperature()
#
#    # Decrease Variations
#    temps = temps[1:] + [cpu]
#    avg = sum(temps) / float(len(temps))
#    raw = bme280.get_temperature()
#    new_temp = raw - ((avg - raw) / factor)
#
#    resp = flask.Response("{:.1f}".format(new_temp))
#    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
#    
#    return resp
#
## humidity route
#def humidity():
#    humidity = bme280.get_humidity()
#    resp = flask.Response("{:.1f}".format(humidity))
#    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
#    return resp
#
## pressure route
#def pressure():
#    pressure = bme280.get_pressure()
#    resp = flask.Response("{:.1f}".format(pressure))
#    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
#    return resp
#
## Reducing(CO) route
#def reducing():
#    co = gas.read_all()
#    co = co.reducing / 1000
#    resp = flask.Response("{:.2f}".format(co))
#    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
#    return resp
#
## Ammonia(NH3) route
#def ammonia():
#    ammonia = gas.read_all()
#    ammonia = ammonia.nh3 / 1000
#    resp = flask.Response("{:.2f}".format(ammonia))
#    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
#    return resp
#
#
## CPU Temperature Compensation
#def get_cpu_temperature():
#    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
#        temp = f.read()
#        temp = int(temp) / 1000.0
#    return temp


@strawberry.type(
    description="A snapshot of current environmental data"
)
class Env:
    temperature: float = strawberry.field(description="Current temperature reading in Celsius")
    humidity: float = strawberry.field(description="Current humidity reading")
    pressure: float = strawberry.field(description="Current pressure reading in mmHg")
    co: float = strawberry.field(description="Reducing gas measurement of Carbon Monoxide")
    nh3: float = strawberry.field(description="Concentration measurement of Ammonia gas")