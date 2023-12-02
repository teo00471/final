import machine
import time

# Define the UART configuration
uart = machine.UART(1, baudrate=115200, tx=17, rx=16)  # Adjust pins as needed

# Define the LED pin
led_pin = machine.Pin(2, machine.Pin.OUT)  # Assuming GPIO2, adjust as needed

def process_uart_commands():
    while True:
        if uart.any():
            command = uart.readline().decode('utf-8').strip()
            print(f"Received command: {command}")
            execute_command(command)

def execute_command(command):
    if command == 'led_on':
        led_pin.on()
        print("LED turned ON")
    elif command == 'led_off':
        led_pin.off()
        print("LED turned OFF")
    else:
        print("Unknown command")

def main():
    uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=17, rx=16)
    try:
        process_uart_commands()
    except KeyboardInterrupt:
        print("Script stopped.")

if __name__ == "__main__":
    main()
