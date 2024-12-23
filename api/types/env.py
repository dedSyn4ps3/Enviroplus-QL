import asyncio
import strawberry

from bme280 import BME280
from enviroplus import gas

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus


# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.05

########################
#  Initialize Sensor   #
########################

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

########################
#   Sensor Functions   #
########################

async def get_temperature():
    temps = [get_cpu_temperature()] * 4
    cpu = get_cpu_temperature()

    # Decrease Variations
    temps = temps[1:] + [cpu]
    avg = sum(temps) / float(len(temps))
    raw = bme280.get_temperature()
    new_temp = raw - ((avg - raw) / factor)

    return new_temp

async def get_humidity():
    return bme280.get_humidity()

async def get_pressure():
    return bme280.get_pressure()

async def get_co():
    return gas.read_all().reducing / 1000

async def get_nh3():
    return gas.read_all().nh3 / 1000

# CPU Temperature Compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp


@strawberry.type(
    description="A snapshot of current environmental data"
)
class Env:
    temperature: float = strawberry.field(description="Current temperature reading in Celsius")
    humidity: float = strawberry.field(description="Current humidity reading")
    pressure: float = strawberry.field(description="Current pressure reading in mmHg")
    co: float = strawberry.field(description="Reducing gas measurement of Carbon Monoxide")
    nh3: float = strawberry.field(description="Concentration measurement of Ammonia gas")

async def get_env_data() -> Env:
    temperature, humidity, pressure, co, nh3 = await asyncio.gather(
        get_temperature(),
        get_humidity(),
        get_pressure(),
        get_co(),
        get_nh3()
    )
    return Env(
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
        co=co,
        nh3=nh3
    )